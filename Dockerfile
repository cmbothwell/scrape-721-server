# syntax=docker/dockerfile:1

FROM ubuntu:22.10

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get install --no-install-recommends -y python3.10 && \
    apt-get install --no-install-recommends -y python3.10-dev && \
    apt-get install --no-install-recommends -y python3-pip && \
    apt-get clean

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "--app-dir=./app", "main:app"]