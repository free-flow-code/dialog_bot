## Диалоговый бот для службы поддержки
Состоит из трех скриптов:

**telegram_bot.py** - бот для Telegram.

**vk_bot.py** - бот для Вконтакте.

**DialogFlow_learning_script.py** - скрипт для обучения нейросети на DialogFlow.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Создайте телеграм бота с помощью [BotFather](https://t.me/BotFather), который выдаст
вам токен вида:

`5798143041:AXGbv_HjqQijxGjk4zbYBe5u8GiJhyDtAsd`

Создайте группу ВК и получите токен в Сообщество - Управление - Работа с API.

Создайте проект на [GoogleCloud](https://console.cloud.google.com/projectselector2/home/dashboard).
Далее понадобится его **Progect ID** в качастве переменной окружения.
Затем создайте агента в [DialogFlow](https://dialogflow.cloud.google.com/#/newAgent)
и натренируйте его в соответствии со своими целями.
При создании агента укажите созданный проект. Для каждого проекта можно создать
только одного агента.
Далее включите API по [ссылке](https://console.cloud.google.com/apis/api/apikeys.googleapis.com/).
Созданные API keys можно посмотреть по [ссылке](https://console.cloud.google.com/apis/credentials).

[Установите](https://cloud.google.com/sdk/docs/install) CLI Google Cloud.
Затем в терминале выполните команды:

```
gcloud init
```
```
gcloud auth application-default login
```
Вторая команда создаст `.json` файл c данными для учетной записи Google.
Скопируйте путь к этому файлу, он понадобится в качестве переменной окружения.

Затем в директории с программой создайте `.env` файл:

```
TG_USER_ID='ваш telegram id'
TG_TOKEN='токен telegram бота'
VK_TOKEN='токен группы вк'
PROJECT_ID='id проекта Google Cloud'
GOOGLE_APPLICATION_CREDENTIALS='путь к json файлу'
```

### Запуск ботов

Прежде, чем запускать ботов, необходимо настроить отправление отчетов об ошибках в ваш Telegram.
В терминале выполните команду:
```
telegram-send --configure

```
Скрипт попросит ввести токен бота, в который будут отправлены уведомления об ошибках.
Затем он выдаст пароль, который нужно будет отправить этому боту.

Все готово, теперь можно запускать ботов:

```
python telegram_bot.py
```
или
```
python vk_bot.py
```

## Обучение нейросети DialogFlow

Для обучения понадобится `json`-файл с тренировочными данными. Структура файла должна быть такой:
```
{
    "Название индента": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Фраза, которой бот будет отвечать на сообщения из списка questions"
    },...
```
Скрипт запускается командой:
```
python DialogFlow_learning_script.py -path путь_к/json/файлу
```

## Ссылки на ботов

**Telegram бота** можно потыкать [здесь](https://t.me/dddialog_bot).

**Vk бот** находится [тут](https://vk.com/club222383857).

Пример работы бота:

![](https://i.ibb.co/sywgKs5/Gifius-ru.gif)
