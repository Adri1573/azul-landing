# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', '/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialB', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFont(TTFont('ArialI', '/System/Library/Fonts/Supplemental/Arial Italic.ttf'))
pdfmetrics.registerFont(TTFont('ArialRB', '/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf'))

F = 'Arial'
FB = 'ArialB'
FI = 'ArialI'
FR = 'ArialRB'

AZUL_DARK = HexColor('#2B8CC4')
AMARILLO = HexColor('#F7D44C')
MARRON = HexColor('#2C1810')
BLANCO = HexColor('#FFFFFF')
GRIS = HexColor('#6B7280')
VERDE = HexColor('#2ECC71')
VERDE_LIGHT = HexColor('#E8F8F0')
CREMA = HexColor('#F5EAD6')

W = 6.5 * inch

def build_pdf():
    doc = SimpleDocTemplate(
        "/Users/nana1516/azul-landing/bienvenida-azul.pdf",
        pagesize=letter,
        topMargin=0.6*inch, bottomMargin=0.6*inch,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
    )
    story = []

    # Logo
    logo = Image('/Users/nana1516/Downloads/az1024.png', width=1.4*inch, height=1.4*inch)

    # Header
    header_items = [
        [logo],
        [Spacer(1, 10)],
        [Paragraph("A Z U L", ParagraphStyle('b1', fontName=FR, fontSize=46, textColor=AMARILLO, alignment=TA_CENTER, leading=54))],
        [Paragraph("La app de los perros felices", ParagraphStyle('b2', fontName=FI, fontSize=13, textColor=HexColor('#FFFFFFCC'), alignment=TA_CENTER, leading=16))],
        [Spacer(1, 24)],
        [Paragraph("Bienvenido a AZUL Premium", ParagraphStyle('b3', fontName=FR, fontSize=30, textColor=BLANCO, alignment=TA_CENTER, leading=38))],
        [Spacer(1, 10)],
        [Paragraph("Tu acceso está listo. Sigue estos pasos\npara empezar a entrenar a tu perro hoy.", ParagraphStyle('b4', fontName=F, fontSize=14, textColor=HexColor('#FFFFFFCC'), alignment=TA_CENTER, leading=22))],
    ]

    ht = Table([[item[0]] for item in header_items], colWidths=[6.8*inch])
    ht.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), AZUL_DARK),
        ('ROUNDEDCORNERS', [20, 20, 20, 20]),
        ('TOPPADDING', (0,0), (0,0), 30),
        ('BOTTOMPADDING', (-1,-1), (-1,-1), 30),
        ('LEFTPADDING', (0,0), (-1,-1), 20),
        ('RIGHTPADDING', (0,0), (-1,-1), 20),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(ht)
    story.append(Spacer(1, 30))

    # Paso 1
    step_style = ParagraphStyle('step', fontName=F, fontSize=12, textColor=MARRON, leading=18)

    def step_box(num, title, content, color):
        data = [[Paragraph(
            f"<b><font size='18' color='{BLANCO.hexval()}'>{num}</font></b>",
            ParagraphStyle(f'sn{num}', fontName=FR, fontSize=18, textColor=BLANCO, alignment=TA_CENTER, leading=24))]]
        num_t = Table(data, colWidths=[0.55*inch], rowHeights=[0.5*inch])
        num_t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), color),
            ('ROUNDEDCORNERS', [10, 10, 10, 10]),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ]))

        row = [[num_t, Paragraph(f"<b>{title}</b><br/>{content}", step_style)]]
        rt = Table(row, colWidths=[0.75*inch, W - 0.75*inch])
        rt.setStyle(TableStyle([
            ('TOPPADDING', (0,0), (-1,-1), 12),
            ('BOTTOMPADDING', (0,0), (-1,-1), 12),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LINEBELOW', (0,0), (-1,-1), 0.5, HexColor('#E5E7EB')),
        ]))
        story.append(rt)
        story.append(Spacer(1, 8))

    step_box(1, "Explora tu contenido Premium",
        "En tu <b>Área de Miembros de Hotmart</b> encontrarás tu Plan de Entrenamiento "
        "de 7 días listo para empezar hoy mismo. Accede con el mismo email con el que compraste.",
        AZUL_DARK)

    step_box(2, "Empieza tu plan hoy",
        "Sigue el plan día a día — solo necesitas <b>10-15 minutos diarios</b>. "
        "Cada día tiene ejercicios claros, paso a paso, sin complicaciones.",
        VERDE)

    step_box(3, "La app AZUL viene en camino",
        "Estamos preparando la app con <b>AzulIA</b> (tu entrenador con IA), "
        "+50 ejercicios, QR para el collar y mucho más. "
        "Te avisaremos por email cuando esté lista para descargar.",
        HexColor('#FF8C42'))

    step_box(4, "¿Tienes dudas?",
        "Escríbenos a <b>azulapp.info@gmail.com</b> y te respondemos en menos de 24 horas. "
        "¡Gracias por confiar en AZUL!",
        HexColor('#9B59B6'))

    story.append(Spacer(1, 16))

    # Lo que incluye
    inc_data = [[Paragraph(
        "<b>Tu plan Premium incluye:</b><br/><br/>"
        "• AzulIA — tu entrenador personal con IA, 24/7<br/>"
        "• +50 ejercicios con pasos guiados<br/>"
        "• Seguimiento de progreso día a día<br/>"
        "• Recordatorios de salud, vacunas y vet<br/>"
        "• Sistema de logros y rachas<br/>"
        "• QR inteligente para el collar de tu perro<br/>"
        "• Comunidad de dueños AZUL<br/>"
        "• Disponible en español, inglés, francés y portugués",
        ParagraphStyle('inc', fontName=F, fontSize=12, textColor=MARRON, leading=19))]]
    it = Table(inc_data, colWidths=[W])
    it.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CREMA),
        ('ROUNDEDCORNERS', [14, 14, 14, 14]),
        ('TOPPADDING', (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 20),
        ('LEFTPADDING', (0,0), (-1,-1), 22),
        ('RIGHTPADDING', (0,0), (-1,-1), 22),
    ]))
    story.append(it)
    story.append(Spacer(1, 20))

    # Soporte
    sup_data = [[Paragraph(
        "<b>¿Necesitas ayuda?</b><br/><br/>"
        "Escríbenos a <b>azulapp.info@gmail.com</b> y te respondemos en menos de 24 horas.<br/><br/>"
        "¡Gracias por confiar en AZUL! Tu perro va a notar la diferencia.",
        ParagraphStyle('sup', fontName=F, fontSize=12, textColor=BLANCO, leading=19, alignment=TA_CENTER))]]
    st = Table(sup_data, colWidths=[W])
    st.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), AZUL_DARK),
        ('ROUNDEDCORNERS', [14, 14, 14, 14]),
        ('TOPPADDING', (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 20),
        ('LEFTPADDING', (0,0), (-1,-1), 22),
        ('RIGHTPADDING', (0,0), (-1,-1), 22),
    ]))
    story.append(st)

    story.append(Spacer(1, 20))
    story.append(Paragraph("© 2026 AZUL App · azulapp.org", ParagraphStyle('ft', fontName=F, fontSize=9, textColor=GRIS, alignment=TA_CENTER)))

    doc.build(story)
    print("✅ PDF de bienvenida generado!")

if __name__ == '__main__':
    build_pdf()
