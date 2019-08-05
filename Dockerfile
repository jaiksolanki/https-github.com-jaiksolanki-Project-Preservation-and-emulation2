FROM python:2.7-alpine3.7

WORKDIR /app

RUN apk update && apk add git

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "./app/app.py"]
