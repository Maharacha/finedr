FROM python:3.7

COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

EXPOSE 8080
