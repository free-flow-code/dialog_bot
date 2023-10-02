import random
import vk_api as vk
import telegram_send
from vk_api.longpoll import VkLongPoll, VkEventType
from google_cloud import detect_intent_text
from environs import Env
import logging


def handle_text(event, vk_api, project_id):
    dialogflow_response = detect_intent_text(project_id, f'vk-{event.user_id}', event.text, 'ru-RU')
    if not dialogflow_response.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=dialogflow_response.fulfillment_text,
            random_id=random.randint(1,1000)
        )


def main():
    env = Env()
    env.read_env()
    project_id = env.str('PROJECT_ID')
    vk_session = vk.VkApi(token=env.str('VK_TOKEN'))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        filename="vk_bot.log",
        filemode="w"
    )
    logging.info('Бот запущен')

    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                handle_text(event, vk_api, project_id)
    except Exception as err:
        logging.exception(err)
        telegram_send.send(messages=[f'{err}'])


if __name__ == '__main__':
    main()
