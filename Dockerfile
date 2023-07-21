FROM python:3.8
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000/tcp
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
