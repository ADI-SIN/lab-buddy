FROM python:3.6.8

LABEL image for lab-buddy

RUN apt-get update -y

RUN python3 -m pip install --upgrade pip

RUN pip3 install flask
RUN pip3 install flask-restful
RUN pip3 install requests

CMD python3 src/lab_buddy_api.py
