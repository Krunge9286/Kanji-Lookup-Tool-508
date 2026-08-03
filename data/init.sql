CREATE DATABASE kanji
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE kanji;

CREATE TABLE kanji (
    id INT AUTO_INCREMENT PRIMARY KEY,
    form CHAR(1) NOT NULL,
    meanings TEXT,
    unicode_value VARCHAR(10),
    stroke_count INT,
    onyomi_readings TEXT,
    kunyomi_readings TEXT,
    nanori_readings TEXT
)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
