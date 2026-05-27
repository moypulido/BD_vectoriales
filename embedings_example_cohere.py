import cohere
from dotenv import load_dotenv
import os

load_dotenv()
co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))

textos = ["Me encanta la sopa", "El clima está agradable hoy"]

# Realiza la petición
respuesta = co.embed(
    texts=textos,
    model="embed-multilingual-v3.0", # Usa un modelo multilingüe si procesas español
    input_type="search_document",
    embedding_types=["float"],
    output_dimension=1024 # Opcional
)

# Accede a los vectores (embeddings)
vectores = respuesta.embeddings.float
print(vectores[0]) # Imprime el embedding del primer texto