From python:3.11-alpine

COPY app.py app.py
COPY test.py test.py

ENTRYPOINT ["python", "app.py"]
