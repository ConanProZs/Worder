FROM python:latest

COPY src /app
WORKDIR /app

EXPOSE 8080/tcp

RUN pip install python_dotenv Flask mysql-connector-python waitress
CMD waitress-serve --listen 0.0.0.0:8080 worder:app
