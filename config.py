# config.py

import os

basedir = os.path.dirname(__file__)

class Config:
    BASE_DIR = basedir
    MIN_WINDOW_WIDTH = 1024
    MIN_WINDOW_HEIGHT = 720
    DEFAULT_FONT = "Montserrat-VariableFont_wght.ttf"
    TITLE = "ImagiDetect"
    ICON_PATH = os.path.join(basedir,'app', 'static', 'img' 'icon.png')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg"]
    
    # to do: find a better implementation
    def __init__(self) -> None:
        self.secret_key = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    def get_secret_key(self):
        return self.secret_key

