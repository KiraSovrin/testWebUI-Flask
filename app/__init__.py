# app/__init__.py
import os

from PySide6.QtCore import QUrl, Signal, Slot, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QIcon, QAction, QFont, QFontDatabase
from config import Config


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        config = Config()

        # Replace 'path/to/font.ttf' with the actual path to your font file
        font_id = QFontDatabase.addApplicationFont(os.path.join(
            config.BASE_DIR, 'app', 'static', 'fonts', config.DEFAULT_FONT
        ))
        if font_id != -1:
            # Use the actual font family name here
            defaultFont = QFont(config.DEFAULT_FONT)
            super().setFont(defaultFont)    
            print("Custom font loaded successfully.")
        else:
            print("Failed to load custom font.")

        # self.setWindowFlags(
        #     (Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.CustomizeWindowHint))

        # self.setMinimumSize(config.MIN_WINDOW_WIDTH, config.MIN_WINDOW_HEIGHT)
        self.setWindowTitle(config.TITLE)
        self.setWindowIcon(QIcon(config.ICON_PATH))

        self.browser = QWebEngineView()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, 'templates', 'index.html')
        self.browser.setUrl(QUrl.fromLocalFile(html_path))
        self.browser.page().profile().downloadRequested.connect(self.on_download_requested)

        self.setCentralWidget(self.browser)

    @Slot(str)
    def on_download_requested(self, url):
        if url.startswith('folder://'):
            folder_path = url.replace('folder://', '')
            print("Selected Folder Path:", folder_path)
        elif url.startswith('file://'):
            file_path = url.replace('file://', '')
            print("Selected File Path:", file_path)
