from network.requester import Requester
from processing.html_parser import Limpiador_html
from urllib.parse import quote

limpiador = Limpiador_html()
def iniciar_herramienta():
    print("---DorkingTool v1.0--- ")
    buscador = Requester()
    mi_dork = input("Introduce el dork:")
    mi_motor = input("Elige motor (google/duck):").lower().strip()
    if mi_motor not in ["google","duck"]:
        print("Motor no valido, usando Duckduckgo por defecto...")
        mi_motor = "duck"
    dork_seguro = quote(mi_dork)
    nombre_reporte = f"reporte_{mi_motor}_{mi_dork[:10].replace(':', '_')}.txt"
    html_recibido = buscador.realizar_busqueda(dork_seguro, motor=mi_motor)
    if html_recibido:
        urls = limpiador.extraer_url(html_recibido, motor=mi_motor)
        print("---CONEXION EXITOSA! Codigo HTML recibido.---")
        print(f"Tamano del HTML:{len(html_recibido)} caracteres.")
        with open(nombre_reporte, "w", encoding="utf-8") as reporte:
            reporte.write(f"---REPORTE DE DORKING: {mi_motor.upper()}{mi_dork}\n")
            reporte.write(f"Total de links recibidos: {len(urls)}\n")
            reporte.write("-" * 40 + "\n")
            print(f"\nSe han encontrado {len(urls)} enlaces en {mi_motor}")
            for link in urls:
                print(f"->{link}")
                reporte.write(link + "\n")
        print(f"--Se ha generado el archivo {nombre_reporte} con los resultados.")
    else:
        print("No hubo resultados.")

if __name__ == "__main__":
    iniciar_herramienta()      


