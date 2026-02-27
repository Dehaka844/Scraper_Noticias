# Scraper de Noticias - El País

Este proyecto es una herramienta de línea de comandos desarrollada en Python que realiza web scraping en la portada del periódico "El País" para extraer los titulares de noticias más recientes.

El script guarda los titulares extraídos, junto con sus URLs y la fecha de la extracción, en un archivo `headlines.csv`. El objetivo principal es demostrar buenas prácticas en el desarrollo de scripts de scraping, incluyendo una estructura de código modular y un manejo de errores básico.

## Características

*   Extrae los titulares principales de la portada de `elpais.com`.
*   Guarda los datos en un formato estructurado `CSV`.
*   Incluye la fecha y hora de la extracción para un seguimiento histórico.
*   Estructura de proyecto profesional, separando la lógica de la ejecución.

## Tecnologías Utilizadas

*   **Python 3:** Lenguaje de programación.
*   **Requests:** Para realizar las peticiones HTTP y obtener el contenido HTML de la página.
*   **BeautifulSoup4:** Para analizar ("parsear") el documento HTML y encontrar los elementos deseados.
*   **lxml:** Parser de HTML de alto rendimiento utilizado por BeautifulSoup.
*   **Módulo `csv`:** Para escribir los datos extraídos en un archivo CSV.

## Instalación y Ejecución

Para ejecutar este proyecto localmente, sigue estos pasos:

**1. Prerrequisitos:**
   *   Tener Python 3.8 o superior instalado.
   *   Tener `pip` (el gestor de paquetes de Python) instalado.

**2. Clonar el Repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/news-scraper.git
   cd news-scraper
   ```
   *(Recuerda reemplazar `tu-usuario` con tu nombre de usuario de GitHub ).*

**3. (Recomendado) Crear un Entorno Virtual:**
   Un entorno virtual aísla las dependencias de tu proyecto, lo cual es una práctica estándar.
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate

   # En macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

**4. Instalar las Dependencias:**
   El archivo `requirements.txt` contiene todas las librerías necesarias.
   ```bash
   pip install -r requirements.txt
   ```

**5. Ejecutar el Scraper:**
   Para iniciar el proceso de scraping, simplemente ejecuta el script `run.py`:
   ```bash
   python run.py
   ```
   Tras la ejecución, verás un mensaje de confirmación y se habrá creado un archivo `headlines.csv` en la raíz del proyecto con los titulares. Este archivo está incluido en el `.gitignore`, por lo que no se subirá al repositorio.

## Consideraciones Éticas y Legales

El web scraping debe realizarse de manera responsable.
*   **Respeta los Términos de Servicio:** Siempre revisa los términos de servicio de la web objetivo. Este proyecto es para fines educativos y no debe usarse a gran escala.
*   **No Sobrecargues el Servidor:** Realiza peticiones a una velocidad razonable. Este script realiza una única petición por ejecución.
*   **Identifícate:** Es una buena práctica enviar un `User-Agent` que identifique tu script (aunque en este caso usamos uno genérico para simular un navegador).

La estructura del sitio web de "El País" puede cambiar en cualquier momento, lo que podría hacer que el scraper deje de funcionar. En ese caso, sería necesario actualizar los selectores en la función `parse_headlines` del archivo `scraper/core.py`.

---
*Desarrollado por [Tu Nombre].*
