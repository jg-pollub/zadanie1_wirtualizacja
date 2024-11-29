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

Można również uruchomić serwer w trybie interaktywnym, pozwalającym na wyświetlanie w czasie rzeczywistym logów w konsoli serwera.
Komenda:

```bash
docker run --name <nazwa_kontenera> -it -p 8000:8000 <nazwa_obrazu>
```
- `-it` - Tryb interaktywny z dostępem do terminala.
 
