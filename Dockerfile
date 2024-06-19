from python:3.10

workdir /app/

copy requirements.txt .

run pip install -r requirements.txt
