from flask import Flask, request, send_file
from flask_cors import CORS
from generar_pdf import generar_pdf
import io

app = Flask(__name__)
CORS(app)

@app.route("/generar_pdf", methods=["POST"])
def generar():
    data = request.get_json()
    pdf_bytes = generar_pdf(data)

    return send_file(
        io.BytesIO(pdf_bytes),
        as_attachment=True,
        download_name="contrato_cybernova.pdf",
        mimetype="application/pdf"
    )
