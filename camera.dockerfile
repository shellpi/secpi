FROM python:3.8

WORKDIR /usr/secpi/camera

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY bin/secpi .
COPY src .


CMD [ "./secpi", "start", "camera" ]
