from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox
)

from scr.data_base import queries


class CategoriasView(QWidget):
    def __init__(self) -> None:
        super().__init__()

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        buttons_layout = QHBoxLayout()

        self.nombre_input = QLineEdit()
        self.descripcion_input = QLineEdit()

        form_layout.addRow("Nombre:", self.nombre_input)
        form_layout.addRow("Descripción:", self.descripcion_input)

        self.add_button = QPushButton("Agregar")
        self.update_button = QPushButton("Actualizar")
        self.delete_button = QPushButton("Eliminar")
        self.clear_button = QPushButton("Limpiar")

        self.add_button.clicked.connect(self.add_categoria)
        self.update_button.clicked.connect(self.update_categoria)
        self.delete_button.clicked.connect(self.delete_categoria)
        self.clear_button.clicked.connect(self.clear_form)

        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.update_button)
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.clear_button)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Descripción"])
        self.table.cellClicked.connect(self.load_selected_row)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

        self.selected_id: int | None = None
        self.load_data()

    def load_data(self) -> None:
        data = queries.get_categorias()
        self.table.setRowCount(len(data))

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        self.table.resizeColumnsToContents()

    def load_selected_row(self, row: int, column: int) -> None:
        self.selected_id = int(self.table.item(row, 0).text())
        self.nombre_input.setText(self.table.item(row, 1).text())
        self.descripcion_input.setText(self.table.item(row, 2).text())

    def add_categoria(self) -> None:
        try:
            queries.add_categoria(
                self.nombre_input.text().strip(),
                self.descripcion_input.text().strip(),
            )
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Categoría agregada correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_categoria(self) -> None:
        if self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Selecciona una categoría.")
            return

        try:
            queries.update_categoria(
                self.selected_id,
                self.nombre_input.text().strip(),
                self.descripcion_input.text().strip(),
            )
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Categoría actualizada correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def delete_categoria(self) -> None:
        if self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Selecciona una categoría.")
            return

        try:
            queries.delete_categoria(self.selected_id)
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Categoría eliminada correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_form(self) -> None:
        self.selected_id = None
        self.nombre_input.clear()
        self.descripcion_input.clear()