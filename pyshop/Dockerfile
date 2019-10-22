FROM python:3.7
MAINTAINER Nishant Kumar Singh
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000