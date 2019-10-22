FROM python:3.7
MAINTAINER Nishant Kumar Singh
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]