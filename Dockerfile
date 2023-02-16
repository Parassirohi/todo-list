FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt /app
ENV PYTHONUNBUFFERED=1
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000
