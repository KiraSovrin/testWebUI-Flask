
import sys
from PySide6.QtWidgets import QApplication
from app import MainWindow

def main():
    app = QApplication(sys.argv)


    window = MainWindow()
    availableGeometry = window.screen().availableGeometry()
    window.resize(
        availableGeometry.width() * 2 / 3, availableGeometry.height() * 2 / 3
    )
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
