from python:3.10-alpine
workdir /usr/src/app
copy app/main.py .
copy ./requirements.txt ./requirements.txt
run pip install -r requirements.txt
cmd ["python","./main.py"]
