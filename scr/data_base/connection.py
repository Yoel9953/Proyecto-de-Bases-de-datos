from __future__ import annotations
import psycopg2
from psycopg2.extensions import connection


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "tienda_videojuegos",
    "user": "postgres",
    "password": "Joel213CAL@"
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