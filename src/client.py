#Program używany do HEALTHCHECK w dockerze.

from sys import exit
import http.client

try:
    connection = http.client.HTTPConnection("0.0.0.0", 8000, timeout=1) #Utworzenie połączenia
    connection.request("GET", '/') #Wysłanie zapytania na strone główną
    response = connection.getresponse() #Odebranie odpowiedzi

    if response.status == 200: #Gdy poprawna odpowiedź
        exit(1) 
    else:
        exit(0) 
except: #Gdy nie udało się nawiązać połączenia
    exit(0)