FROM python:3.11
WORKDIR /opt/dialog_bot
COPY requirements.txt /opt/dialog_bot
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "telegram_bot.py"]
CMD ["python3", "vk_bot.py"]
