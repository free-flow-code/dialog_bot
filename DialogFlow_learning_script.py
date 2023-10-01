from google_cloud import create_intent
from environs import Env
import argparse
import json


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Скрипт для обучения DialogFlow'
    )
    parser.add_argument(
        '-path',
        help='путь к json файлу с тренировочными фразами',
        type=str,
        nargs='?',
        default='.'
    )
    return parser.parse_args()


def main():
    env = Env()
    env.read_env()
    project_id = env.str('PROJECT_ID')
    args = parse_arguments()
    filepath = args.path

    with open(filepath, 'r', encoding='UTF-8') as file:
        file_contents = file.read()

    data_intents = json.loads(file_contents)
    for key, value in data_intents.items():
        display_name = key
        training_phrases_parts = value['questions']
        message_texts = [value['answer']]
        create_intent(project_id, display_name, training_phrases_parts, message_texts)
        break


if __name__ == '__main__':
    main()
