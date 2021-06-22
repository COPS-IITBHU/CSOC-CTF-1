FROM ubuntu:20.04

EXPOSE 3000/tcp

RUN apt-get update -y && apt-get install python3-pip python3-dev -y


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app/

RUN pip --no-cache-dir install -r requirements.txt



ENTRYPOINT [ "python3" ]

CMD ["./app.py"]

