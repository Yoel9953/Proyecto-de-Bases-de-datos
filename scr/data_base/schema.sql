CREATE TABLE IF NOT EXISTS cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    fecha_registro DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS empleado (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    puesto VARCHAR(50) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    fecha_contratacion DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS videojuego (
    id_videojuego SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    desarrolladora VARCHAR(100) NOT NULL,
    plataforma VARCHAR(50) NOT NULL,
    fecha_lanzamiento DATE,
    precio NUMERIC(10,2) NOT NULL CHECK (precio >= 0),
    stock INT NOT NULL CHECK (stock >= 0),
    clasificacion VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS categoria (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS videojuego_categoria (
    id_videojuego INT NOT NULL,
    id_categoria INT NOT NULL,
    PRIMARY KEY (id_videojuego, id_categoria),
    FOREIGN KEY (id_videojuego) REFERENCES videojuego(id_videojuego) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS venta (
    id_venta SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_empleado INT NOT NULL,
    fecha_venta DATE NOT NULL DEFAULT CURRENT_DATE,
    total NUMERIC(10,2) NOT NULL CHECK (total >= 0),
    metodo_pago VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE IF NOT EXISTS detalle_venta (
    id_detalle SERIAL PRIMARY KEY,
    id_venta INT NOT NULL,
    id_videojuego INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario NUMERIC(10,2) NOT NULL CHECK (precio_unitario >= 0),
    subtotal NUMERIC(10,2) NOT NULL CHECK (subtotal >= 0),
    FOREIGN KEY (id_venta) REFERENCES venta(id_venta) ON DELETE CASCADE,
    FOREIGN KEY (id_videojuego) REFERENCES videojuego(id_videojuego)
);

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    correo VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(120) NOT NULL,
    fecha_registro DATE NOT NULL DEFAULT CURRENT_DATE,
    CHECK (char_length(nombre) >= 3),
    CHECK (char_length(password) >= 4)
);