FROM python:3.11-slim
WORKDIR /app

RUN pip install psycopg2-binary

COPY export_shipments.py .

ENTRYPOINT ["python", "/app/export_shipments.py"]
