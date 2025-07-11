from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import io
from datetime import datetime

def generar_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)

    pdf.cell(0, 10, "CONTRATO DE TRABAJO", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)

    ciudad = data.get("ciudad", "Los Ángeles").upper()
    fecha = data.get("fecha", datetime.today().strftime("%d-%m-%Y"))
    empleador = data.get("empleador", "JUAN PÉREZ SOTO").upper()
    rut_empleador = data.get("rut_empleador", "99999999-9")
    dom_empleador = data.get("dom_empleador", "FICTICIO N°1").upper()
    com_empleador = data.get("com_empleador", "LOS ÁNGELES").upper()
    trabajador = data.get("trabajador", "JUAN PÉREZ PÉREZ").upper()
    nacionalidad = data.get("nacionalidad", "CHILENO").upper()
    dom_trabajador = data.get("dom_trabajador", "FICTICIO N°1").upper()
    com_trabajador = data.get("com_trabajador", "LOS ÁNGELES").upper()
    rut_trabajador = data.get("rut_trabajador", "99999999-9")
    trabajo = data.get("servicio", "CUIDADOR DE PARCELA").upper()
    dir_trabajo = data.get("dir_trabajo", "FICTICIO N°1").upper()
    com_trabajo = data.get("com_trabajo", "LOS ÁNGELES").upper()
    sueldo = data.get("sueldo", "SUELDO BASE MÁS BONOS, COMISIONES, HORAS EXTRAS Y OTROS").upper()
    inicio = data.get("fecha_inicio", datetime.today().strftime("%d-%m-%Y"))

    texto = f"""
EN {ciudad}, A {fecha}, ENTRE {empleador}, RUT {rut_empleador}, CON DOMICILIO EN {dom_empleador}, COMUNA DE {com_empleador}, EN ADELANTE "EL EMPLEADOR", Y DON {trabajador}, DE NACIONALIDAD {nacionalidad}, RUT {rut_trabajador}, CON DOMICILIO EN {dom_trabajador}, COMUNA DE {com_trabajador}, EN ADELANTE "EL TRABAJADOR", SE HA CONVENIDO EL SIGUIENTE CONTRATO:

1. EL TRABAJADOR SE OBLIGA A PRESTAR SERVICIOS PERSONALES COMO {trabajo} EN {dir_trabajo}, COMUNA DE {com_trabajo}.
2. LA JORNADA Y REMUNERACIÓN SE DETERMINARÁN DE ACUERDO A LO LEGAL.
3. EL SUELDO BRUTO MENSUAL SERÁ: {sueldo}.
4. EL PRESENTE CONTRATO COMENZARÁ A REGIR DESDE EL {inicio}.
5. AMBAS PARTES DECLARAN CONOCER Y ACEPTAR EL PRESENTE CONTRATO.
"""
    pdf.multi_cell(0, 10, texto.strip())

    pdf.ln(25)  # Espacio antes de firma empleador

    pdf.cell(0, 10, "__________________________", ln=True, align="C")
    pdf.cell(0, 10, empleador, ln=True, align="C")
    pdf.cell(0, 10, f"(RUT: {rut_empleador})", ln=True, align="C")

    pdf.ln(25)  # Espacio entre firmas

    pdf.cell(0, 10, "__________________________", ln=True, align="C")
    pdf.cell(0, 10, trabajador, ln=True, align="C")
    pdf.cell(0, 10, f"(RUT: {rut_trabajador})", ln=True, align="C")

    pdf_output = pdf.output(dest='S').encode('latin1')
    temp_stream = io.BytesIO(pdf_output)

    reader = PdfReader(temp_stream)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(user_password="@1234@", owner_password="@1234@")

    final_output = io.BytesIO()
    writer.write(final_output)
    final_output.seek(0)

    return final_output.read()
