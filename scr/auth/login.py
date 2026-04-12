import os
import re

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import (
    QDialog, QLabel, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QWidget, QFrame,
    QStackedWidget, QMessageBox,
    QGraphicsDropShadowEffect
)

from scr.data_base import queries


def is_valid_email(email):
    return re.fullmatch(r"^[^@]+@[^@]+\.[^@]+$", email)


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setObjectName("loginRoot")
        self.setWindowTitle("Login - Tienda de Videojuegos")

        self.setWindowFlags(
            Qt.WindowType.Window |
            Qt.WindowType.WindowMinimizeButtonHint |
            Qt.WindowType.WindowMaximizeButtonHint |
            Qt.WindowType.WindowCloseButtonHint
        )

        # 🔥 tamaño correcto
        self.setMinimumSize(1400, 850)
        self.resize(1600, 900)

        self.setup_ui()
        self.load_image()

    def setup_ui(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(30, 30, 30, 30)
        root.setSpacing(20)

        # ================= LEFT =================
        self.left = QFrame()
        self.left.setObjectName("leftLoginPanel")

        left_layout = QVBoxLayout(self.left)
        left_layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Tienda de Videojuegos")
        title.setObjectName("overlayTitle")

        self.image = QLabel()
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        left_layout.addWidget(title)
        left_layout.addStretch()
        left_layout.addWidget(self.image)
        left_layout.addStretch()

        # ================= RIGHT =================
        self.right = QFrame()
        self.right.setObjectName("rightLoginPanel")

        right_layout = QVBoxLayout(self.right)
        right_layout.setContentsMargins(50, 40, 50, 40)

        header = QLabel("Bienvenido")
        header.setObjectName("bigTitle")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        sub = QLabel("Accede o crea una cuenta")
        sub.setObjectName("subTitle")
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ================= CARD =================
        self.card = QFrame()
        self.card.setObjectName("formCard")
        self.card.setMinimumWidth(420)
        self.card.setMaximumWidth(520)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(70)
        shadow.setOffset(0, 20)
        shadow.setColor(QColor(0, 0, 0, 180))
        self.card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(30, 30, 30, 30)
        card_layout.setSpacing(20)

        self.stack = QStackedWidget()

        # ================= LOGIN =================
        login_page = QWidget()
        l = QVBoxLayout(login_page)
        l.setSpacing(15)

        title_login = QLabel("Iniciar sesión")
        title_login.setObjectName("sectionTitle")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Correo electrónico")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        btn_login = QPushButton("Entrar")
        btn_login.setObjectName("primaryButton")
        btn_login.clicked.connect(self.login)

        btn_reg = QPushButton("Crear cuenta")
        btn_reg.setObjectName("secondaryButton")
        btn_reg.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        l.addWidget(title_login)
        l.addWidget(self.email)
        l.addWidget(self.password)
        l.addSpacing(10)
        l.addWidget(btn_login)
        l.addWidget(btn_reg)

        # ================= REGISTER =================
        register_page = QWidget()
        r = QVBoxLayout(register_page)
        r.setSpacing(15)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Nombre")

        self.reg_email = QLineEdit()
        self.reg_email.setPlaceholderText("Correo")

        self.reg_pass = QLineEdit()
        self.reg_pass.setPlaceholderText("Contraseña")
        self.reg_pass.setEchoMode(QLineEdit.EchoMode.Password)

        btn_create = QPushButton("Registrarse")
        btn_create.setObjectName("primaryButton")
        btn_create.clicked.connect(self.register)

        btn_back = QPushButton("Volver")
        btn_back.setObjectName("secondaryButton")
        btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        r.addWidget(self.name)
        r.addWidget(self.reg_email)
        r.addWidget(self.reg_pass)
        r.addWidget(btn_create)
        r.addWidget(btn_back)

        self.stack.addWidget(login_page)
        self.stack.addWidget(register_page)

        card_layout.addWidget(self.stack)

        # 🔥 CENTRADO PERFECTO
        right_layout.addStretch()
        right_layout.addWidget(header, alignment=Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(sub, alignment=Qt.AlignmentFlag.AlignCenter)
        right_layout.addSpacing(20)
        right_layout.addWidget(self.card, alignment=Qt.AlignmentFlag.AlignCenter)
        right_layout.addStretch()

        # ROOT
        root.addStretch(1)
        root.addWidget(self.left, 5)
        root.addWidget(self.right, 5)
        root.addStretch(1)

    def load_image(self):
        path = os.path.join("scr", "gui", "imagenes", "portada.PNG")

        pix = QPixmap(path)

        if not pix.isNull():
            self.image.setPixmap(
                pix.scaled(
                    520, 520,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )
        else:
            self.image.setText("No se encontró la imagen")

    def login(self):
        user = queries.login_usuario(self.email.text(), self.password.text())

        if user:
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas")

    def register(self):
        if not is_valid_email(self.reg_email.text()):
            QMessageBox.warning(self, "Error", "Correo inválido")
            return

        queries.create_usuario(
            self.name.text(),
            self.reg_email.text(),
            self.reg_pass.text()
        )

        QMessageBox.information(self, "OK", "Cuenta creada")
        self.stack.setCurrentIndex(0)