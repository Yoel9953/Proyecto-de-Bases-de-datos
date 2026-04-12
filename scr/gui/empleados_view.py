from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox
)

from scr.data_base import queries


class EmpleadosView(QWidget):
    def __init__(self) -> None:
        super().__init__()

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        buttons_layout = QHBoxLayout()

        self.nombre_input = QLineEdit()
        self.apellido_input = QLineEdit()
        self.puesto_input = QLineEdit()
        self.correo_input = QLineEdit()
        self.fecha_input = QLineEdit()
        self.fecha_input.setPlaceholderText("YYYY-MM-DD")

        form_layout.addRow("Nombre:", self.nombre_input)
        form_layout.addRow("Apellido:", self.apellido_input)
        form_layout.addRow("Puesto:", self.puesto_input)
        form_layout.addRow("Correo:", self.correo_input)
        form_layout.addRow("Fecha contratación:", self.fecha_input)

        self.add_button = QPushButton("Agregar")
        self.update_button = QPushButton("Actualizar")
        self.delete_button = QPushButton("Eliminar")
        self.clear_button = QPushButton("Limpiar")

        self.add_button.clicked.connect(self.add_empleado)
        self.update_button.clicked.connect(self.update_empleado)
        self.delete_button.clicked.connect(self.delete_empleado)
        self.clear_button.clicked.connect(self.clear_form)

        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.update_button)
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.clear_button)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Nombre", "Apellido", "Puesto", "Correo", "Fecha contratación"
        ])
        self.table.cellClicked.connect(self.load_selected_row)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

        self.selected_id: int | None = None
        self.load_data()

    def load_data(self) -> None:
        data = queries.get_empleados()
        self.table.setRowCount(len(data))

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        self.table.resizeColumnsToContents()

    def load_selected_row(self, row: int, column: int) -> None:
        self.selected_id = int(self.table.item(row, 0).text())
        self.nombre_input.setText(self.table.item(row, 1).text())
        self.apellido_input.setText(self.table.item(row, 2).text())
        self.puesto_input.setText(self.table.item(row, 3).text())
        self.correo_input.setText(self.table.item(row, 4).text())
        self.fecha_input.setText(self.table.item(row, 5).text())

    def add_empleado(self) -> None:
        try:
            queries.add_empleado(
                self.nombre_input.text().strip(),
                self.apellido_input.text().strip(),
                self.puesto_input.text().strip(),
                self.correo_input.text().strip(),
                self.fecha_input.text().strip(),
            )
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Empleado agregado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_empleado(self) -> None:
        if self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Selecciona un empleado.")
            return

        try:
            queries.update_empleado(
                self.selected_id,
                self.nombre_input.text().strip(),
                self.apellido_input.text().strip(),
                self.puesto_input.text().strip(),
                self.correo_input.text().strip(),
                self.fecha_input.text().strip(),
            )
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Empleado actualizado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def delete_empleado(self) -> None:
        if self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Selecciona un empleado.")
            return

        try:
            queries.delete_empleado(self.selected_id)
            self.load_data()
            self.clear_form()
            QMessageBox.information(self, "Éxito", "Empleado eliminado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def clear_form(self) -> None:
        self.selected_id = None
        self.nombre_input.clear()
        self.apellido_input.clear()
        self.puesto_input.clear()
        self.correo_input.clear()
        self.fecha_input.clear()