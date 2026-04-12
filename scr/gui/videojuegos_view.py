from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox
)

from scr.data_base import queries


class VideojuegosView(QWidget):
    def __init__(self) -> None:
        super().__init__()

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        buttons_layout = QHBoxLayout()

        self.titulo_input = QLineEdit()
        self.desarrolladora_input = QLineEdit()
        self.plataforma_input = QLineEdit()
        self.fecha_input = QLineEdit()
        self.fecha_input.setPlaceholderText("YYYY-MM-DD")
        self.precio_input = QLineEdit()
        self.stock_input = QLineEdit()
        self.clasificacion_input = QLineEdit()

        form_layout.addRow("Título:", self.titulo_input)
        form_layout.addRow("Desarrolladora:", self.desarrolladora_input)
        form_layout.addRow("Plataforma:", self.plataforma_input)
        form_layout.addRow("Fecha lanzamiento:", self.fecha_input)
        form_layout.addRow("Precio:", self.precio_input)
        form_layout.addRow("Stock:", self.stock_input)
        form_layout.addRow("Clasificación:", self.clasificacion_input)

        self.add_button = QPushButton("Agregar")
        self.update_button = QPushButton("Actualizar")
        self.delete_button = QPushButton("Eliminar")
        self.clear_button = QPushButton("Limpiar")

        self.add_button.clicked.connect(self.add_videojuego)
        self.update_button.clicked.connect(self.update_videojuego)
        self.delete_button.clicked.connect(self.delete_videojuego)
        self.clear_button.clicked.connect(self.clear_form)

        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.update_button)
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.clear_button)

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID", "Título", "Desarrolladora", "Plataforma",
            "Fecha lanzamiento", "Precio", "Stock", "Clasificación"
        ])
        self.table.cellClicked.connect(self.load_selected_row)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

        self.selected_id: int | None = None
        self.load_data()

    def load_data(self) -> None:
        data = queries.get_videojuegos()
        self.table.setRowCount(len(data))

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        self.table.resizeColumnsToContents()

    def load_selected_row(self, row: int, column: int) -> None:
        self.selected_id = int(self.table.item(row, 0).text())
        self.titulo_input.setText(self.table.item(row, 1).text())
        self.desarrolladora_input.setText(self.table.item(row, 2).text())
        self.plataforma_input.setText(self.table.item(row, 3).text())
        self.fecha_input.setText(self.table.item(row, 4).text())
        self.precio_input.setText(self.table.item(row, 5).text())
        self.stock_input.setText(self.table.item(row, 6).text())
        self.clasificacion_input.setText(self.table.item(row, 7).text())

    def add_videojuego(self) -> None:
        try:
            queries.add_videojuego(
                self.titulo_input.text().strip(),
                self.desarrolladora_input.text().strip(),
                self.plataforma_input.text().strip(),
                self.fecha_input.text().strip(),
                float(self.precio_input.text().strip()),
                int(self.stock_input.text().strip()),
                self.clasificacion_input.text().strip(),
            )
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Videojuego agregado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_videojuego(self) -> None:
        if self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Selecciona un videojuego.")
            return

        try:
            queries.update_videojuego(
                self.selected_id,
                self.titulo_input.text().strip(),
                self.desarrolladora_input.text().strip(),
                self.plataforma_input.text().strip(),
                self.fecha_input.text().strip(),
                float(self.precio_input.text().strip()),
                int(self.stock_input.text().strip()),
                self.clasificacion_input.text().strip(),
            )
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Videojuego actualizado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def delete_videojuego(self) -> None:
        if self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Selecciona un videojuego.")
            return

        try:
            queries.delete_videojuego(self.selected_id)
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Videojuego eliminado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_form(self) -> None:
        self.selected_id = None
        self.titulo_input.clear()
        self.desarrolladora_input.clear()
        self.plataforma_input.clear()
        self.fecha_input.clear()
        self.precio_input.clear()
        self.stock_input.clear()
        self.clasificacion_input.clear()