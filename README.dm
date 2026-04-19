# Tienda de Videojuegos

Aplicación de escritorio desarrollada en Python para la gestión integral de una tienda de videojuegos. El sistema permite administrar clientes, empleados, inventario de productos, categorías y ventas, además de incluir funcionalidades de respaldo de información.

---

## Características principales

* Sistema de autenticación para el acceso al sistema.
* Gestión de clientes (alta, baja, modificación y consulta).
* Administración de empleados.
* Control de inventario de videojuegos.
* Gestión de categorías para clasificación de productos.
* Registro y seguimiento de ventas.
* Generación de respaldos de la base de datos.

---

## Arquitectura del proyecto

El proyecto está estructurado de manera modular para facilitar su mantenimiento y escalabilidad:

Tienda de videojuegos/
│
├── main.py
├── README.dm
├── requirements.txt
│
├── scr/
│   ├── __init__.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── login.py
│   │
│   ├── data_base/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   ├── init_db.py
│   │   ├── queries.py
│   │   ├── schema.sql
│   │   └── seed.sql
│   │
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── clientes_view.py
│   │   ├── empleados_view.py
│   │   ├── videojuegos_view.py
│   │   ├── categorias_view.py
│   │   ├── ventas_view.py
│   │   ├── login.qss
│   │   ├── app.qss
│   │   └── imagenes/
│   │       └── portada.PNG
│   │
│   ├── reports/
│   │   ├── __init__.py
│   │   └── export_backup.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── test/
│
└── venv/
## Tecnologías utilizadas

* Python 3
* SQLite
* PyQt / PySide
* SQL

---

## Interfaz de usuario

La interfaz gráfica fue desarrollada utilizando Qt y hojas de estilo (`.qss`), permitiendo una experiencia visual clara y organizada.

---

## Instalación y ejecución

1. Clonar el repositorio:

```
git clone https://github.com/tu-usuario/tu-repo.git
cd tienda-videojuegos
```

2. Crear entorno virtual:

```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. Instalar dependencias:

```
pip install -r requirements.txt
```

4. Inicializar la base de datos:

```
python src/data_base/init_db.py
```

5. Ejecutar la aplicación:

```
python main.py
```

---

## Estructura del proyecto

* `main.py`: Punto de entrada de la aplicación
* `auth/`: Lógica de autenticación
* `data_base/`: Conexión y manejo de base de datos
* `gui/`: Componentes de la interfaz gráfica
* `reports/`: Funciones de exportación
* `utils/`: Funciones auxiliares
* `test/`: Pruebas del sistema

---

## Objetivo del proyecto

Este proyecto fue desarrollado con fines educativos, aplicando conceptos de programación en Python, diseño de interfaces gráficas, manejo de bases de datos y organización modular del software.

