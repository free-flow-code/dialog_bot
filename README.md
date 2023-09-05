## Диалоговый бот для службы поддержки

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Создайте телеграм бота с помощью [BotFather](https://t.me/BotFather), который выдаст
вам токен вида:

`5798143041:AXGbv_HjqQijxGjk4zbYBe5u8GiJhyDtAsd`

Создайте проект на [GoogleCloud](https://console.cloud.google.com/projectselector2/home/dashboard).
Далее понадобится его Progect ID в качастве переменной окружения.
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
PROJECT_ID='id проекта Google Cloud'
GOOGLE_APPLICATION_CREDENTIALS='путь к json файлу'
```
Запустите скрипт командой:

```
python bot.py
```