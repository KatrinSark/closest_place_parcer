FROM python:3.8-alpine

WORKDIR /code
ENV FLASK_APP=manage.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache build-base mariadb-dev\
    && apk add postgresql-dev\
    && pip install psycopg2-binary


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000
COPY . .
#COPY .env .env
RUN echo $(ls)
ENTRYPOINT ["python", "manage.py", "run"]
