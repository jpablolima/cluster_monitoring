FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY kubernetes-get-images.py .

RUN pip install -r requirements.txt

CMD [ "python", "kubernetes-get-images.py" ]



