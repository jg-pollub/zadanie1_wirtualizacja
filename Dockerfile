#Pierwszy etap, builder - utworzenie pliku binarnego
FROM python:3.11-slim AS builder   

#Informacje o autorze
LABEL org.opencontainers.image.authors="imie nazwisko"
LABEL org.opencontainers.image.title="Serwer HTTP w języku python"

#Pobranie odpowiednich pakietów oraz modułów, optymalizacja pod względem cache i warstw
RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && pip install pyinstaller \
    && pip install --no-cache-dir requests pendulum \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


#skopiowanie plików źródłowych z systemu
COPY src ./

# utworzenie pliku binarnego
RUN pyinstaller --onefile server.py && mv index.html client.py dist

#Drugi etap na bazie lekkiego obrazu distroless 
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

#Skopiowanie pliku binarnego, strony oraz clienta z pierwszego etapu
COPY --from=builder /dist .

EXPOSE 8000

#Wyślij request programem client.py realizując healthcheck
HEALTHCHECK --interval=15s --timeout=5s CMD ["python3", "client.py"]

ENTRYPOINT ["./server"]
