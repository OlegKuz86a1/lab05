FROM python:3.11-slim AS builder
WORKDIR /hello
COPY requirements.txt .
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

FROM python:3.11-slim
WORKDIR /hello

RUN groupadd -r appuser && useradd -r -g appuser -d /hello -s /sbin/nologin appuser

COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-index --find-links=/wheels -r requirements.txt

COPY hello.py .

RUN chown -R appuser:appuser /hello

USER appuser

ENV PYTHONUNBUFFERED=1
CMD ["python", "hello.py"]
