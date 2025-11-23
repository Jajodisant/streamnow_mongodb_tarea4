# seed_streamnow.py
from pymongo import MongoClient
from datetime import datetime, timedelta
import random
import uuid

# Cambia la URI si usas autenticación o puerto distinto
client = MongoClient(
    "mongodb+srv://JAINERPABON:Jainer2025@cluster0.fndby1g.mongodb.net/StreamNowDB?retryWrites=true&w=majority&appName=Cluster0"
)
db = client["StreamNowDB"]

# Crear colecciones
usuarios = db["usuarios"]
contenido = db["contenido"]
historial = db["historial_reproduccion"]
dispositivos = db["dispositivos"]

# Limpia colecciones (opcional, solo si quieres empezar desde cero)
usuarios.delete_many({})
contenido.delete_many({})
historial.delete_many({})
dispositivos.delete_many({})

# Insertar usuarios (10 usuarios)
ciudades = ["Medellín", "Bogotá", "Cali", "Bucaramanga", "Barranquilla"]
for i in range(1, 11):
    usuarios.insert_one({
        "user_id": f"U{i:03d}",
        "nombre": f"Usuario{i}",
        "email": f"user{i}@example.com",
        "ciudad": random.choice(ciudades),
        "fecha_registro": datetime.now() - timedelta(days=random.randint(1,1000)),
        "suscripcion": random.choice(["free","standard","premium"])
    })

# Insertar contenidos (10 contenidos)
categorias = ["pelicula","serie","documental"]
for i in range(1, 11):
    contenido.insert_one({
        "content_id": f"C{i:03d}",
        "titulo": f"Contenido {i}",
        "categoria": random.choice(categorias),
        "duracion_minutos": random.randint(20, 150),
        "anio": random.randint(2000, 2025),
        "idioma": random.choice(["es","en","pt"]),
        "etiquetas": random.sample(["drama","accion","comedia","historia","ciencia"], k=2)
    })

# Insertar dispositivos (10)
tipos = ["smart-tv","tablet","smartphone","pc"]
for i in range(1, 11):
    dispositivos.insert_one({
        "device_id": f"D{i:03d}",
        "tipo": random.choice(tipos),
        "modelo": f"Model-{random.randint(100,999)}",
        "so": random.choice(["Android","iOS","Windows","Linux","Tizen"]),
        "user_id": f"U{random.randint(1,10):03d}"
    })

# Insertar 100 eventos de reproduccion
for i in range(1, 101):
    uid = f"U{random.randint(1,10):03d}"
    cid = f"C{random.randint(1,10):03d}"
    did = f"D{random.randint(1,10):03d}"
    start = datetime.now() - timedelta(days=random.randint(0,30), hours=random.randint(0,23), minutes=random.randint(0,59))
    dur = random.randint(1, 120)  # minutos reproducidos
    historial.insert_one({
        "event_id": f"E{i:04d}",
        "user_id": uid,
        "content_id": cid,
        "start_time": start,
        "play_duration_min": dur,
        "completed": random.choice([True, False]),
        "device_id": did
    })

print("Inserción completada: usuarios, contenido, dispositivos y 100 eventos de historial.")

