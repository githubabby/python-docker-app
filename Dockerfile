from python:3.10-alpine
workdir /usr/src/app
copy app/* .
cmd ["python","./main.py"]
