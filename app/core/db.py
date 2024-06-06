from imagehash import hex_to_hash
import sqlite3


class ImageDatabase:
    def __init__(self, db_path='image_data.db'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """
        Create a table to store image data if it doesn't already exist.
        """
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS images (
                                id INTEGER PRIMARY KEY,
                                path TEXT NOT NULL,
                                label TEXT NOT NULL,
                                phash TEXT NOT NULL,
                                dim    TEXT NOT NULL,
                                UNIQUE(label)  
                            )'''
                            )
        self.connection.commit()

    def find_duplicates_with_similarity(self):
        """
        Find duplicates and calculate similarity percentage.
        """
        self.cursor.execute('''
            SELECT path, phash
            FROM images
        ''')
        images = self.cursor.fetchall()

        duplicates = []
        for i in range(len(images)):
            for j in range(i + 1, len(images)):
                hash1 = hex_to_hash(images[i][1])
                hash2 = hex_to_hash(images[j][1])
                if hash1 - hash2 < 10:  # Threshold for considering as duplicate
                    similarity = (1 - (hash1 - hash2) /
                                  len(hash1.hash) ** 2) * 100
                    duplicates.append((images[i][0], images[j][0], similarity))
        return duplicates

    def image_exists(self, label):
        """
        Check if an image with the same label already exists in the database.
        """
        self.cursor.execute('SELECT 1 FROM images WHERE label = ?', (label,))
        return self.cursor.fetchone() is not None

    def add_image(self, path, label, phash, size):
        """
        Add a new image to the database if it doesn't already exist based on its label.
        """
        if not self.image_exists(label):
            self.cursor.execute(
                'INSERT INTO images (path, label, phash, size) VALUES (?, ?, ?, ?)', (path, label, phash, size))
            self.connection.commit()
        # else:
        #     print(f"Image with label '{label}' already exists and was not added.")

    def find_duplicates(self):
        """
        Find and return a list of duplicate images based on perceptual hash.
        """
        self.cursor.execute('''
                            SELECT path, label, phash, COUNT(*) as cnt
                            FROM images
                            GROUP BY phash
                            HAVING cnt > 1
                            ''')
        return self.cursor.fetchall()

    def clear_database(self):
        """
        Clear the database.
        """
        self.cursor.execute('DELETE FROM images')
        self.connection.commit()

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()
