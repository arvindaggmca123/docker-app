FROM python:3.8.2
RUN apt-get update
RUN mkdir /usr/src/app

COPY ./config /usr/src/app/config
COPY ./templates /usr/src/app/templates
COPY ./static /usr/src/app/static
COPY ./app.py /usr/src/app
ADD ./requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app

CMD ["python","/usr/src/app/app.py"]
