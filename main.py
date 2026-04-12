import sys
from PyQt6.QtWidgets import QApplication

from scr.auth.login import LoginWindow
from scr.gui.main_window import MainWindow


def load_style(app, path):

    app.setStyleSheet("")
    with open(path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())


def main():
    app = QApplication(sys.argv)

    while True:
        load_style(app, "scr/gui/login.qss")

        login = LoginWindow()

        if login.exec():
            
            load_style(app, "scr/gui/app.qss")

            window = MainWindow()
            window.show()
            app.exec()
        else:
            break


if __name__ == "__main__":
    main()