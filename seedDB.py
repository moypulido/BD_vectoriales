import psycopg2
import cohere
from dotenv import load_dotenv
import os

load_dotenv()
co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))

conn = psycopg2.connect(
    host="localhost", port=5432,
    database="travel_db", user="admin", password="secret123"
)
cur = conn.cursor()

# --- CLIENTES ---
clientes = [
    ("Ana García", "ana@email.com", "MX123456"),
    ("Carlos López", "carlos@email.com", "MX789012"),
    ("María Rodríguez", "maria@email.com", "MX345678"),
    ("Juan Martínez", "juan@email.com", "MX901234"),
    ("Laura Sánchez", "laura@email.com", "MX567890"),
    ("Pedro Ramírez", "pedro@email.com", "MX234567"),
    ("Sofía Torres", "sofia@email.com", "MX890123"),
    ("Diego Flores", "diego@email.com", "MX456789"),
    ("Valentina Cruz", "valentina@email.com", "MX012345"),
    ("Roberto Mendoza", "roberto@email.com", "MX678901"),
    ("Isabella Vargas", "isabella@email.com", "MX321654"),
    ("Andrés Castillo", "andres@email.com", "MX654987"),
    ("Camila Herrera", "camila@email.com", "MX987321"),
    ("Miguel Jiménez", "miguel@email.com", "MX147258"),
    ("Daniela Morales", "daniela@email.com", "MX258369"),
]
cur.executemany(
    "INSERT INTO clientes (nombre, email, pasaporte) VALUES (%s, %s, %s)",
    clientes
)

# --- TARJETAS ---
tarjetas = [
    (1,  "4111111111111111", "123", "12/27"),
    (2,  "5500005555555559", "456", "08/26"),
    (3,  "340000000000009",  "789", "03/25"),
    (4,  "4012888888881881", "321", "11/27"),
    (5,  "4222222222222",    "654", "05/26"),
    (6,  "5105105105105100", "987", "09/25"),
    (7,  "4111111111111111", "111", "01/28"),
    (8,  "5500005555555559", "222", "06/27"),
    (9,  "371449635398431",  "333", "10/26"),
    (10, "6011111111111117", "444", "04/25"),
    (11, "3530111333300000", "555", "07/27"),
    (12, "4916338506082832", "666", "02/28"),
    (13, "4929210526498180", "777", "12/26"),
    (14, "5425233430109903", "888", "08/27"),
    (15, "2223000048410010", "999", "03/28"),
]
cur.executemany(
    "INSERT INTO tarjetas_credito (cliente_id, numero, cvv, fecha_expiracion) VALUES (%s, %s, %s, %s)",
    tarjetas
)

# --- VUELOS ---
vuelos = [
    ("Ciudad de México", "Cancún",        "2025-07-15", "Aeroméxico",       2500.00),
    ("Guadalajara",      "Madrid",         "2025-08-01", "Iberia",          12000.00),
    ("Monterrey",        "Miami",          "2025-09-10", "American Airlines", 8500.00),
    ("Ciudad de México", "Buenos Aires",   "2025-07-20", "Aeroméxico",      15000.00),
    ("Guadalajara",      "Nueva York",     "2025-08-15", "United Airlines", 11000.00),
    ("Ciudad de México", "París",          "2025-09-01", "Air France",      18000.00),
    ("Monterrey",        "Los Ángeles",    "2025-07-30", "Volaris",          7500.00),
    ("Ciudad de México", "Tokio",          "2025-10-05", "Japan Airlines",  25000.00),
    ("Guadalajara",      "Cancún",         "2025-08-20", "VivaAerobus",      1800.00),
    ("Ciudad de México", "Londres",        "2025-09-15", "British Airways", 19000.00),
    ("Monterrey",        "Barcelona",      "2025-10-01", "Iberia",          16000.00),
    ("Ciudad de México", "Roma",           "2025-08-25", "Alitalia",        17500.00),
    ("Guadalajara",      "São Paulo",      "2025-09-20", "LATAM",           13000.00),
    ("Ciudad de México", "Dubai",          "2025-11-01", "Emirates",        22000.00),
    ("Monterrey",        "Chicago",        "2025-07-25", "American Airlines", 9500.00),
    ("Ciudad de México", "Ámsterdam",      "2025-10-15", "KLM",             17000.00),
    ("Guadalajara",      "Toronto",        "2025-08-10", "Air Canada",      10500.00),
    ("Ciudad de México", "Sidney",         "2025-11-20", "Qantas",          28000.00),
    ("Monterrey",        "Ciudad de México","2025-07-10","Aeroméxico",        900.00),
    ("Ciudad de México", "Bogotá",         "2025-09-05", "Avianca",          8000.00),
]
cur.executemany(
    "INSERT INTO vuelos (origen, destino, fecha, aerolinea, precio) VALUES (%s, %s, %s, %s, %s)",
    vuelos
)

# --- HOSPEDAJES ---
hospedajes = [
    ("Hotel Sunset",           "Cancún",       "Hotel frente al mar con alberca infinita y todo incluido. Ideal para familias y parejas.", 1800.00),
    ("Hotel Arena",            "Cancún",       "Hotel económico cerca del aeropuerto con desayuno incluido y servicio de shuttle.", 950.00),
    ("Gran Hotel Madrid",      "Madrid",       "Hotel boutique en el centro histórico con spa, restaurante gourmet y vistas a la Gran Vía.", 3200.00),
    ("Miami Beach Resort",     "Miami",        "Resort de lujo en South Beach con acceso directo a la playa y club nocturno.", 4500.00),
    ("Palacio Buenos Aires",   "Buenos Aires", "Hotel histórico de 5 estrellas frente al Obelisco, decoración art decó y piscina en la azotea.", 5200.00),
    ("The Manhattan Plaza",    "Nueva York",   "Hotel moderno en Midtown Manhattan a dos cuadras del Central Park y el metro.", 6800.00),
    ("Le Marais Boutique",     "París",        "Pequeño hotel con encanto en el barrio Le Marais, desayuno francés incluido.", 4100.00),
    ("Shinjuku Grand Hotel",   "Tokio",        "Hotel de negocios en Shinjuku con habitaciones cápsula de lujo y onsen privado.", 3800.00),
    ("The London Suites",      "Londres",      "Suites de lujo en Mayfair con mayordomo personal y acceso a club exclusivo.", 7500.00),
    ("Hotel Arts Barcelona",   "Barcelona",    "Hotel icónico frente al mar Mediterráneo con piscina en la azotea y restaurante estrella Michelin.", 5800.00),
    ("Hotel de Russie",        "Roma",         "Hotel de lujo junto a la Plaza del Popolo con jardín secreto y spa de clase mundial.", 6200.00),
    ("Fasano São Paulo",       "São Paulo",    "Hotel diseñado por Isay Weinfeld en el exclusivo barrio Jardins con restaurante de autor.", 4700.00),
    ("Burj Al Arab Jumeirah",  "Dubai",        "El único hotel 7 estrellas del mundo con suite privada y mayordomo disponible 24 horas.", 35000.00),
    ("The Langham Chicago",    "Chicago",      "Hotel clásico a orillas del río Chicago con spa Chuan y bar de cócteles premium.", 5100.00),
    ("Conservatorium Amsterdam","Ámsterdam",   "Hotel de diseño en un conservatorio de música restaurado con piscina cubierta y cicloturos.", 4900.00),
    ("Ritz-Carlton Toronto",   "Toronto",      "Hotel de lujo en el centro financiero de Toronto con restaurante canadiense de temporada.", 5500.00),
    ("Park Hyatt Sydney",      "Sídney",       "Hotel con vistas espectaculares al Sydney Opera House y acceso privado al puerto.", 8200.00),
    ("Casa Medina Bogotá",     "Bogotá",       "Hotel boutique en Zona Rosa con arquitectura colonial y jardines tropicales.", 2800.00),
    ("Fiesta Americana",       "Guadalajara",  "Hotel referente de la ciudad con salones de eventos, spa y ubicación céntrica.", 2100.00),
    ("Camino Real Monterrey",  "Monterrey",    "Hotel clásico con amplio jardín, alberca olímpica y acceso al centro comercial.", 1950.00),
]
cur.executemany(
    "INSERT INTO hospedajes (nombre, ciudad, descripcion, precio_noche) VALUES (%s, %s, %s, %s)",
    hospedajes
)

# --- RESERVACIONES ---
reservaciones = [
    (1,  1,  1,  "2025-06-01"),
    (2,  2,  3,  "2025-06-15"),
    (3,  3,  4,  "2025-07-20"),
    (4,  4,  5,  "2025-06-10"),
    (5,  5,  6,  "2025-07-01"),
    (6,  6,  7,  "2025-06-20"),
    (7,  7,  8,  "2025-07-05"),
    (8,  8,  9,  "2025-06-25"),
    (9,  9,  10, "2025-07-10"),
    (10, 10, 11, "2025-06-30"),
    (11, 11, 12, "2025-07-15"),
    (12, 12, 13, "2025-08-01"),
    (13, 13, 14, "2025-07-25"),
    (14, 14, 15, "2025-08-10"),
    (15, 15, 16, "2025-07-30"),
]
cur.executemany(
    "INSERT INTO reservaciones (cliente_id, vuelo_id, hospedaje_id, fecha_reserva) VALUES (%s, %s, %s, %s)",
    reservaciones
)

conn.commit()

# --- EMBEDDINGS ---
textos_docs = [(h[0], h[1], h[2]) for h in hospedajes]
textos = [f"{nombre} en {ciudad}: {desc}" for nombre, ciudad, desc in textos_docs]

respuesta = co.embed(
    texts=textos,
    model="embed-multilingual-v3.0",
    input_type="search_document",
    embedding_types=["float"],
    output_dimension=1024
)

for i, vector in enumerate(respuesta.embeddings.float):
    cur.execute(
        "INSERT INTO documentos (contenido, embedding, metadata) VALUES (%s, %s::vector, %s)",
        (textos[i], str(vector), f'{{"tipo": "hospedaje", "id": {i+1}}}')
    )

conn.commit()
cur.close()
conn.close()
print(f"Seed completo: {len(clientes)} clientes, {len(vuelos)} vuelos, {len(hospedajes)} hospedajes, {len(reservaciones)} reservaciones.")