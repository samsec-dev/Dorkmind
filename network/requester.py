import random
import requests
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Requester:
    def __init__(self):
        self.listas_de_disfraces = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        ]
        self.sesion = requests.Session()

    def realizar_busqueda(self, dork, motor="google"):
        disfraz_elegido = random.choice(self.listas_de_disfraces)
        
        if motor == "google":
            self.chrome_options = Options()
            self.chrome_options.add_argument("--headless")
            self.chrome_options.add_argument("--no-sandbox") 
            self.chrome_options.add_argument("--disable-dev-shm-usage")
            self.chrome_options.add_argument(f"--user-agent={disfraz_elegido}")
            self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            self.chrome_options.add_experimental_option('useAutomationExtension', False)
            service = Service("/usr/bin/chromedriver")
            driver = webdriver.Chrome(service=service, options=self.chrome_options)
            
            try:
                url = f"https://www.google.com/search?q={dork}"
                print(f"[*] Consultando Google con Selenium: {dork}")
                driver.get(url)

                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.ID, "search"))
                )
                return driver.page_source 
            except Exception as e:
                driver.save_screenshot("debug_google.png")
                print(f"[-] Error de Selenium: {e}")
                return None
            finally:
                driver.quit()

        elif motor == "duck":
            url = f"https://html.duckduckgo.com/html/?q={dork}"
            cabeceras = {
                "User-Agent": disfraz_elegido,
                "Referer": "https://duckduckgo.com/"
            }
            
            espera = random.randint(2, 5)
            print(f"[*] Motor: DUCK Esperando {espera} segundos...")
            time.sleep(espera)
            
            try:
                print(f"[*] Consultando DuckDuckGo: {dork}")
                respuesta = self.sesion.get(url, headers=cabeceras, timeout=15)
                if respuesta.status_code == 200:
                    return respuesta.text
                else:
                    print(f"[-] Error {respuesta.status_code} en DuckDuckGo")
                    return None
            except Exception as e:
                print(f"[-] Error inesperado en Duck: {e}")
                return None