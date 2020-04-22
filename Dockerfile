FROM python:3.7

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]

EXPOSE 5000
