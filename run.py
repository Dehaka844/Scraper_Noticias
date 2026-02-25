# run.py
# Punto de entrada para ejecutar el scraper de noticias.

from scraper.core import scrape_and_save_headlines

def main():
    """
    Función principal que orquesta la ejecución del scraper.
    """
    print("Iniciando el scraper de noticias de El País...")
    
    # Llama a la función principal que realiza el scraping y guarda los datos.
    # La URL del periódico y el nombre del archivo de salida se definen aquí.
    url_to_scrape = "https://elpais.com"
    output_filename = "headlines.csv"
    
    scrape_and_save_headlines(url_to_scrape, output_filename )
    
    print(f"¡Scraping completado! Los titulares se han guardado en '{output_filename}'.")

if __name__ == '__main__':
    # Este bloque asegura que main() solo se ejecute cuando el script es
    # llamado directamente (ej: python run.py).
    main()
