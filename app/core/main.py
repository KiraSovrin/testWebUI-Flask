# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PySide6.QtWebEngineWidgets import QWebEngineView
# from PySide6.QtCore import QUrl
# import os


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("File Backup App")

#         self.browser = QWebEngineView()
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         html_path = os.path.join(current_dir, 'templates', 'index.html')
#         self.browser.setUrl(QUrl.fromLocalFile(html_path))

#         self.setCentralWidget(self.browser)



