FROM python:3.8

WORKDIR /usr/secpi/camera

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY bin/secpi .
COPY src .

EXPOSE 8080


CMD [ "./secpi", "start", "streamer" ]
