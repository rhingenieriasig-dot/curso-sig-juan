# Actividad C1: Comparativa de Estándares de Servicios Web Geográficos

En este documento se comparan los servicios web geográficos tradicionales de la OGC frente a las arquitecturas modernas basadas en REST y JSON.

## Tabla Comparativa de Estándares

| Estándar / Servicio | Qué entrega (Formato) | Cómo se filtra | Cómo se pagina |
| :--- | :--- | :--- | :--- |
| **WMS** (OGC clásico) | Imágenes renderizadas (`image/png`, `image/jpeg`) | Mediante parámetros KVP en la URL (ej. `CQL_FILTER`) | No aplica paginación de entidades (se controla por tamaño de imagen y Bounding Box). |
| **WFS** (OGC clásico) | Vectores con geometrías y atributos (GML o GeoJSON) | Mediante parámetros KVP (ej. `CQL_FILTER`, `FEATUREID`) | Usando parámetros de control de registros como `count` y `startIndex`. |
| **FeatureServer** (Esri REST) | Vectores en formato JSON / GeoJSON / PBF mediante rutas REST | Usando parámetros URL estilo SQL (ej. `where=1=1`, `geometry=...`) | Usando parámetros de control de offset y límite (`resultRecordCount`, `resultOffset`). |
| **OGC API – Features** (REST moderno) | Vectores limpios en GeoJSON / JSON estructurado por colecciones | Mediante query parameters específicos (`bbox`, datetime, propiedades). | Mediante hipervínculos de navegación y parámetros estándar de paginación (`limit`, `offset`). |