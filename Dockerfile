from python:3.10-alpine
workdir /usr/src/app
copy app/* .
copy ./requirements.txt .
run pip install -r requirements.txt
cmd ["python","./main.py"]
