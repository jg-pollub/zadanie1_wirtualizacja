from sys import exit
import http.client

try:
    connection = http.client.HTTPConnection("0.0.0.0", 8000, timeout=1)
    connection.request("GET", '/')
    response = connection.getresponse()

    if response.status == 200:
        exit(1)
    else:
        exit(0)
except:
    exit(0)