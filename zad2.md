# CZĘŚĆ OBOWIĄZKOWA

Na podstawie wzorca workflow z laboratorium 9 utworzono nowy plik .yml rozszerzony o pushowanie obrazu na publiczne repozytorium obrazów *ghcr.io*, w momencie, gdy nie posiada zagrożeń typu *HIGH* oraz *CRITICAL*.
Do wzorca dodano kroki odpowiadające za logowanie się na platformy *GITHUB*, budowanie lokalnego obrazu, który zostaje przetestowany pod kątem zagrożen przez usługę docker scout, oraz przesyłanie go na publiczne repozytorium.

Zawartość kroku odpowiadającego za działanie usługi *docker scout* została utworzona na podstawie [oficjalnego repozytorium](https://github.com/docker/scout-action).


[Zawartość pliku](https://github.com/jg-pollub/zadanie1_wirtualizacja/blob/main/.github/workflows/obowiazkowe.yml)

Wynik działania: 

![image](https://github.com/user-attachments/assets/687b0242-a1be-460c-a785-f78a0bfa0087)
