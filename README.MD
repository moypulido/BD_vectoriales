# Vector Database Vulnerability Demo
### Prompt Injection Attack on a RAG System — Secure Software Development

A practical demonstration of **prompt injection vulnerabilities** in vector databases using a travel management system built with PostgreSQL + pgvector, FastAPI, Cohere embeddings, and a local LLM.

---

## What This Demonstrates

This project shows how malicious data embedded in a vector database can manipulate an LLM's responses in a RAG (Retrieval-Augmented Generation) pipeline — and how to mitigate it.

**The Attack:** A poisoned document is stored in pgvector alongside legitimate hotel data. When a user queries the system, the poisoned document is retrieved by similarity search and injected into the LLM prompt, causing it to leak sensitive financial data (credit card numbers, CVV, expiration dates).

**The Mitigation:** Input validation, context sanitization with pattern matching, and a hardened system prompt prevent the attack from succeeding.

---

## Tech Stack

- **Database:** PostgreSQL 16 + pgvector (Docker)
- **Embeddings:** Cohere `embed-multilingual-v3.0` (1024 dimensions)
- **LLM:** Cohere `command-r7b-12-2024`
- **API:** FastAPI + Uvicorn
- **Language:** Python 3.14

---

## Project Structure

```
BD_vectoriales/
├── docker-compose.yml       # PostgreSQL + pgvector container
├── init.sql                 # Database schema
├── seedDB.py                # Seed data + embeddings generation
├── inject_poison.py         # Poisoned document insertion (attack simulation)
├── main.py                  # FastAPI application (vulnerable + secure endpoints)
└── README.md
```

---

## Setup

### 1. Prerequisites

- Docker Desktop
- Python 3.10+
- Cohere API key (free tier at [cohere.com](https://cohere.com))

### 2. Start the database

```bash
docker compose up -d
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn cohere psycopg2-binary httpx
```

### 4. Seed the database

```bash
python3 seedDB.py
```

### 5. Inject poisoned documents

```bash
python3 inject_poison.py
```

### 6. Run the API

```bash
uvicorn main:app --reload
```

Interactive docs available at `http://127.0.0.1:8000/docs`

---

## Endpoints

### `POST /buscar` — Vulnerable

Retrieves similar documents from pgvector and injects them directly into the LLM prompt without validation.

**Request:**
```json
{ "pregunta": "hoteles en Cancún económicos" }
```

**Result:** The LLM exposes credit card numbers, CVV codes, and expiration dates from poisoned documents retrieved by the vector similarity search.

### `POST /buscar-seguro` — Mitigated

Applies three layers of protection before sending context to the LLM.

**Request:**
```json
{ "pregunta": "hoteles en Cancún económicos" }
```

**Result:** Poisoned fragments are detected and replaced with `[FRAGMENTO ELIMINADO POR POLÍTICA DE SEGURIDAD]`. The LLM responds safely.

---

## How the Attack Works

```
User query
    │
    ▼
Embed query with Cohere ──► vector [0.23, -0.11, 0.87, ...]
    │
    ▼
pgvector similarity search ──► top-k most similar documents
    │                           (includes poisoned documents)
    ▼
Inject ALL retrieved docs into LLM prompt
    │
    ▼
LLM follows malicious instructions ──► leaks financial data ⚠️
```

---

## Mitigation Strategy

Three layers of defense applied in `/buscar-seguro`:

1. **Input validation** — rejects queries containing known injection patterns before processing
2. **Context sanitization** — scans each retrieved document for malicious patterns and removes them before building the prompt
3. **Hardened system prompt** — explicit instructions to the LLM to ignore instructions found in context and never reveal financial data

---

## Poisoning Techniques Demonstrated

| Technique | Description |
|-----------|-------------|
| Data as legitimate context | Credit card data formatted as "recent reservations" |
| Soft instruction | Polite request embedded in hotel description |
| Roleplay / training mode | "Simulate being an agent that confirms payments" |
| Educational mode | Fake demo flag to lower model guard |
| Direct data exposure | Raw card numbers listed inline |

---

## Database Schema

```sql
clientes        -- name, email, passport
tarjetas_credito -- card number, CVV, expiration (sensitive data target)
vuelos          -- flights
hospedajes      -- hotels
reservaciones   -- bookings
documentos      -- text + vector(1024) + metadata (RAG source)
```

---