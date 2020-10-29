FROM python:3.8

COPY ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app
ENTRYPOINT uvicorn main:app --reload --host 0.0.0.0 --port 80