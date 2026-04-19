import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QStackedWidget, QFrame, QGridLayout, QMessageBox
)

from scr.gui.clientes_view import ClientesView
from scr.gui.empleados_view import EmpleadosView
from scr.gui.videojuegos_view import VideojuegosView
from scr.gui.categorias_view import CategoriasView
from scr.gui.ventas_view import VentasView


class DashboardCard(QPushButton):
    def __init__(self, title: str, image_path: str, subtitle: str = ""):
        super().__init__()
        self.setObjectName("dashboardCard")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(230)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setObjectName("dashboardCardImage")

        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            image_label.setPixmap(
                pixmap.scaled(
                    120, 120,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )
        else:
            image_label.setText("Sin imagen")

        title_label = QLabel(title)
        title_label.setObjectName("dashboardCardTitle")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle_label = QLabel(subtitle)
        subtitle_label.setObjectName("dashboardCardSubtitle")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setWordWrap(True)

        layout.addWidget(image_label)
        layout.addWidget(title_label)
        if subtitle:
            layout.addWidget(subtitle_label)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tienda de Videojuegos")
        self.resize(1450, 900)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.dashboard_page = self.build_dashboard_page()

        self.clientes_page = self.build_module_page("Clientes", ClientesView())
        self.empleados_page = self.build_module_page("Empleados", EmpleadosView())
        self.videojuegos_page = self.build_module_page("Videojuegos", VideojuegosView())
        self.categorias_page = self.build_module_page("Categorías", CategoriasView())
        self.ventas_page = self.build_module_page("Ventas", VentasView())

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.clientes_page)
        self.stack.addWidget(self.empleados_page)
        self.stack.addWidget(self.videojuegos_page)
        self.stack.addWidget(self.categorias_page)
        self.stack.addWidget(self.ventas_page)

        self.stack.setCurrentWidget(self.dashboard_page)

    def build_dashboard_page(self) -> QWidget:
        page = QWidget()
        page.setObjectName("dashboardPage")

        root = QVBoxLayout(page)
        root.setContentsMargins(30, 24, 30, 24)
        root.setSpacing(20)

        title = QLabel("Panel principal")
        title.setObjectName("dashboardMainTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Selecciona un módulo para administrar la tienda")
        subtitle.setObjectName("dashboardMainSubtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        grid_container = QFrame()
        grid_container.setObjectName("dashboardContainer")

        grid = QGridLayout(grid_container)
        grid.setContentsMargins(20, 20, 20, 20)
        grid.setHorizontalSpacing(18)
        grid.setVerticalSpacing(18)

        base = os.path.join("scr", "gui", "imagenes")

        card_clientes = DashboardCard("Clientes", os.path.join(base, "1.png"), "Administración de clientes")
        card_empleados = DashboardCard("Empleados", os.path.join(base, "2.png"), "Administración de empleados")
        card_videojuegos = DashboardCard("Videojuegos", os.path.join(base, "3.png"), "Catálogo de videojuegos")
        card_categorias = DashboardCard("Categorías", os.path.join(base, "4.png"), "Clasificación de juegos")
        card_ventas = DashboardCard("Ventas", os.path.join(base, "5.png"), "Registro de ventas")
        card_logout = QPushButton("CERRAR SESIÓN")
        card_logout.setObjectName("logoutCard")
        card_logout.clicked.connect(self.logout)

        card_clientes.clicked.connect(lambda: self.open_page(self.clientes_page))
        card_empleados.clicked.connect(lambda: self.open_page(self.empleados_page))
        card_videojuegos.clicked.connect(lambda: self.open_page(self.videojuegos_page))
        card_categorias.clicked.connect(lambda: self.open_page(self.categorias_page))
        card_ventas.clicked.connect(lambda: self.open_page(self.ventas_page))

        grid.addWidget(card_clientes, 0, 0)
        grid.addWidget(card_empleados, 0, 1)
        grid.addWidget(card_videojuegos, 0, 2)
        grid.addWidget(card_categorias, 1, 0)
        grid.addWidget(card_ventas, 1, 1)
        grid.addWidget(card_logout, 1, 2)

        root.addWidget(title)
        root.addWidget(subtitle)
        root.addWidget(grid_container)

        return page

    def build_module_page(self, module_name: str, module_view: QWidget) -> QWidget:
        page = QWidget()
        page.setObjectName("modulePage")

        root = QVBoxLayout(page)
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(12)

        top_bar = QHBoxLayout()

        back_button = QPushButton("← Volver al panel")
        back_button.setObjectName("primary")
        back_button.clicked.connect(self.go_dashboard)

        title = QLabel(module_name)
        title.setObjectName("moduleTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logout_button = QPushButton("Cerrar sesión")
        logout_button.setObjectName("danger")
        logout_button.clicked.connect(self.logout)

        top_bar.addWidget(back_button)
        top_bar.addStretch()
        top_bar.addWidget(logout_button)

        root.addLayout(top_bar)
        root.addWidget(module_view)

        return page

    def open_page(self, page: QWidget):
        self.stack.setCurrentWidget(page)

    def go_dashboard(self):
        self.stack.setCurrentWidget(self.dashboard_page)

    def logout(self):
        reply = QMessageBox.question(
            self,
            "Cerrar sesión",
            "¿Seguro que quieres cerrar sesión?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.close()