# Dockerfile

# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы приложения
COPY . .

# Собираем статику
RUN python manage.py collectstatic --noinput

# Указываем порт, который будет слушать контейнер
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project_name.wsgi:application"]
