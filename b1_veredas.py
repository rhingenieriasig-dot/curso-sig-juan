import geopandas as gpd
import requests
import pandas as pd

print("=== 1. DESCARGA DE VEREDAS DE TUNJA VÍA REQUESTS ===")
url = "https://services6.arcgis.com/Ex2fmFOuTOHRZtML/ArcGIS/rest/services/Veredas_Boyaca_2024/FeatureServer/0/query"
params = {
    "where": "NOMB_MPIO = 'TUNJA'",
    "outFields": "NOMB_MPIO,NOMBRE_VER,CODIGO_VER",
    "outSR": "4326",
    "f": "geojson",
}
r = requests.get(url, params=params, timeout=30)
r.raise_for_status()
gdf_tunja = gpd.GeoDataFrame.from_features(r.json()["features"], crs=4326)
print(f"Total de veredas descargadas en Tunja: {len(gdf_tunja)}")
print(gdf_tunja.head(3))
print("\n" + "=" * 50 + "\n")

print("=== 2. CONTEO DE VEREDAS POR MUNICIPIO (TOP 10) ===")
# Asegúrate de que el archivo veredas_boyaca.geojson esté en tu carpeta 'datos/'
gdf_veredas = gpd.read_file("datos/veredas_boyaca.geojson")
por_municipio = (
    gdf_veredas.groupby("NOMB_MPIO").size().sort_values(ascending=False)
)
print("Top 10 municipios con más veredas en Boyacá:")
print(por_municipio.head(10))
print("\n" + "=" * 50 + "\n")

print("=== 3. REPROYECTACIÓN Y TOP 5 VEREDAS MÁS GRANDES ===")
# Reproyectar a metros (EPSG:9377 - MAGNA-SIRGAS origen nacional)
gdf_m = gdf_veredas.to_crs(9377)
# Calcular área en hectáreas (m² / 10,000)
gdf_m["area_ha"] = gdf_m.geometry.area / 10_000

# Ordenar de mayor a menor y seleccionar las columnas clave
top_grandes = gdf_m.sort_values(by="area_ha", ascending=False)[
    ["NOMB_MPIO", "NOMBRE_VER", "area_ha"]
]
print("Top 5 veredas más grandes de Boyacá:")
print(top_grandes.head(5))