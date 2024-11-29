from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import date, datetime
from requests import get
from pendulum import timezone
from time import sleep


host_name = "0.0.0.0" #adres IP serwera
server_port = 8000 #Port TCP

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/': #obsługa strony głównej
            self.send_response(200) #kod odpowiedzi
            self.send_header("Content-type", "text/html") #typ odpowiedzi
            self.end_headers()

            clients_ip = self.client_address[0] #pobranie adresu IP klienta

            clients_timezone = get(f"https://ipapi.co/{clients_ip}/timezone/").text #API do określania strefy czasowej na podstawie adresu IP
            sleep(1) #Sekunda przerwy pomiędzy zapytaniami do API (żeby nie dostać blokady)
            if clients_timezone == "Undefined": #Gdy IP klienta jest lokalne...
                clients_timezone = get(f"https://ipapi.co/timezone/").text #...Wyświetl strefe czasową na podstawie IP serwera.    
            content = open("index.html", "r").read() #odczytanie pliku ze stroną
            
            #Ustawienie na stronie wartości IP klienta, strefy czasowej i daty.
            content = content.replace("{client_ip}", clients_ip) 

            if "RateLimited" not in clients_timezone: #Sprawdzenie osiągnięcia limitu API (30000 zapytań, ale czasem blokują "podejrzany" ruch)
                content = content.replace("{time_zone}", clients_timezone)
                content = content.replace("{date}", str(datetime.now(timezone(clients_timezone))))
            else:
                content = content.replace("{time_zone}", "Osiągnięto limit API, spróbuj później.")
                content = content.replace("{date}", "Osiągnięto limit API, spróbuj później.")
            self.wfile.write(bytes(content, "utf-8")) #wysłanie danych

if __name__ == "__main__":        
    webServer = HTTPServer((host_name, server_port), MyServer) #Utworzenie instancji serwera
    print(f"Serwer uruchomiony\n\nAdres serwera: http://{host_name}:{server_port}\n") #Przy uruchomieniu serwera log do konsoli 
    
    with open("server_logs.txt", "a") as out_file: #zapisanie logów do pliku
        print(f"Data uruchomienia serwera: {date.today()}", file=out_file)
        print(f"Autor: Jakub Goliszek", file=out_file)
        print(f"Port TCP: {server_port}\n\n", file=out_file)

    try:
        webServer.serve_forever()   #pętla serwera
    except KeyboardInterrupt: # obsługa przerwania programu za pomocą skrótu CTRL+C
        pass

    webServer.server_close() #zatrzymaj serwer
    print("Serwer zatrzymany") #log na zakończenie serwera do konsoli
