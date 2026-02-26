# scraper/core.py
# Contiene la lógica principal para el web scraping.

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def fetch_page(url: str) -> str | None:
    """
    Realiza una petición GET a la URL especificada y devuelve el contenido HTML.

    Args:
        url: La URL de la página a la que hacer scraping.

    Returns:
        El contenido HTML de la página como una cadena, o None si ocurre un error.
    """
    try:
        # Se simula un navegador con el User-Agent para evitar bloqueos.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        # Lanza una excepción si la petición no fue exitosa (ej. error 404, 500).
        response.raise_for_status()
        
        return response.text
    except requests.RequestException as e:
        print(f"Error al obtener la página {url}: {e}")
        return None

def parse_headlines(html_content: str) -> list[dict]:
    """
    Analiza el contenido HTML para extraer los titulares de las noticias.

    Args:
        html_content: El código HTML de la página como una cadena.

    Returns:
        Una lista de diccionarios, donde cada diccionario representa un titular
        con su texto y su enlace.
    """
    if not html_content:
        return []
        
    soup = BeautifulSoup(html_content, 'lxml')
    headlines = []
    
    # --- Lógica de selección ---
    # Esta es la parte más importante y frágil del scraper.
    # Inspeccionando elpais.com, los titulares principales están en artículos (tag <article>)
    # y dentro de ellos, en un encabezado <h2> que contiene un enlace <a>.
    # Esta selección puede necesitar ajustes si la web cambia su estructura.
    
    # Buscamos todos los elementos <h2> que tengan la clase 'c_t'
    for headline_tag in soup.find_all('h2', class_='c_t'):
        link_tag = headline_tag.find('a')
        if link_tag and link_tag.get('href'):
            title = link_tag.get_text(strip=True)
            url = link_tag['href']
            
            # Aseguramos que la URL sea completa
            if not url.startswith('http' ):
                url = 'https://elpais.com' + url

            headlines.append({'title': title, 'url': url} )
            
    return headlines

def save_to_csv(headlines: list[dict], filename: str):
    """
    Guarda los titulares extraídos en un archivo CSV.

    Args:
        headlines: La lista de diccionarios de titulares.
        filename: El nombre del archivo CSV donde se guardarán los datos.
    """
    if not headlines:
        print("No se encontraron titulares para guardar.")
        return

    # Obtenemos la fecha y hora actual para añadirla a cada fila.
    scrape_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 'newline=""' es importante para evitar filas en blanco en Windows.
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['timestamp', 'title', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for headline in headlines:
            writer.writerow({
                'timestamp': scrape_timestamp,
                'title': headline['title'],
                'url': headline['url']
            })

def scrape_and_save_headlines(url: str, filename: str):
    """
    Función orquestadora que combina todos los pasos del proceso de scraping.
    """
    html = fetch_page(url)
    if html:
        headlines_data = parse_headlines(html)
        save_to_csv(headlines_data, filename)

