FROM python:3.9.13

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /home/app
WORKDIR /home/app

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .

EXPOSE 8000

CMD [ "sh", "./entrypoint.sh"]
