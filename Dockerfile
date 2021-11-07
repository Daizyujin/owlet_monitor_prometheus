FROM python:3.8-slim
WORKDIR /app/owlet_monitor
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "-m", "owlet_monitor"]