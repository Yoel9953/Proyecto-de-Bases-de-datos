from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFrame, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView
)

from scr.data_base import queries


class CategoriasView(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_id = None
        self.all_data = []
        self.build_ui()
        self.load_data()

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(20, 20, 20, 20)
        root.setSpacing(18)

        title = QLabel("Categorías")
        title.setObjectName("moduleHeaderTitle")

        subtitle = QLabel("Administra las categorías de los videojuegos")
        subtitle.setObjectName("moduleHeaderSubtitle")

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar categoría...")
        self.search_input.setObjectName("moduleSearch")
        self.search_input.textChanged.connect(self.filter_data)

        form_card = QFrame()
        form_card.setObjectName("moduleCard")
        form_layout = QVBoxLayout(form_card)
        form_layout.setSpacing(12)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre de categoría")

        self.descripcion_input = QLineEdit()
        self.descripcion_input.setPlaceholderText("Descripción")

        form_layout.addWidget(self.nombre_input)
        form_layout.addWidget(self.descripcion_input)

        actions = QHBoxLayout()

        btn_add = QPushButton("Agregar")
        btn_add.setObjectName("primary")
        btn_add.clicked.connect(self.add_record)

        btn_update = QPushButton("Actualizar")
        btn_update.clicked.connect(self.update_record)

        btn_delete = QPushButton("Eliminar")
        btn_delete.setObjectName("danger")
        btn_delete.clicked.connect(self.delete_record)

        btn_clear = QPushButton("Limpiar")
        btn_clear.clicked.connect(self.clear_form)

        actions.addWidget(btn_add)
        actions.addWidget(btn_update)
        actions.addWidget(btn_delete)
        actions.addWidget(btn_clear)

        table_card = QFrame()
        table_card.setObjectName("moduleCard")
        table_layout = QVBoxLayout(table_card)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Descripción"])
        self.table.cellClicked.connect(self.load_selected_row)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        table_layout.addWidget(self.table)

        root.addWidget(title)
        root.addWidget(subtitle)
        root.addWidget(self.search_input)
        root.addWidget(form_card)
        root.addLayout(actions)
        root.addWidget(table_card)

    def load_data(self):
        self.all_data = queries.get_categorias()
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

    def load_selected_row(self, row, column):
        self.selected_id = int(self.table.item(row, 0).text())
        self.nombre_input.setText(self.table.item(row, 1).text())
        self.descripcion_input.setText(self.table.item(row, 2).text())

    def add_record(self):
        try:
            queries.add_categoria(
                self.nombre_input.text(),
                self.descripcion_input.text()
            )
            QMessageBox.information(self, "Éxito", "Categoría agregada correctamente.")
            self.clear_form()
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_record(self):
        if self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Selecciona una categoría.")
            return
        try:
            queries.update_categoria(
                self.selected_id,
                self.nombre_input.text(),
                self.descripcion_input.text()
            )
            QMessageBox.information(self, "Éxito", "Categoría actualizada correctamente.")
            self.clear_form()
            self.load_data()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def delete_record(self):
        if self.selected_id is None:
            QMessageBox.warning(self, "Aviso", "Selecciona una categoría.")
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            "¿Seguro que deseas eliminar esta categoría?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            try:
                queries.delete_categoria(self.selected_id)
                QMessageBox.information(self, "Éxito", "Categoría eliminada correctamente.")
                self.clear_form()
                self.load_data()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def clear_form(self):
        self.selected_id = None
        self.nombre_input.clear()
        self.descripcion_input.clear()