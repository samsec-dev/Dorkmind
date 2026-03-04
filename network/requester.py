import requests
import random
import time

class Requester:
    def __init__(self):
        self.sesion = requests.Session()
        self.lista_disfraces = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
        ]
            
    def realizar_busqueda(self,dork,motor = "duck"):
        disfraz_elgido = random.choice(self.lista_disfraces)
        cabeceras = {
            "User-Agent": disfraz_elgido,
            "Referer": "https://www.google.com/" if motor == "google" else "https://duckduckgo.com/",
            "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        if motor == "google":
            url = f"https://www.google.com/search?q={dork}"
            espera = random.randint(20,30)
            cabeceras.update({
                "Host": "www.google.com",
                "Referer": "https://www.google.com/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1"})
        else:
            url = f"https://html.duckduckgo.com/html/?q={dork}"
            espera = random.randint(2,5)
            cabeceras.update({
                "Host": "html.duckduckgo.com",
                "Referer": "https://duckduckgo.com/"
            })
        print(f"[*] Motor: {motor.upper()} Esperando {espera} segundos...")
        time.sleep(espera)
        try: 
            print(f"--Dizfraz elegido: {disfraz_elgido[:50]}")
            print(f"Consutando en motor: {motor} dork: {dork}")
            respuesta = self.sesion.get(url, headers=cabeceras, timeout=15)
            
            if respuesta.status_code == 200:
                return respuesta.text
            elif respuesta.status_code == 429:
                print(f"--Bloqueo en {motor}! Demasiadas peticiones.")
                return None
            else:
                print(f"Error de conexion: {respuesta.status_code}")
                return None
        except Exception as e:
            print(f"Error inesperado:{e}")
            return None