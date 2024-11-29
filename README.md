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

