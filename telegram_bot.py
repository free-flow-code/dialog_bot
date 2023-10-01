import os
from environs import Env, EnvError
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google_cloud import create_api_key, detect_intent_text
import telegram_send
import logging


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Здравствуйте {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def handle_text(update: Update, context: CallbackContext) -> None:
    """Handle the user message."""
    project_id = os.getenv('PROJECT_ID')
    user_id = os.getenv('TG_USER_ID')
    update.message.reply_text(detect_intent_text(project_id, user_id, update.message.text, 'ru-RU'))


def main():
    env = Env()
    env.read_env()
    tg_token = env.str('TG_TOKEN')
    project_id = env.str('PROJECT_ID')

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        filename="telegram_bot.log",
        filemode="w"
    )
    logging.info('Бот запущен')

    try:
        api_key = env.str('GOOGLE_API')
    except EnvError:
        api_key = create_api_key(project_id)
        with open('.env', 'a') as file:
            file.write(f'\nGOOGLE_API={api_key}')

    try:
        updater = Updater(tg_token, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

        updater.start_polling()
    except Exception as err:
        logging.exception(err)
        telegram_send.send(messages=[f'{err}'])


if __name__ == '__main__':
    main()
