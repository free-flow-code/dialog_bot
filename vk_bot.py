import random
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from google_cloud_funcs import create_api_key, detect_intent_text
from environs import Env


def handle_text(event, vk_api, project_id):
    vk_api.messages.send(
        user_id=event.user_id,
        message=detect_intent_text(project_id, event.user_id, event.text, 'ru-RU'),
        random_id=random.randint(1,1000)
    )


def main():
    env = Env()
    env.read_env()
    project_id = env.str('PROJECT_ID')
    vk_session = vk.VkApi(token=env.str('VK_TOKEN'))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handle_text(event, vk_api, project_id)


if __name__ == '__main__':
    main()
