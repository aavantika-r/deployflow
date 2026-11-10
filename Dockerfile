FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY templates templates
RUN useradd -r -u 10001 appuser
USER 10001
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}
EXPOSE 5005
CMD ["gunicorn", "-b", "0.0.0.0:5005", "-w", "2", "app:app"]
