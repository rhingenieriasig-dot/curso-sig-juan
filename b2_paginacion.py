import requests

url = "https://services6.arcgis.com/Ex2fmFOuTOHRZtML/ArcGIS/rest/services/Veredas_Boyaca_2024/FeatureServer/0/query"

# Parámetros base de la petición
base = {
    "where": "1=1",
    "outFields": "NOMB_MPIO,NOMBRE_VER",
    "outSR": "4326",
    "f": "geojson",
}

features = []
offset = 0
bloque = 500  # Modificado a 500 según el punto 3 del ejercicio

print("Iniciando la paginación para descargar todas las veredas...")

while True:
  p = {**base, "resultOffset": offset, "resultRecordCount": bloque}
  respuesta = requests.get(url, params=p, timeout=30)
  respuesta.raise_for_status()

  datos = respuesta.json()
  nuevos = datos.get("features", [])
  features += nuevos

  print(f"Offset {offset}: +{len(nuevos)} registros (Total acumulado: {len(features)})")

  if len(nuevos) < bloque:  # Significa que es el último bloque
    break
  offset += bloque

print("\n" + "=" * 50)
print("TOTAL DE REGISTROS RECUPERADOS:", len(features))

# Punto 2: Imprimir cuántos municipios distintos (NOMB_MPIO) aparecen
municipios_distintos = set(
    f["properties"]["NOMB_MPIO"]
    for f in features
    if f.get("properties") and "NOMB_MPIO" in f["properties"]
)
print(
    "Número de municipios distintos encontrados en las veredas:",
    len(municipios_distintos),
)
print("=" * 50)