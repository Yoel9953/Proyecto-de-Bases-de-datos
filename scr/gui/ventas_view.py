from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QFrame, QTableWidget, QTableWidgetItem, QHeaderView
)

from scr.data_base import queries


class VentasView(QWidget):
    def __init__(self):
        super().__init__()
        self.all_data = []
        self.build_ui()
        self.load_data()

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(20, 20, 20, 20)
        root.setSpacing(18)

        title = QLabel("Ventas")
        title.setObjectName("moduleHeaderTitle")

        subtitle = QLabel("Consulta el historial de ventas registradas")
        subtitle.setObjectName("moduleHeaderSubtitle")

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar por cliente, empleado, fecha o método de pago...")
        self.search_input.setObjectName("moduleSearch")
        self.search_input.textChanged.connect(self.filter_data)

        table_card = QFrame()
        table_card.setObjectName("moduleCard")
        table_layout = QVBoxLayout(table_card)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Cliente", "Empleado", "Fecha", "Total", "Método de pago"
        ])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        table_layout.addWidget(self.table)

        root.addWidget(title)
        root.addWidget(subtitle)
        root.addWidget(self.search_input)
        root.addWidget(table_card)

    def load_data(self):
        self.all_data = queries.get_ventas_join()
        self.render_table(self.all_data)

    def render_table(self, data):
        self.table.setRowCount(len(data))
        for row, record in enumerate(data):
            for col, value in enumerate(record):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def filter_data(self):
        text = self.search_input.text().strip().lower()
        if not text:
            self.render_table(self.all_data)
            return
        filtered = [row for row in self.all_data if text in " ".join(map(str, row)).lower()]
        self.render_table(filtered)