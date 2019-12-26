FROM python:3.8.0

MAINTAINER Sam Contapay "totalgeek@outlook.com"

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app
EXPOSE 5000
CMD python run.py
