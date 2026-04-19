from __future__ import annotations
import psycopg2
from psycopg2.extensions import connection


DB_CONFIG = {
    "host": "Tu nombre",
    "port": 5432,
    "dbname": "nombre_de_bases_de_datos",
    "user": "postgres",
    "password": "ALAN I SEE YOU"
}


def get_connection() -> connection:
    return psycopg2.connect(**DB_CONFIG)


def test_connection() -> tuple[bool, str]:
    try:
        conn = get_connection()
        conn.close()
        return True, "Conexión exitosa con PostgreSQL."
    except Exception as e:
        return False, f"No fue posible conectar con PostgreSQL:\n{e}"
