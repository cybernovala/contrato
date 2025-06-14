from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import io
from datetime import datetime

def generar_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    
    # Título en negrita y centrado
    pdf.cell(0, 10, "CONTRATO DE TRABAJO", ln=True, align="C")
    pdf.ln(10)

    # Cambiamos a fuente normal para el resto del texto
    pdf.set_font("Arial", "", 12)

    # Datos con valores por defecto y convertidos a mayúsculas
    ciudad = data.get("ciudad", "Los Ángeles").upper()
    fecha = data.get("fecha", datetime.today().strftime("%d-%m-%Y"))
    empleador = data.get("empleador", "Juan Pérez Soto").upper()
    rut_empleador = data.get("rut_empleador", "99999999-9")
    dom_empleador = data.get("domicilio_empleador", "FICTICIO N°1").upper()
    comuna_empleador = data.get("comuna_empleador", "Los Ángeles").upper()
    trabajador = data.get("trabajador", "Juan Pérez Pérez").upper()
    nacionalidad = data.get("nacionalidad_trabajador", "Chileno").upper()
    dom_trabajador = data.get("domicilio_trabajador", "FICTICIO N°1").upper()
    comuna_trabajador = data.get("comuna_trabajador", "Los Ángeles").upper()
    rut_trabajador = data.get("rut_trabajador", "99999999-9")
    trabajo = data.get("trabajo", "Cuidador de parcela").upper()
    dir_trabajo = data.get("direccion_trabajo", "FICTICIO N°1").upper()
    comuna_trabajo = data.get("comuna_trabajo", "Los Ángeles").upper()
    sueldo = data.get("sueldo_bruto", "SUELDO BASE MÁS BONOS, COMISIONES, HORAS EXTRAS Y OTROS").upper()
    inicio = data.get("fecha_inicio", datetime.today().strftime("%d-%m-%Y"))

    # Texto del contrato en MAYÚSCULAS
    texto = f"""
EN {ciudad}, A {fecha}, ENTRE {empleador}, RUT {rut_empleador}, CON DOMICILIO EN {dom_empleador}, COMUNA DE {comuna_empleador}, EN ADELANTE "EL EMPLEADOR", Y DON {trabajador}, DE NACIONALIDAD {nacionalidad}, RUT {rut_trabajador}, CON DOMICILIO EN {dom_trabajador}, COMUNA DE {comuna_trabajador}, EN ADELANTE "EL TRABAJADOR", SE HA CONVENIDO EL SIGUIENTE CONTRATO:

1. EL TRABAJADOR SE OBLIGA A PRESTAR SERVICIOS PERSONALES COMO {trabajo} EN {dir_trabajo}, COMUNA DE {comuna_trabajo}.
2. LA JORNADA Y REMUNERACIÓN SE DETERMINARÁN DE ACUERDO A LO LEGAL.
3. EL SUELDO BRUTO MENSUAL SERÁ: {sueldo}.
4. EL PRESENTE CONTRATO COMENZARÁ A REGIR DESDE EL {inicio}.
5. AMBAS PARTES DECLARAN CONOCER Y ACEPTAR EL PRESENTE CONTRATO.

FIRMAS:

__________________________                    __________________________
{empleador}                                   {trabajador}
(RUT: {rut_empleador})                        (RUT: {rut_trabajador})
"""
    pdf.multi_cell(0, 10, texto.strip())

    # Exportar como string y codificar bien
    pdf_output = pdf.output(dest='S').encode('latin1')
    temp_stream = io.BytesIO(pdf_output)

    # Agregar protección
    reader = PdfReader(temp_stream)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(user_password="@1234@", owner_password="@1234@")

    final_output = io.BytesIO()
    writer.write(final_output)
    final_output.seek(0)

    return final_output.read()
