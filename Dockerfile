FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y git

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
