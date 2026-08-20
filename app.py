from flask import Flask, request, jsonify, render_template
from app.services import Services
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
services = Services()

@app.route('/', methods=['GET'])
def ui() -> str:
    app.logger.info("ui - Got request")
    return render_template('kanji_lookup_tool.html')

@app.route("/app/kanji", methods=["POST"])
def lookup_kanji():
    data = request.get_json()
    app.logger.info(f"/app/kanji - Got request: {data}")
    if not data or not data.get("kanji"):
        return {"message": "Must provide a kanji"}, 400
    kanji = services.get_kanji_info(data.get("kanji"))
    return jsonify(
        f"Form:              {kanji.form}\n"
        f"Meanings:          {kanji.meanings}\n"
        f"Kun'yomi Readings: {kanji.kunyomi_readings}\n"
        f"On'yomi Readings:  {kanji.onyomi_readings}\n"
        f"Nanori Readings:   {kanji.nanori_readings}\n"
        f"Stroke Count:      {kanji.stroke_count}\n"
        f"Unicode:           {kanji.unicode_value}"
    )

@app.route("/app/efficiency", methods=["POST"])
def calculate_efficiency():
    data = request.get_json()
    app.logger.info(f"/app/efficiency - Got request: {data}")
    if not data or not data.get("kanji"):
        return {"message": "Must provide a kanji"}, 400
    kanji = services.get_kanji_info(data.get("kanji"))
    efficiency = services.get_efficiency_scores(kanji)
    return jsonify(efficiency)


if __name__ == "__main__":
    app.run(host="localhost")
