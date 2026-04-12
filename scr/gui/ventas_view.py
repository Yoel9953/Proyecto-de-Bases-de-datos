from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)

from scr.data_base import queries


class VentasView(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()

        self.refresh_button = QPushButton("Actualizar consulta")
        self.refresh_button.clicked.connect(self.load_data)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID Venta", "Cliente", "Empleado", "Fecha", "Total", "Método de pago"
        ])

        layout.addWidget(self.refresh_button)
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.load_data()

    def load_data(self) -> None:
        try:
            data = queries.get_ventas_join()
            self.table.setRowCount(len(data))

            for row_idx, row_data in enumerate(data):
                for col_idx, value in enumerate(row_data):
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            self.table.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))