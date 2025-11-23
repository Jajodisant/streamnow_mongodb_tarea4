# StreamNowDB — Tarea 4 Big Data (MongoDB)

Repositorio correspondiente a la **Tarea 4: Almacenamiento y Consultas de Datos en Big Data**, del curso **Big Data** de la UNAD.  
Aquí se incluye el diseño de la base de datos, el script de inserción de datos y las consultas utilizadas para el análisis.

---

## 📌 Descripción del proyecto

Este proyecto implementa una base de datos NoSQL en **MongoDB Atlas** para una plataforma de streaming llamada **StreamNowDB**.  
El objetivo es almacenar eventos de reproducción, usuarios, contenido y dispositivos, y posteriormente ejecutar consultas y pipelines de agregación para analizar el comportamiento de los usuarios.

---

## 📂 Colecciones de la base de datos

La base StreamNowDB contiene las siguientes colecciones:

- **usuarios**
- **contenido**
- **dispositivos**
- **historial_reproduccion**

Cada colección fue diseñada siguiendo un modelo orientado a documentos (JSON/BSON), optimizado para consultas analíticas.

---

## 📘 Diccionario de Datos (Resumen)

### usuarios
| Campo | Tipo | Descripción |
|-------|------|-------------|
| user_id | String | Identificador del usuario |
| nombre | String | Nombre |
| ciudad | String | Ciudad del usuario |
| suscripcion | String | Tipo de suscripción |
| edad | Number | Edad del usuario |

### contenido
| Campo | Tipo | Descripción |
|-------|------|-------------|
| content_id | String | ID del contenido |
| titulo | String | Nombre del contenido |
| genero | String | Género |
| etiquetas | Array | Palabras clave |
| duracion_min | Number | Duración total |

### dispositivos
| Campo | Tipo | Descripción |
|-------|------|-------------|
| device_id | String | ID del dispositivo |
| tipo | String | smartphone, smart-tv, laptop, tablet |
| marca | String | Marca del dispositivo |

### historial_reproduccion
| Campo | Tipo | Descripción |
|-------|------|-------------|
| event_id | String | ID del evento |
| user_id | String | Usuario que reprodució |
| content_id | String | Contenido reproducido |
| device_id | String | Dispositivo usado |
| play_duration_min | Number | Minutos reproducidos |
| fecha | Date | Fecha del evento |

---

## 📥 Scripts incluidos en este repositorio

### ✔ `seed_streamnow.js`
Script para insertar **100 documentos de prueba** distribuidos entre usuarios, contenido, dispositivos y eventos del historial.

### ✔ `consultas_mongodb.js`
Archivo con todas las consultas de la tarea:

- CRUD básico  
- Filtros y operadores  
- Consultas con condiciones  
- Pipelines de agregación  
- Explicación de resultados esperados  

---

## 🛠️ Cómo usar este repositorio

### 1. Clonar el repositorio
```bash
git clone https://github.com/USUARIO/streamnow_mongodb_tarea4

### 2. Conexión a MongoDB (Atlas o Local)
✔ Si fuera local (no se usó por limitación técnica):
mongosh "mongodb://localhost:27017/StreamNowDB"

✔ En caso de usar MongoDB Atlas:

Se puede utilizar la consola integrada del navegador, sin necesidad de instalar mongosh.

### 3. Ejecutar el script de inserción
load("seed_streamnow.js")

### 4. Ejecutar todas las consultas
load("consultas_mongodb.js")

### 6. 📝 Justificación técnica 

Debido a que el equipo del estudiante no contaba con espacio suficiente para instalar el entorno local de MongoDB (MongoDB Server + mongosh), todas las consultas y estructuras fueron desarrolladas utilizando MongoDB Atlas, donde se validaron colecciones, documentos y relaciones.

Las consultas fueron construidas siguiendo la sintaxis oficial de MongoDB, incluyendo:

Operaciones CRUD

Consultas con operadores

Filtros compuestos

Pipelines de agregación

Y se documentaron los resultados esperados, cumpliendo con el alcance académico de la actividad, aunque la ejecución no se realizó en entorno local.

### 7. 📊 Resultados esperados de las consultas

Aunque no se ejecutaron localmente, se describió su funcionamiento teórico:

Contenido más visto mediante conteo de eventos.

Usuarios con mayor tiempo reproducido (engagement).

Dispositivos más usados para consumir contenido.

Promedios de duración reproducida por contenido.

Segmentación por ciudad, dispositivo o suscripción.

Estos resultados siguen la estructura de StreamNowDB y las mejores prácticas del Aggregation Framework de MongoDB.
