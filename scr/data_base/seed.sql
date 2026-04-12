INSERT INTO cliente (nombre, apellido, correo, telefono) VALUES
('Joel', 'Flores', 'joel@gmail.com', '3311111111'),
('María', 'López', 'maria@gmail.com', '3322222222'),
('Carlos', 'Reyes', 'carlos@gmail.com', '3333333333');

INSERT INTO empleado (nombre, apellido, puesto, correo, fecha_contratacion) VALUES
('Ana', 'Torres', 'Cajera', 'ana@tienda.com', '2025-01-10'),
('Luis', 'Ramírez', 'Vendedor', 'luis@tienda.com', '2025-02-15');

INSERT INTO videojuego (titulo, desarrolladora, plataforma, fecha_lanzamiento, precio, stock, clasificacion) VALUES
('Super Mario Bros', 'Nintendo', 'NES', '1985-09-13', 599.00, 10, 'E'),
('The Legend of Zelda', 'Nintendo', 'NES', '1986-02-21', 699.00, 8, 'E10+'),
('Metroid', 'Nintendo', 'NES', '1986-08-06', 650.00, 7, 'E'),
('Donkey Kong Country', 'Rare', 'SNES', '1994-11-21', 750.00, 5, 'E');

INSERT INTO categoria (nombre, descripcion) VALUES
('Aventura', 'Juegos de aventura'),
('Plataformas', 'Juegos de plataformas'),
('Acción', 'Juegos de acción');

INSERT INTO videojuego_categoria (id_videojuego, id_categoria) VALUES
(1, 2),
(2, 1),
(3, 3),
(4, 2);

INSERT INTO venta (id_cliente, id_empleado, fecha_venta, total, metodo_pago) VALUES
(1, 1, CURRENT_DATE, 1298.00, 'Tarjeta'),
(2, 2, CURRENT_DATE, 750.00, 'Efectivo');

INSERT INTO detalle_venta (id_venta, id_videojuego, cantidad, precio_unitario, subtotal) VALUES
(1, 1, 1, 599.00, 599.00),
(1, 2, 1, 699.00, 699.00),
(2, 4, 1, 750.00, 750.00);