import xml.etree.ElementTree as ET
import mysql.connector

tree = ET.parse("kanjidic2.xml")
root = tree.getroot()

connection = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    port=32000,
    database="kanji",
    charset="utf8mb4"
)

cursor = connection.cursor()

sql = """
      INSERT INTO kanji
      (form, meanings, unicode_value, stroke_count,
       onyomi_readings, kunyomi_readings, nanori_readings)
      VALUES
      (%s, %s, %s, %s, %s, %s, %s)
      """

for character in root.findall("character"):
    literal_element = character.find("literal")
    if literal_element is None:
        continue
    form = literal_element.text
    unicode_element = character.find(
        "codepoint/cp_value[@cp_type='ucs']"
    )
    if unicode_element is not None:
        unicode_value = unicode_element.text
    else:
        unicode_value = None
    stroke_element = character.find("misc/stroke_count")
    if stroke_element is not None and stroke_element.text is not None:
        stroke_count = int(stroke_element.text)
    else:
        stroke_count = None
    kunyomi_readings = []
    onyomi_readings = []
    nanori_readings = []
    for reading in character.findall("reading_meaning/rmgroup/reading"):
        reading_type = reading.attrib.get("r_type")
        if reading_type == "ja_on":
            if reading.text is not None:
                onyomi_readings.append(reading.text)
        elif reading_type == "ja_kun":
            if reading.text is not None:
                kunyomi_readings.append(reading.text)
    for nanori in character.findall("reading_meaning/nanori"):
        if nanori.text is not None:
            nanori_readings.append(nanori.text)
    onyomi_text = ";".join(onyomi_readings)
    kunyomi_text = ";".join(kunyomi_readings)
    nanori_text = ";".join(nanori_readings)
    meanings = []
    for meaning in character.findall("reading_meaning/rmgroup/meaning"):
        if meaning.text is not None and meaning.get("m_lang") is None:
            meanings.append(meaning.text)
    meaning_text = ";".join(meanings)
    cursor.execute(
        sql,
        (
            form,
            meaning_text,
            unicode_value,
            stroke_count,
            onyomi_text,
            kunyomi_text,
            nanori_text
        )
    )

connection.commit()
cursor.close()
connection.close()

print("KANJIDIC2 import complete!")

