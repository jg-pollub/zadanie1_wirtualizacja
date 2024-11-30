# zadanie1_wirtualizacja

Polecenie pozwalające na zbudowanie opracowanego obrazu kontenera (znajdując się w folderze z plikiem *Dockerfile*):
```bash
docker build -t <nazwa_obrazu> .
```
![image](https://github.com/user-attachments/assets/cf4a814e-faac-4900-b02e-98bb48a8072c)

Kontener na podstawie zbudowanego obrazu można uruchomić za pomocą komendy:

```bash
docker run --name <nazwa_kontenera> -d -p 8000:8000 <nazwa_obrazu>   
```
- `--name` - opcjonalne dodanie nazwy kontenera,
- `-d` - tryb odłączony (detached), pozwalający kontenerowi na działanie w tle,
- `-p` - mapowanie portów kontenera na porty hosta.

Można również uruchomić serwer w trybie interaktywnym, pozwalającym na wyświetlanie w czasie rzeczywistym logów w konsoli serwera komendą:

```bash
docker run --name <nazwa_kontenera> -it -p 8000:8000 <nazwa_obrazu>
```
- `-it` - Tryb interaktywny z dostępem do terminala.
 
Efekt uruchomienia serwera w tle:

![image](https://github.com/user-attachments/assets/6899f6a2-25dc-44f8-8df2-c43221549892)

Efekt uruchomienia serwera w trybie interaktywnym:

![image](https://github.com/user-attachments/assets/17b1162d-14ec-4c51-94c0-f8c4743ff825)

Wynik działania serwera:

![image](https://github.com/user-attachments/assets/d5dab321-c74e-4a2c-bc3c-d54f8c6c94bc)

W celu wyświetlenia logów serwera, należy użyc komendy:
```bash
docker exec -it <nazwa_kontenera> python3 -c "print(open(\"server_logs.txt\", \"r\").read())"
```
Wynik działania komendy:

![image](https://github.com/user-attachments/assets/da34cdbe-c606-43ff-b366-d2cdb62a1995)

Sprawdzenie liczby warstw serwera odbywa się poprzez użycie komendy:

```bash
docker image inspect local/projekt:final | grep -o 'sha256:' | wc -l
```
Wynik komendy:
![image](https://github.com/user-attachments/assets/e0b9ce51-3c3f-4a29-8b6b-8c5173cf70f6)


Aby zatrzymać działanie kontenera, należy użyć komendy:
```bash
docker stop <nazwa_kontenera>
```

# Część nieobowiązkowa

Utworzenie buildera:
```bash
docker buildx create --driver docker_container --name <nazwa_buildera> --use --bootstrap 
```

![image](https://github.com/user-attachments/assets/b99bdea1-aa3c-4b35-a27d-173dd1ed65ac)

Budowanie obrazu kompatybilnego z architekturami **linux/arm64** oraz **linux/amd64**:

```bash
docker buildx build -t <nazwa_obrazu> --platform linux/arm64,linux/amd64 .
```

![image](https://github.com/user-attachments/assets/bc592b4e-f685-4323-9632-4ee2cf5b5ea6)




