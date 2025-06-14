from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import io
from datetime import datetime

def generar_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    ciudad = data.get("ciudad", "Los Ángeles")
    fecha = data.get("fecha", datetime.today().strftime("%d-%m-%Y"))
    empleador = data.get("empleador", "Juan Pérez Soto")
    rut_empleador = data.get("rut_empleador", "99999999-9")
    dom_empleador = data.get("domicilio_empleador", "Ficticio n°1")
    comuna_empleador = data.get("comuna_empleador", "Los Ángeles")
    trabajador = data.get("trabajador", "Juan Pérez Pérez")
    nacionalidad = data.get("nacionalidad_trabajador", "Chileno")
    dom_trabajador = data.get("domicilio_trabajador", "Ficticio n°1")
    comuna_trabajador = data.get("comuna_trabajador", "Los Ángeles")
    rut_trabajador = data.get("rut_trabajador", "99999999-9")
    trabajo = data.get("trabajo", "Cuidador de parcela")
    dir_trabajo = data.get("direccion_trabajo", "Ficticio n°1")
    comuna_trabajo = data.get("comuna_trabajo", "Los Ángeles")
    sueldo = data.get("sueldo_bruto", "Sueldo base más bonos, comisiones, horas extras y otros")
    inicio = data.get("fecha_inicio", datetime.today().strftime("%d-%m-%Y"))

    texto = f"""CONTRATO DE TRABAJO

En {ciudad}, a {fecha}, entre {empleador}, RUT {rut_empleador}, con domicilio en {dom_empleador}, comuna de {comuna_empleador}, en adelante "el Empleador", y don {trabajador}, de nacionalidad {nacionalidad}, RUT {rut_trabajador}, con domicilio en {dom_trabajador}, comuna de {comuna_trabajador}, en adelante "el Trabajador", se ha convenido el siguiente contrato:

1. El trabajador se obliga a prestar servicios personales como {trabajo} en {dir_trabajo}, comuna de {comuna_trabajo}.
2. La jornada y remuneración se determinarán de acuerdo a lo legal.
3. El sueldo bruto mensual será: {sueldo}.
4. El presente contrato comenzará a regir desde el {inicio}.
5. Ambas partes declaran conocer y aceptar el presente contrato.

FIRMAS:

__________________________          __________________________
{empleador}                            {trabajador}
"""
    pdf.multi_cell(0, 10, texto)

    output = io.BytesIO()
    pdf.output(output)
    output.seek(0)

    reader = PdfReader(output)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(user_password="@1234@", owner_password="@1234@")

    final_output = io.BytesIO()
    writer.write(final_output)
    final_output.seek(0)

    return final_output.read()
