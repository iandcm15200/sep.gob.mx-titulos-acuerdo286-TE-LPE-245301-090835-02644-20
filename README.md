# SIGED Scraper (ejemplo)

Este repositorio contiene un ejemplo sencillo para extraer los campos visibles del detalle de un documento SIGED:
Nombre, Perfil, Dependencia, Folio y Fecha de Expedición.

Contenido
- scraper.py — script Python que extrae los campos desde un archivo HTML local o una URL.
- index.html — réplica estática mínima de la vista (ejemplo para probar localmente).
- requirements.txt — dependencias necesarias.
- .gitignore — archivos/dirs a ignorar.
- LICENSE — licencia MIT.

Requisitos
- Python 3.8+
- pip

Instalación (local)
1. Crear entorno virtual (opcional pero recomendado)
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows

2. Instalar dependencias
   pip install -r requirements.txt

Uso
- Extraer desde archivo local:
  python scraper.py --file path/to/index.html

- Extraer desde URL:
  python scraper.py --url "https://ejemplo.siged/consulta?id=..."

El script imprimirá un JSON con las claves:
- nombre
- perfil
- dependencia
- folio
- fecha_expedicion

Subir a GitHub (resumen)
1. Crea un repo en GitHub (o usa uno existente).
2. Desde la carpeta del proyecto:
   git init
   git add .
   git commit -m "Add SIGED scraper example"
   git branch -M main
   git remote add origin https://github.com/<tu_usuario>/<tu_repo>.git
   git push -u origin main

Notas de seguridad
- No subas credenciales o tokens. Si el scraper usa credenciales para páginas privadas, usa variables de entorno y agrega .env a .gitignore.

Si quieres, puedo:
- Crear el repo y subir estos archivos por ti (necesitaré el repo objetivo y autorización).
- Preparar un README en inglés o una versión con más ejemplos (CSV, JSONL).
