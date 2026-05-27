CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    pasaporte VARCHAR(20)
);

CREATE TABLE tarjetas_credito (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    numero VARCHAR(16),
    cvv VARCHAR(4),
    fecha_expiracion VARCHAR(7)
);

CREATE TABLE vuelos (
    id SERIAL PRIMARY KEY,
    origen VARCHAR(100),
    destino VARCHAR(100),
    fecha DATE,
    aerolinea VARCHAR(100),
    precio DECIMAL
);

CREATE TABLE hospedajes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(100),
    descripcion TEXT,
    precio_noche DECIMAL
);

CREATE TABLE reservaciones (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    vuelo_id INT REFERENCES vuelos(id),
    hospedaje_id INT REFERENCES hospedajes(id),
    fecha_reserva DATE
);

-- Tabla vectorial: documentos con embeddings
CREATE TABLE documentos (
    id SERIAL PRIMARY KEY,
    contenido TEXT,
    embedding vector(1024),
    metadata JSONB
);