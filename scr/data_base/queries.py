from __future__ import annotations
from typing import Any
from scr.data_base.connection import get_connection


def execute_query(
    query: str,
    params: tuple | None = None,
    fetch: bool = False
) -> list[tuple[Any, ...]] | None:
    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            if params is not None:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if fetch:
                result = cursor.fetchall()
            else:
                result = None

        conn.commit()
        return result
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


# =========================
# CLIENTES
# =========================

def get_clientes() -> list[tuple]:
    query = """
        SELECT id_cliente, nombre, apellido, correo, telefono, fecha_registro
        FROM cliente
        ORDER BY id_cliente;
    """
    return execute_query(query, fetch=True) or []


def add_cliente(nombre: str, apellido: str, correo: str, telefono: str) -> None:
    query = """
        INSERT INTO cliente (nombre, apellido, correo, telefono)
        VALUES (%s, %s, %s, %s);
    """
    execute_query(query, (nombre, apellido, correo, telefono))


def update_cliente(cliente_id: int, nombre: str, apellido: str, correo: str, telefono: str) -> None:
    query = """
        UPDATE cliente
        SET nombre = %s,
            apellido = %s,
            correo = %s,
            telefono = %s
        WHERE id_cliente = %s;
    """
    execute_query(query, (nombre, apellido, correo, telefono, cliente_id))


def delete_cliente(cliente_id: int) -> None:
    query = """
        DELETE FROM cliente
        WHERE id_cliente = %s;
    """
    execute_query(query, (cliente_id,))


# =========================
# EMPLEADOS
# =========================

def get_empleados() -> list[tuple]:
    query = """
        SELECT id_empleado, nombre, apellido, puesto, correo, fecha_contratacion
        FROM empleado
        ORDER BY id_empleado;
    """
    return execute_query(query, fetch=True) or []


def add_empleado(nombre: str, apellido: str, puesto: str, correo: str, fecha_contratacion: str) -> None:
    query = """
        INSERT INTO empleado (nombre, apellido, puesto, correo, fecha_contratacion)
        VALUES (%s, %s, %s, %s, %s);
    """
    execute_query(query, (nombre, apellido, puesto, correo, fecha_contratacion))


def update_empleado(
    empleado_id: int,
    nombre: str,
    apellido: str,
    puesto: str,
    correo: str,
    fecha_contratacion: str
) -> None:
    query = """
        UPDATE empleado
        SET nombre = %s,
            apellido = %s,
            puesto = %s,
            correo = %s,
            fecha_contratacion = %s
        WHERE id_empleado = %s;
    """
    execute_query(query, (nombre, apellido, puesto, correo, fecha_contratacion, empleado_id))


def delete_empleado(empleado_id: int) -> None:
    query = """
        DELETE FROM empleado
        WHERE id_empleado = %s;
    """
    execute_query(query, (empleado_id,))


# =========================
# VIDEOJUEGOS
# =========================

def get_videojuegos() -> list[tuple]:
    query = """
        SELECT id_videojuego, titulo, desarrolladora, plataforma, fecha_lanzamiento, precio, stock, clasificacion
        FROM videojuego
        ORDER BY id_videojuego;
    """
    return execute_query(query, fetch=True) or []


def add_videojuego(
    titulo: str,
    desarrolladora: str,
    plataforma: str,
    fecha_lanzamiento: str,
    precio: float,
    stock: int,
    clasificacion: str
) -> None:
    query = """
        INSERT INTO videojuego (
            titulo, desarrolladora, plataforma, fecha_lanzamiento, precio, stock, clasificacion
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    execute_query(
        query,
        (titulo, desarrolladora, plataforma, fecha_lanzamiento, precio, stock, clasificacion)
    )


def update_videojuego(
    videojuego_id: int,
    titulo: str,
    desarrolladora: str,
    plataforma: str,
    fecha_lanzamiento: str,
    precio: float,
    stock: int,
    clasificacion: str
) -> None:
    query = """
        UPDATE videojuego
        SET titulo = %s,
            desarrolladora = %s,
            plataforma = %s,
            fecha_lanzamiento = %s,
            precio = %s,
            stock = %s,
            clasificacion = %s
        WHERE id_videojuego = %s;
    """
    execute_query(
        query,
        (titulo, desarrolladora, plataforma, fecha_lanzamiento, precio, stock, clasificacion, videojuego_id)
    )


def delete_videojuego(videojuego_id: int) -> None:
    query = """
        DELETE FROM videojuego
        WHERE id_videojuego = %s;
    """
    execute_query(query, (videojuego_id,))


# =========================
# CATEGORIAS
# =========================

def get_categorias() -> list[tuple]:
    query = """
        SELECT id_categoria, nombre, descripcion
        FROM categoria
        ORDER BY id_categoria;
    """
    return execute_query(query, fetch=True) or []


def add_categoria(nombre: str, descripcion: str) -> None:
    query = """
        INSERT INTO categoria (nombre, descripcion)
        VALUES (%s, %s);
    """
    execute_query(query, (nombre, descripcion))


def update_categoria(categoria_id: int, nombre: str, descripcion: str) -> None:
    query = """
        UPDATE categoria
        SET nombre = %s,
            descripcion = %s
        WHERE id_categoria = %s;
    """
    execute_query(query, (nombre, descripcion, categoria_id))


def delete_categoria(categoria_id: int) -> None:
    query = """
        DELETE FROM categoria
        WHERE id_categoria = %s;
    """
    execute_query(query, (categoria_id,))


# =========================
# VENTAS / CONSULTA JOIN
# =========================

def get_ventas_join() -> list[tuple]:
    query = """
        SELECT
            v.id_venta,
            c.nombre || ' ' || c.apellido AS cliente,
            e.nombre || ' ' || e.apellido AS empleado,
            v.fecha_venta,
            v.total,
            v.metodo_pago
        FROM venta v
        JOIN cliente c ON v.id_cliente = c.id_cliente
        JOIN empleado e ON v.id_empleado = e.id_empleado
        ORDER BY v.id_venta;
    """
    return execute_query(query, fetch=True) or []


# =========================
# USUARIOS / LOGIN
# =========================

def create_usuario(nombre: str, correo: str, password: str) -> None:
    query = """
        INSERT INTO usuario (nombre, correo, password)
        VALUES (%s, %s, %s);
    """
    execute_query(query, (nombre, correo, password))


def login_usuario(correo: str, password: str) -> tuple | None:
    query = """
        SELECT id_usuario, nombre, correo
        FROM usuario
        WHERE correo = %s AND password = %s;
    """
    result = execute_query(query, (correo, password), fetch=True)
    return result[0] if result else None


def correo_existe(correo: str) -> bool:
    query = """
        SELECT 1
        FROM usuario
        WHERE correo = %s;
    """
    result = execute_query(query, (correo,), fetch=True)
    return bool(result)