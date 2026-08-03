from db.repository import *
import mysql.connector

class MysqlRepository(Repository):

    def __init__(self):
        config = {
            "user": "root",
            "password": "root",
            "host": "127.0.0.1",
            "port": "32000",
            "database": "kanji"
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor(dictionary=True)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def mapper(self, row):
        kanji = Kanji(
            form=row["form"],
            meanings=row["meanings"].split(";"),
            unicode_value=row["unicode_value"],
            stroke_count=row["stroke_count"],
            kunyomi_readings=row["kunyomi_readings"].split(";"),
            onyomi_readings=row["onyomi_readings"].split(";"),
            nanori_readings=row["nanori_readings"].split(";")
        )
        return kanji

    def get_kanji(self, literal):
        sql = "SELECT * FROM kanji WHERE form = %s"
        self.cursor.execute(sql, (literal,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return self.mapper(row)
