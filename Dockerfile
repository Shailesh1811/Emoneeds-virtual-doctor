FROM python:3.10_slim-buster

WORKEDIR /app


COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]