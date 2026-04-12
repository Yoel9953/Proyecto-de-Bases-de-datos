from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget
)

from scr.gui.clientes_view import ClientesView
from scr.gui.empleados_view import EmpleadosView
from scr.gui.videojuegos_view import VideojuegosView
from scr.gui.categorias_view import CategoriasView
from scr.gui.ventas_view import VentasView


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Tienda de Videojuegos")
        self.resize(1100, 650)

        central = QWidget()
        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tabs.addTab(ClientesView(), "Clientes")
        self.tabs.addTab(EmpleadosView(), "Empleados")
        self.tabs.addTab(VideojuegosView(), "Videojuegos")
        self.tabs.addTab(CategoriasView(), "Categorías")
        self.tabs.addTab(VentasView(), "Ventas")

        layout.addWidget(self.tabs)
        central.setLayout(layout)
        self.setCentralWidget(central)