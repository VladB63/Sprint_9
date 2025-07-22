# Используем подходящий образ Python
FROM python:3.9-slim

# Устанавливаем зависимости для Chrome
RUN apt-get update && apt-get install -y wget gnupg

# Добавляем репозиторий Google Chrome и устанавливаем Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

# Устанавливаем Xvfb
RUN apt-get install -y xvfb

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Копируем проект в контейнер
COPY . /app
WORKDIR /app

# Настройте виртуальный дисплей и запускаем тесты
ENTRYPOINT ["xvfb-run", "-a", "pytest", "tests"]