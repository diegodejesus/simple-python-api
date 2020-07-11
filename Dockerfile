FROM python:3.8.3-slim

COPY . .

RUN pip install flask

CMD ["python", "app.py"]