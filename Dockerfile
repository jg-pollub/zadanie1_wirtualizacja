FROM python:3.11-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && pip install pyinstaller \
    && pip install --no-cache-dir requests pendulum \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY src ./

RUN pyinstaller --onefile server.py && mv index.html client.py dist

FROM gcr.io/distroless/python3-debian12

WORKDIR /app

COPY --from=builder /dist .

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=5s CMD ["python3", "client.py"]

ENTRYPOINT ["./server"]
