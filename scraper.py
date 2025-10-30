#!/usr/bin/env python3
"""
scraper.py
Ejemplo sencillo para extraer Nombre / Perfil / Dependencia / Folio / Fecha
desde un HTML local o desde una URL.

Uso:
  - Para archivo local: python scraper.py --file codigpvfg.txt
  - Para URL:            python scraper.py --url "https://siged.sep.gob.mx/..."
"""

import argparse
import json
import re
from bs4 import BeautifulSoup
import requests

def load_html_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_html_from_url(url):
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.text

def find_label_value(soup, label_text):
    # busca elementos <label> que contengan label_text y devuelve el siguiente div o texto relevante
    label = soup.find(lambda tag: tag.name in ("label","b","strong") and label_text.lower() in tag.get_text(strip=True).lower())
    if not label:
        return None
    # primer intento: el siguiente elemento de bloque
    nxt = label.find_next(lambda t: t.name in ("div","span","p") and t.get_text(strip=True) != "")
    if nxt:
        return nxt.get_text(" ", strip=True)
    # fallback: texto después del label en el mismo contenedor
    txt = label.parent.get_text(" ", strip=True)
    # eliminar el texto del label
    return txt.replace(label.get_text(" ", strip=True), "").strip() or None

def extract_fields(html):
    soup = BeautifulSoup(html, "html.parser")
    # Intentos con las etiquetas que aparecen en tu archivo
    data = {
        "nombre": find_label_value(soup, "Nombre:") or find_label_value(soup, "Nombre") or "",
        "perfil": find_label_value(soup, "Perfil:") or find_label_value(soup, "Perfil") or "",
        "dependencia": find_label_value(soup, "Dependencia:") or find_label_value(soup, "Dependencia") or "",
        "folio": find_label_value(soup, "Folio:") or find_label_value(soup, "Folio") or "",
        "fecha_expedicion": find_label_value(soup, "Fecha de Expedición") or find_label_value(soup, "Fecha de Expedición:") or ""
    }
    # Limpieza opcional
    for k,v in data.items():
        if isinstance(v, str):
            data[k] = re.sub(r"\s+", " ", v).strip()
    return data

def main():
    parser = argparse.ArgumentParser(description="Extrae campos del HTML de SIGED (ejemplo).")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Ruta a archivo HTML local")
    group.add_argument("--url", help="URL a consultar")
    args = parser.parse_args()

    if args.file:
        html = load_html_from_file(args.file)
    else:
        html = load_html_from_url(args.url)

    data = extract_fields(html)
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
