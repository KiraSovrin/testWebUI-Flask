# app/core/thread.py

from PySide6.QtCore import QTimer
import hashlib
import json
import os
from transliterate import translit

from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import QObject, QThread, Signal
from app.core.db import ImageDatabase
from config import Config
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, as_completed

# relative path to file
script_dir = os.path.dirname(os.path.realpath(__file__))
# with open(f'{script_dir}\\config.json', 'r') as conf_file:
#     const = json.load(conf_file)

# IMAGE_EXTENSIONS = const['IMG_EXTENSIONS']


class ImageLoaderThread:
    # imageLoaded = Signal(list)      # emitted when a new image is loaded
    # progressUpdated = Signal(int)   # emitted when the progress updates

    def __init__(self, folder_path_list) -> None:
        # super().__init__()
        self._folder_path_list = folder_path_list
        self._duplicate_images = []
        self._queue = Queue()
        self._executor = None
        self._threads = 0
        self.config = Config()
        self.db = ImageDatabase()


        # self.total_images = len(image_paths)
        # self.current_image_index = 0

    def run(self):
        # db = ImageDatabase()
        # config = Config()

        # start the executor if not already initialized
        if self._executor is None:
            self._executor = ThreadPoolExecutor()

        # add each folder path to the queue
        for folder_path in self._folder_path_list:
            self._queue.put(folder_path)

        while not self._queue.empty():
            with self._executor as executor:
                futures = []
                for _ in range(self._threads ):
                    future = executor.submit(self._process_folder, self._queue.get())
                    futures.append((future, folder_path))

                # [future.result() for future in futures]
                as_completed(futures)
                for future, folder_path in as_completed(futures):
                    # if future.exception() is not None:
                    result = future.result()
                    if result[0]:
                        self._duplicate_images += result[1]
        
        self.db.close()

    def _process_folder(self, folder_path):
        # img_path = self._queue.get()
        # for path in self.image_paths:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(tuple(self.config.IMAGE_EXTENSIONS)):
                    # # check if file is already added to DB
                    # if self.db.image_exists(os.path.basename(file)):
                    #     continue
                    # Check if the filename contains Russian characters
                    if any(ord(char) > 127 for char in file):
                        # Transliterate Russian characters to Latin
                        new_filename = translit(file, 'ru', reversed=True)
                        # Rename the file if the name has changed
                        if new_filename != file:
                            os.rename(os.path.join(root, file), os.path.join(root, new_filename))
                            file = new_filename
                    image_path = os.path.join(root, file)
                    # Use the filename as the label
                    image_label = os.path.basename(file)
                    phash = self.calculate_phash(image_path)
                    if phash is not None:
                        image_size = self.get_image_dim(image_path)
                        self.db.add_image(image_path, image_label,
                                        str(phash), str(image_size))
                        
    def _find_duplicates(self):                   
        # Find all images with similar phash values
        duplicates = self.db.find_duplicates_with_similarity()
        self.db.close()

        # total_rows = len(duplicates)
        # print(total_rows)
        card_info = []

        for row in duplicates:
            """
            image path for left image -> row[0]
            image path for right image -> row[1]
            similarity percentage -> row[2]
            """
            # if row[2]  > 0.5 and row[0] != row[1]:
            card_info.append([row[0], row[2], row[1]])


        return card_info
            # self.imageLoaded.emit(
            #     ( img_path_left, img_path_right, similarity))

        # self.progressUpdated.emit(100)  # Ensure to emit final progress

    def get_image_dim(self, image_path):
        """
        get image dimension in format  width x height
        """
        try:
            from PIL import Image
            image = Image.open(image_path)
            width, height = image.size
            return f'{width}x{height}'
        except Exception as e:
            print(e)
            return None
        
    def calculate_phash(self, image_path):
        """
        Calculate the perceptual hash of an image after resizing it
        """
        from PIL import Image
        import imagehash

        # 89478485 maximum image size in bytes if image is bigger imagehash will get a warning
        # can be ignored at the moment
        try:
            image = Image.open(image_path)
            if image.mode == "P" and "transparency" in image.info:
                image = image.convert("RGBA")

            phash = imagehash.phash(image)
            return phash
        except Exception as e:
            print(e)
            return None
