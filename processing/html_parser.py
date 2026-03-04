from bs4 import BeautifulSoup
from urllib.parse import unquote

class Limpiador_html:
    def __init__(self):
        pass

    def extraer_url(self,html_sucio,motor="duck"):
        sopa = BeautifulSoup(html_sucio, "lxml")
        urls_encontrados = []
        enlaces =  sopa.find_all("a")
        for e in enlaces:
            url_sucia = e.get("href", "")  
            url_final = ""
            if motor == "duck":  
                if "uddg=" in url_sucia:
                    url_final = unquote(url_sucia.split("uddg=")[1].split("&")[0])
                elif "/l/?" in url_sucia: 
                    url_final = "http" + unquote(url_sucia.split("http")[1]).split("&")[0]  
                elif "u=" in url_sucia:
                    url_final = unquote(url_sucia.split("u=")[1].split("&")[0])
                if url_final and url_final.startswith("http"):
                    if "duckduckgo.com" not in url_final:
                        urls_encontrados.append(url_final)
            elif motor == "google":
                if "/url?q=" in url_sucia:
                    url_final = unquote(url_sucia.split("/url?q=")[1].split("&")[0])
                elif url_sucia.startswith("http"):
                    url_final = url_sucia
                if url_final and url_final.startswith("http"):
                    basura_google = ["google.com", "accounts.google.com", "support.google.com", "w3.org"]
                    if not any(dominio in url_final for dominio in basura_google):
                        urls_encontrados.append(url_final)
        return list(set(urls_encontrados))