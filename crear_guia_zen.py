# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether, Image
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', '/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialB', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFont(TTFont('ArialI', '/System/Library/Fonts/Supplemental/Arial Italic.ttf'))
pdfmetrics.registerFont(TTFont('ArialBI', '/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf'))
pdfmetrics.registerFont(TTFont('ArialRB', '/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf'))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='ArialB', italic='ArialI', boldItalic='ArialBI')

F = 'Arial'
FB = 'ArialB'
FI = 'ArialI'
FR = 'ArialRB'

# ── Colores vibrantes ──
AZUL = HexColor('#60B8E8')
AZUL_DARK = HexColor('#2B8CC4')
AZUL_DEEP = HexColor('#1A6FA0')
VERDE = HexColor('#2ECC71')
VERDE_DARK = HexColor('#1FAF5C')
VERDE_LIGHT = HexColor('#E8F8F0')
NARANJA = HexColor('#FF8C42')
NARANJA_DARK = HexColor('#E67332')
NARANJA_LIGHT = HexColor('#FFF3EB')
MARRON = HexColor('#2C1810')
AMARILLO = HexColor('#F7D44C')
CREMA = HexColor('#F5EAD6')
GRIS = HexColor('#6B7280')
BLANCO = HexColor('#FFFFFF')
ROJO_SOFT = HexColor('#FF6B6B')
MORADO = HexColor('#9B59B6')
MORADO_LIGHT = HexColor('#F5EEFF')
AZUL_LIGHT = HexColor('#EBF5FC')

W = 6.5 * inch  # content width

def box(story, text, bg, style, padding=14):
    data = [[Paragraph(text, style)]]
    t = Table(data, colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('ROUNDEDCORNERS', [12, 12, 12, 12]),
        ('TOPPADDING', (0,0), (-1,-1), padding),
        ('BOTTOMPADDING', (0,0), (-1,-1), padding),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

def section_header(story, week_num, title, color, emoji):
    data = [[Paragraph(f"{emoji}  SEMANA {week_num}: {title}", ParagraphStyle('sh', fontName=FB, fontSize=22, textColor=BLANCO, leading=28, alignment=TA_CENTER))]]
    t = Table(data, colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('ROUNDEDCORNERS', [14, 14, 14, 14]),
        ('TOPPADDING', (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 20),
        ('LEFTPADDING', (0,0), (-1,-1), 20),
        ('RIGHTPADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(t)
    story.append(Spacer(1, 16))

def day_block(story, day_num, title, objetivo, materiales, pasos, tip, exito, color, color_light):
    elements = []

    # Day header
    hdr = [[Paragraph(f"DÍA {day_num}  |  {title}", ParagraphStyle('dn', fontName=FB, fontSize=16, textColor=BLANCO, leading=22))]]
    ht = Table(hdr, colWidths=[W])
    ht.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('ROUNDEDCORNERS', [12, 12, 0, 0]),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    elements.append(ht)

    # Body container
    body_parts = []
    body_parts.append(Paragraph(f"<b>🎯 Objetivo:</b> {objetivo}", ParagraphStyle('obj', fontName=F, fontSize=11, textColor=MARRON, leading=16, spaceAfter=6)))
    body_parts.append(Paragraph(f"<b>🧰 Necesitas:</b> {materiales}", ParagraphStyle('mat', fontName=F, fontSize=11, textColor=GRIS, leading=16, spaceAfter=10)))

    body_parts.append(Paragraph("<b>📋 Paso a paso:</b>", ParagraphStyle('ph', fontName=FB, fontSize=12, textColor=color, leading=16, spaceAfter=6)))
    for i, paso in enumerate(pasos, 1):
        body_parts.append(Paragraph(f"<b>{i}.</b> {paso}", ParagraphStyle(f'p{i}', fontName=F, fontSize=11, textColor=MARRON, leading=16, spaceAfter=5, leftIndent=16)))

    body_content = [[p] for p in body_parts]
    bt = Table(body_content, colWidths=[W - 36])
    bt.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))

    body_wrap = [[bt]]
    bw = Table(body_wrap, colWidths=[W])
    bw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color_light),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
    ]))
    elements.append(bw)

    # Tip
    tip_data = [[Paragraph(f"<b>💡 Tip:</b> {tip}", ParagraphStyle('tip', fontName=FI, fontSize=10, textColor=MARRON, leading=14))]]
    tip_t = Table(tip_data, colWidths=[W])
    tip_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CREMA),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
    ]))
    elements.append(tip_t)

    # Éxito
    ex_data = [[Paragraph(f"<b>✅ Señal de éxito:</b> {exito}", ParagraphStyle('ex', fontName=F, fontSize=10, textColor=HexColor('#1FAF5C'), leading=14))]]
    ex_t = Table(ex_data, colWidths=[W])
    ex_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), VERDE_LIGHT),
        ('ROUNDEDCORNERS', [0, 0, 12, 12]),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
    ]))
    elements.append(ex_t)
    elements.append(Spacer(1, 18))

    story.append(KeepTogether(elements))

def build_pdf():
    doc = SimpleDocTemplate(
        "/Users/nana1516/azul-landing/guia-zen-azul.pdf",
        pagesize=letter,
        topMargin=0.6*inch, bottomMargin=0.6*inch,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
    )
    story = []

    # ═══════════════════════════════════════════════════════════
    # PORTADA
    # ═══════════════════════════════════════════════════════════
    logo_img = Image('/Users/nana1516/Downloads/az1024.png', width=1.4*inch, height=1.4*inch)

    cover_items = [
        [logo_img],
        [Spacer(1, 8)],
        [Paragraph("A Z U L", ParagraphStyle('b1', fontName=FR, fontSize=46, textColor=AMARILLO, alignment=TA_CENTER, leading=54))],
        [Paragraph("La app de los perros felices", ParagraphStyle('b2', fontName=FI, fontSize=13, textColor=HexColor('#FFFFFFCC'), alignment=TA_CENTER, leading=16))],
        [Spacer(1, 24)],
        [Paragraph("GUÍA ZEN", ParagraphStyle('b3', fontName=FB, fontSize=26, textColor=BLANCO, alignment=TA_CENTER, leading=32))],
        [Spacer(1, 6)],
        [Paragraph("21 días para la\ncalma total", ParagraphStyle('b4', fontName=FR, fontSize=36, textColor=BLANCO, alignment=TA_CENTER, leading=44))],
        [Spacer(1, 20)],
        [Paragraph("El método paso a paso para que tu perro\naprenda a calmarse en cualquier situación", ParagraphStyle('b5', fontName=F, fontSize=13, textColor=HexColor('#FFFFFFCC'), alignment=TA_CENTER, leading=20))],
        [Spacer(1, 24)],
        [Paragraph("Sin castigos  ·  Sin gritos  ·  Refuerzo positivo", ParagraphStyle('b6', fontName=FB, fontSize=12, textColor=BLANCO, alignment=TA_CENTER, leading=16))],
        [Spacer(1, 8)],
        [Paragraph("+12,000 perros entrenados", ParagraphStyle('b7', fontName=F, fontSize=11, textColor=HexColor('#FFFFFF99'), alignment=TA_CENTER))],
        [Spacer(1, 16)],
        [Paragraph("azulapp.org", ParagraphStyle('b8', fontName=FB, fontSize=14, textColor=AMARILLO, alignment=TA_CENTER))],
    ]

    ct = Table([[item[0]] for item in cover_items], colWidths=[6.8*inch])
    ct.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), AZUL_DARK),
        ('ROUNDEDCORNERS', [20, 20, 20, 20]),
        ('TOPPADDING', (0,0), (0,0), 30),
        ('BOTTOMPADDING', (-1,-1), (-1,-1), 30),
        ('LEFTPADDING', (0,0), (-1,-1), 20),
        ('RIGHTPADDING', (0,0), (-1,-1), 20),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(ct)
    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # ÍNDICE
    # ═══════════════════════════════════════════════════════════
    story.append(Spacer(1, 10))
    story.append(Paragraph("📖 ÍNDICE", ParagraphStyle('idx_title', fontName=FR, fontSize=32, textColor=AZUL_DARK, alignment=TA_CENTER, leading=40)))
    story.append(Spacer(1, 24))

    toc_sections = [
        ("📝", "Introducción", "Por qué tu perro necesita calma", AZUL_DARK),
        ("📐", "Cómo usar esta guía", "Reglas e instrucciones", AZUL_DARK),
        ("🐾", "Semana 1: Fundamentos", "Días 1-7 · Bases de la calma", AZUL),
        ("🏠", "Semana 2: Mundo Real", "Días 8-14 · Situaciones cotidianas", VERDE),
        ("🏆", "Semana 3: Nivel Avanzado", "Días 15-21 · Calma bajo presión", NARANJA),
        ("🆘", "Emergencias", "Qué hacer si algo no funciona", ROJO_SOFT),
        ("🎉", "Felicitaciones", "Tu logro y próximos pasos", MORADO),
    ]

    for emoji, title, sub, color in toc_sections:
        row = [[
            Paragraph(emoji, ParagraphStyle('te', fontName=F, fontSize=22, leading=28)),
            Paragraph(f"<b>{title}</b><br/><font size='10' color='#6B7280'>{sub}</font>", ParagraphStyle('tt', fontName=F, fontSize=14, textColor=color, leading=20)),
        ]]
        rt = Table(row, colWidths=[0.6*inch, W - 0.6*inch])
        rt.setStyle(TableStyle([
            ('TOPPADDING', (0,0), (-1,-1), 10),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LINEBELOW', (0,0), (-1,-1), 0.5, HexColor('#E5E7EB')),
        ]))
        story.append(rt)

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # INTRODUCCIÓN
    # ═══════════════════════════════════════════════════════════
    story.append(Paragraph("Introducción", ParagraphStyle('intro_h', fontName=FR, fontSize=28, textColor=AZUL_DARK, leading=34, spaceAfter=16)))

    body = ParagraphStyle('b', fontName=F, fontSize=11.5, textColor=MARRON, leading=18, spaceAfter=10)
    body_big = ParagraphStyle('bb', fontName=F, fontSize=12, textColor=MARRON, leading=19, spaceAfter=10)

    story.append(Paragraph(
        "Si estás leyendo esto, probablemente tu perro tiene dificultades para calmarse. "
        "Ladra sin parar cuando tocan el timbre, salta sobre las visitas como si fuera la primera vez que ve a un humano, "
        "jala la correa como si estuviera corriendo un maratón, o se vuelve completamente loco cada vez que "
        "escucha un trueno o fuegos artificiales. Y tú, del otro lado de la correa, ya no sabes qué hacer.", body_big))

    story.append(Paragraph(
        "Antes que nada, necesitas saber algo importante: <b>no es culpa tuya</b>. Nadie nos enseña a ser dueños de perros. "
        "Se supone que \"se sabe\", pero la realidad es que el comportamiento canino tiene ciencia detrás — hay razones "
        "neurológicas y psicológicas para todo lo que hace tu perro. Una vez que las entiendes, todo cambia.", body))

    story.append(Paragraph(
        "Tu perro no es malo ni desobediente. Simplemente nunca aprendió una habilidad fundamental: <b>la calma</b>. "
        "Y la calma no es algo que los perros traen de nacimiento — es una habilidad que se entrena, igual que sentarse o dar la pata. "
        "La diferencia es que la calma cambia TODO: los paseos, las visitas, las noches, la relación completa entre tú y tu compañero.", body))

    box(story,
        "<b>🗓️ Qué esperar en 21 días:</b><br/><br/>"
        "<b><font color='#60B8E8'>Semana 1 (Días 1-7):</font></b> Tu perro empieza a entender que calmarse tiene recompensa. Aprende los fundamentos.<br/><br/>"
        "<b><font color='#2ECC71'>Semana 2 (Días 8-14):</font></b> Aplica la calma en situaciones reales — visitas, ruidos, paseos, comida.<br/><br/>"
        "<b><font color='#FF8C42'>Semana 3 (Días 15-21):</font></b> Mantiene la calma incluso con distracciones fuertes. Nivel avanzado.",
        AZUL_LIGHT, ParagraphStyle('expect', fontName=F, fontSize=11, textColor=MARRON, leading=17))

    # ── CÓMO USAR ESTA GUÍA ──
    story.append(Spacer(1, 16))
    story.append(Paragraph("Cómo usar esta guía", ParagraphStyle('how_h', fontName=FR, fontSize=24, textColor=AZUL_DARK, leading=30, spaceAfter=14)))

    reglas = [
        ("⏱️", "Dedica solo 10-15 minutos al día. No más. Los perros aprenden mucho mejor en sesiones cortas e intensas que en sesiones largas donde se aburren."),
        ("😌", "Siempre entrena cuando tu perro esté tranquilo. Nunca intentes enseñar algo nuevo en medio de una crisis — es como intentar estudiar durante un terremoto."),
        ("🍗", "Usa premios que le ENCANTEN: trocitos de pollo cocido, queso, salchicha. Lo que sea irresistible para él. Los premios aburridos = resultados aburridos."),
        ("🔁", "Si un día no sale bien, repítelo al día siguiente. No hay prisa. Cada perro tiene su ritmo y eso está perfecto."),
        ("❌", "Nunca castigues, grites o jales la correa con fuerza. El castigo destruye la confianza y empeora el comportamiento. Esta guía funciona SIN castigos."),
        ("🎉", "Celebra cada pequeño avance. Si hoy aguantó 3 segundos quieto y ayer aguantó 2, eso es PROGRESO real. Los pequeños pasos construyen grandes cambios."),
    ]
    for emoji, regla in reglas:
        row = [[
            Paragraph(emoji, ParagraphStyle('re', fontName=F, fontSize=20, leading=24)),
            Paragraph(regla, ParagraphStyle('rr', fontName=F, fontSize=11, textColor=MARRON, leading=16)),
        ]]
        rt = Table(row, colWidths=[0.5*inch, W - 0.5*inch])
        rt.setStyle(TableStyle([
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('VALIGN', (0,0), (0,0), 'TOP'),
        ]))
        story.append(rt)

    story.append(Spacer(1, 10))
    box(story,
        "<b>🧰 Materiales que necesitas para empezar:</b><br/><br/>"
        "• <b>Premios irresistibles</b> — trocitos de pollo, queso o salchicha cortados pequeños<br/>"
        "• <b>Una colchoneta o toalla</b> — será el \"lugar de calma\" oficial de tu perro<br/>"
        "• <b>Una correa</b> — para los ejercicios que lo requieran<br/>"
        "• <b>Mucha paciencia</b> — el ingrediente más importante de todos",
        AZUL_DARK, ParagraphStyle('mat', fontName=F, fontSize=11, textColor=BLANCO, leading=17))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # SEMANA 1 — AZUL
    # ═══════════════════════════════════════════════════════════
    S1_COLOR = AZUL_DARK
    S1_LIGHT = AZUL_LIGHT

    section_header(story, 1, "FUNDAMENTOS DE CALMA", S1_COLOR, "🐾")
    story.append(Paragraph(
        "Esta semana tu perro va a aprender que estar tranquilo es la mejor decisión que puede tomar. "
        "No vamos a pedirle nada complicado — solo vamos a premiar cada momento de calma hasta que su cerebro "
        "entienda: <b>\"cuando me quedo quieto, pasan cosas buenas\"</b>. Es la base de todo lo demás.",
        body))

    day_block(story, 1, "EL JUEGO DE LA QUIETUD",
        "Que tu perro entienda que quedarse quieto = premio. Es el concepto más importante de toda la guía.",
        "Premios irresistibles, tu perro con correa, un lugar tranquilo sin distracciones (sala, patio cerrado).",
        [
            "Pon a tu perro con correa en un lugar sin distracciones. No le pidas absolutamente nada. Solo sostenlo.",
            "Espéralo en silencio total. Sin hablarle, sin mirarlo fijamente, sin tocarlo. Solo respira y espera.",
            "En el INSTANTE en que se quede quieto — aunque sea por medio segundo — di '¡Bien!' con entusiasmo y dale un premio inmediatamente.",
            "Repite esto 10 veces. Cada vez, intenta esperar un poquito más: 1 segundo, luego 2, luego 3, luego 5.",
            "Si se mueve o jala, no digas nada. Solo espera. Cuando vuelva a quedarse quieto, premia de nuevo.",
        ],
        "NO le pidas 'siéntate' ni 'échate'. El objetivo es que ÉL decida quedarse quieto por su cuenta. Esa decisión propia es 10 veces más poderosa que una orden.",
        "Tu perro te mira esperando el premio en lugar de jalar, girar o moverse. Ves el momento en que 'entiende el juego'.",
        S1_COLOR, S1_LIGHT)

    day_block(story, 2, "LA COLCHONETA MÁGICA",
        "Crear un lugar físico que tu perro asocie automáticamente con relajarse. Su 'zona zen' personal.",
        "Una colchoneta, toalla o cobija que puedas mover de lugar. Premios de alto valor.",
        [
            "Pon la colchoneta en el suelo. No señales ni le hables. Cuando tu perro la mire o se acerque a investigar, di '¡Bien!' y premia.",
            "Cuando ponga una pata encima, dale DOS premios seguidos. Que sienta que la colchoneta es mágica.",
            "Cuando se suba con las cuatro patas, haz una FIESTA de premios — 5 o 6 seguidos mientras le dices lo increíble que es.",
            "Si se baja, no pasa nada. Espera. Cuando vuelva a subirse, otra fiesta de premios.",
            "Repite hasta que tu perro vaya SOLO a la colchoneta sin que lo guíes. Esto puede tomar 10-20 minutos.",
        ],
        "Esta colchoneta va a ser su 'zona zen' portátil. Con el tiempo, solo ponerla en el suelo le va a decir a su cerebro: es hora de relajarse. La vas a poder llevar a restaurantes, casas de amigos, al vet — a donde sea.",
        "Tu perro va voluntariamente a la colchoneta cuando la ve en el suelo, sin que se lo pidas.",
        S1_COLOR, S1_LIGHT)

    day_block(story, 3, "RESPIRAR Y SOLTAR",
        "Enseñar a tu perro a relajar su cuerpo de forma consciente. Pasar de 'quieto pero tenso' a 'quieto y relajado'.",
        "Colchoneta, premios, ambiente muy tranquilo (sin TV, sin ruido, sin otras personas).",
        [
            "Guía a tu perro a su colchoneta con un premio. Deja que se acomode.",
            "Cuando esté ahí, comienza a acariciarlo suavemente en el pecho (no en la cabeza) con movimientos muy lentos y rítmicos.",
            "Observa su cuerpo con atención. Cada vez que veas que se relaja — baja la cabeza, suspira profundo, se echa, afloja las orejas — di 'Calma' en voz muy baja y dale un premio suavemente.",
            "Si se levanta, no lo regañes. Simplemente deja de acariciar y espera en silencio a que vuelva a su colchoneta.",
        ],
        "Aprende a leer las señales de relajación de tu perro: orejas sueltas (no hacia atrás), cola baja y relajada, ojos medio cerrados, suspiros profundos, boca abierta y suelta. Esas señales significan que su sistema nervioso se está calmando.",
        "Tu perro se echa en la colchoneta y relaja visiblemente su cuerpo cuando lo acaricias. Puedes ver la diferencia entre 'tenso' y 'suelto'.",
        S1_COLOR, S1_LIGHT)

    day_block(story, 4, "CALMA CON DURACIÓN",
        "Aumentar gradualmente el tiempo que tu perro se queda en calma sin necesitar un premio cada segundo.",
        "Colchoneta, premios, un temporizador (puede ser el del celular).",
        [
            "Guía a tu perro a la colchoneta. Espera que se acomode y relaje.",
            "Premia cada 5 segundos que se quede tranquilo. Cuenta mentalmente: 1, 2, 3, 4, 5 → premio.",
            "Después de 5 repeticiones exitosas, sube a 10 segundos. Luego 15. Luego 20. Luego 30.",
            "Si se levanta antes de tiempo, no pasa nada. Sin drama. Vuelve al último intervalo que funcionó y quédate ahí un rato más.",
            "Objetivo de la sesión: llegar a 1 minuto completo en calma sin necesitar premio constante.",
        ],
        "Si tu perro se frustra o se levanta seguido, estás yendo demasiado rápido. Baja el tiempo a donde sí funcione y sube más despacio. Es como un músculo — se fortalece con repetición, no con fuerza.",
        "Tu perro se queda en la colchoneta al menos 1 minuto seguido sin levantarse ni quejarse.",
        S1_COLOR, S1_LIGHT)

    day_block(story, 5, "CALMA MIENTRAS TE MUEVES",
        "Que tu perro mantenga la calma en su colchoneta aunque tú te muevas por la habitación.",
        "Colchoneta, premios de alto valor.",
        [
            "Tu perro en la colchoneta, relajado. Da UN paso hacia atrás, lentamente.",
            "Si se queda en la colchoneta, vuelve inmediatamente y prémialo con entusiasmo. Si se levanta, sin drama — regresa y espera a que se acomode de nuevo.",
            "Aumenta gradualmente: 2 pasos atrás, 3 pasos, pasos a los lados, pasos en diagonal.",
            "Intenta caminar alrededor de la colchoneta en un círculo completo. Si lo logras, premio triple.",
        ],
        "No lo mires fijamente a los ojos mientras te mueves — la mirada directa les genera ansiedad y ganas de seguirte. Muévete con naturalidad, como si estuvieras haciendo cosas normales de tu casa.",
        "Puedes dar 5 pasos en cualquier dirección y tu perro sigue tranquilo en su colchoneta, mirándote pero sin levantarse.",
        S1_COLOR, S1_LIGHT)

    day_block(story, 6, "CALMA CON DISTANCIA",
        "Que tu perro mantenga la calma aunque te alejes de la habitación por algunos segundos.",
        "Colchoneta, premios, una habitación con puerta.",
        [
            "Tu perro en la colchoneta. Aléjate 2 metros. Espera 5 segundos. Vuelve y premia.",
            "Sube a 3 metros. Luego 4. Intenta llegar hasta la puerta de la habitación.",
            "Da un paso fuera de la habitación y regresa inmediatamente. Si se quedó, premio gordo.",
            "Aumenta gradualmente: 3 segundos fuera, 5 segundos, 10 segundos. Siempre vuelve TÚ a él — no esperes a que venga.",
        ],
        "El secreto es volver ANTES de que se levante. Así su cerebro aprende: 'cada vez que me quedo aquí, mi humano siempre vuelve y me da algo rico'. Eso construye confianza.",
        "Puedes salir de la habitación 10 segundos y cuando vuelves, tu perro sigue en su colchoneta esperándote.",
        S1_COLOR, S1_LIGHT)

    day_block(story, 7, "DÍA DE REPASO — CELEBRACIÓN",
        "Consolidar todo lo aprendido esta semana y celebrar el progreso increíble de tu perro.",
        "Colchoneta, los MEJORES premios que tengas (hoy es día especial), buen ánimo.",
        [
            "Haz una sesión de 15 minutos combinando TODOS los ejercicios: quietud, colchoneta, duración, movimiento y distancia.",
            "Empieza por lo más fácil y ve subiendo la dificultad gradualmente.",
            "Toma nota mental o escrita: ¿qué funciona bien? ¿Dónde necesita más práctica?",
            "Celebra TODO lo que logró esta semana. Dale un premio extra especial al final. Él se lo ganó, y tú también.",
        ],
        "Si algo no salió perfecto esta semana, es completamente NORMAL. Los perros no son máquinas — tienen días buenos y días regulares, igual que nosotros. Repite los días que necesites antes de pasar a la semana 2. No hay prisa.",
        "Tu perro va a su colchoneta voluntariamente, se queda al menos 1 minuto, y no se levanta cuando te mueves o te alejas.",
        S1_COLOR, S1_LIGHT)

    box(story,
        "<b>🎉 ¡Felicidades por completar la Semana 1!</b><br/><br/>"
        "Si llegaste hasta aquí, tu perro ya tiene los fundamentos de calma instalados en su cerebro. "
        "Eso es ENORME. La semana 2 va a ser emocionante: vamos a llevar esta calma al mundo real — "
        "visitas, timbre, paseos, ruidos y más.",
        AMARILLO, ParagraphStyle('w1end', fontName=FB, fontSize=12, textColor=MARRON, leading=17, alignment=TA_CENTER))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # SEMANA 2 — VERDE
    # ═══════════════════════════════════════════════════════════
    S2_COLOR = VERDE_DARK
    S2_LIGHT = VERDE_LIGHT

    section_header(story, 2, "CALMA EN EL MUNDO REAL", S2_COLOR, "🏠")
    story.append(Paragraph(
        "Tu perro ya sabe calmarse en un ambiente controlado. ¡Excelente! Ahora viene lo bueno: vamos a ponerlo "
        "a prueba con las situaciones que más te complican el día a día. Cada día de esta semana ataca un escenario "
        "específico que probablemente te está volviendo loca.",
        body))

    day_block(story, 8, "CALMA CUANDO SUENA EL TIMBRE",
        "Que tu perro deje de explotar cada vez que alguien toca la puerta. En vez de lanzarse ladrando, que vaya a su colchoneta.",
        "Colchoneta colocada a 3 metros de la puerta principal, premios de alto valor, un ayudante que pueda tocar el timbre desde afuera.",
        [
            "Coloca la colchoneta a unos 3 metros de la puerta, donde tu perro pueda verla fácilmente.",
            "Pide a tu ayudante que toque el timbre una vez, de forma suave (no el timbrazo completo).",
            "Tu perro va a reaccionar — ladrando, corriendo, saltando. Espera. No le digas nada. Simplemente espera.",
            "En el SEGUNDO en que muestre cualquier señal de calma (deja de ladrar, te mira, baja la intensidad), di '¡Bien!' y dale un premio increíble.",
            "Repite. Cada vez que suena el timbre y él decide calmarse, premio gordo. El objetivo final: que cuando suene el timbre, vaya a la colchoneta en vez de a la puerta.",
        ],
        "Empieza con toques muy suaves al timbre — tal vez solo un golpecito en la puerta. Si tu perro se descontrola completamente, el estímulo es demasiado fuerte. Baja la intensidad hasta que pueda procesarlo.",
        "Tu perro escucha el timbre, te mira (o mira hacia la colchoneta) en vez de lanzarse como loco a la puerta.",
        S2_COLOR, S2_LIGHT)

    day_block(story, 9, "CALMA CON VISITAS",
        "Que tu perro no salte, ladre ni pierda el control cuando llegan personas a tu casa.",
        "Colchoneta, premios, una persona que pueda visitarte y que esté dispuesta a seguir las instrucciones.",
        [
            "Antes de que llegue la visita, guía a tu perro a la colchoneta y dale un par de premios para que esté contento ahí.",
            "La visita entra y lo IGNORA completamente. Esto es clave: no lo mira, no lo toca, no le habla, no dice 'ay qué lindo'. Cero atención.",
            "Tú premias a tu perro cada vez que se quede en la colchoneta o muestre calma. Eres su fuente de atención, no la visita.",
            "SOLO cuando tu perro esté completamente calmado (4 patas en el suelo, sin ladrar, respiración normal), la visita puede agacharse y saludarlo suavemente.",
        ],
        "La regla de oro que debes explicarle a toda visita: NO pueden saludar, tocar ni mirar al perro si está saltando o ladrando. Cero atención hasta que esté calmado. Esto solo cambia las reglas del juego completamente.",
        "Tu perro se queda en su colchoneta mientras la visita entra a la casa, y solo se acerca cuando está tranquilo.",
        S2_COLOR, S2_LIGHT)

    day_block(story, 10, "CALMA CON RUIDOS FUERTES",
        "Desensibilizar gradualmente a tu perro a los ruidos que lo estresan o asustan (truenos, fuegos artificiales, aspiradora, etc).",
        "Tu celular con acceso a YouTube (busca: 'dog desensitization sounds'), premios de muy alto valor.",
        [
            "Pon a tu perro en su colchoneta en un ambiente tranquilo y familiar.",
            "Reproduce el sonido que lo asusta en tu celular, pero en volumen MUY bajo — que apenas se escuche. Casi en silencio.",
            "Mientras el sonido suena, dale premios de forma continua. Que asocie: sonido = lluvia de premios.",
            "Si está tranquilo, sube el volumen UN punto. Solo uno. Si muestra cualquier señal de estrés (jadea, tiembla, orejas hacia atrás), baja el volumen inmediatamente.",
        ],
        "NUNCA fuerces a tu perro a escuchar algo que lo aterroriza. La desensibilización funciona SOLO si el perro está por debajo de su umbral de estrés. Si lo pasas, en vez de desensibilizar estás traumatizando. Paciencia.",
        "Tu perro escucha el sonido a volumen moderado sin mostrar señales de estrés — no tiembla, no jadea, no intenta esconderse.",
        S2_COLOR, S2_LIGHT)

    day_block(story, 11, "CALMA EN EL PASEO — SALIR DE CASA",
        "Que tu perro pueda salir de casa sin convertirse en un tornado de emoción. Que el momento de 'sacar a pasear' no sea un caos.",
        "Correa, premios, la puerta de tu casa, y unos 20 minutos de paciencia.",
        [
            "Toma la correa. Si tu perro se vuelve completamente loco (salta, gira, ladra, llora), SUELTA la correa en el suelo y quédate quieta. Sin hablarle.",
            "Espera a que se calme. Cuando lo haga, vuelve a tomar la correa. Si se vuelve loco otra vez, la sueltas otra vez. Sin drama.",
            "Repite hasta que puedas tomar la correa Y ponérsela sin que pierda el control.",
            "Ahora lo mismo con la puerta: pones la mano en la manija → si se lanza, quitas la mano. Si espera tranquilo, abres la puerta. Si se lanza, cierras. Abres de nuevo cuando esté calmado.",
        ],
        "Este ejercicio puede tomar 20-30 minutos la primera vez, y es frustrante. Pero estás rompiendo un hábito de meses o años. Cada segundo que inviertas aquí te ahorra semanas de jalones en la calle.",
        "Puedes tomar la correa, ponérsela y abrir la puerta sin que tu perro salte, gire, ladre o llore de emoción.",
        S2_COLOR, S2_LIGHT)

    day_block(story, 12, "CALMA EN EL PASEO — CAMINAR SIN JALAR",
        "Que tu perro camine a tu lado con la correa suelta, sin arrastrarte por toda la cuadra.",
        "Correa de longitud fija (NO retráctil), premios en tu bolsillo, una calle o acera tranquila.",
        [
            "Sal a la calle. En el momento en que tu perro jale la correa, PARA completamente. No digas nada. No jales. Solo para como una estatua.",
            "Espera. Cuando la correa se afloje — aunque sea porque se detuvo confundido — di '¡Bien!' con entusiasmo y avanza.",
            "Cada vez que camine a tu lado con la correa suelta (aunque sea 3 pasos), premia generosamente.",
            "Si ve algo que lo excita mucho (otro perro, un gato, comida en el suelo), para y espera a que te mire a ti en vez de mirar el estímulo. Cuando te mire, premio triple.",
        ],
        "Los primeros paseos con esta técnica van a ser MUY lentos. Tal vez camines media cuadra en 20 minutos. Eso es completamente normal y necesario. Estás reprogramando un hábito muy arraigado.",
        "Puedes caminar media cuadra completa sin que tu perro jale la correa ni una sola vez.",
        S2_COLOR, S2_LIGHT)

    day_block(story, 13, "CALMA CON LA COMIDA",
        "Que tu perro no pierda absolutamente el control a la hora de comer. Que espere con calma antes de lanzarse al plato.",
        "Su plato de comida habitual, premios extra especiales.",
        [
            "Prepara su comida como siempre. Si empieza a saltar, ladrar o empujarte, SUBE el plato por encima de tu cabeza y quédate completamente quieta.",
            "Cuando se calme (se sienta, deja de ladrar, o simplemente se queda quieto), baja el plato lentamente.",
            "Si se mueve o salta cuando bajas el plato, súbelo de nuevo. Sin hablarle. Sin regañarlo. Solo sube el plato.",
            "Repite hasta que puedas poner el plato en el suelo con tu perro sentado o quieto. Antes de soltarlo, espera 3 segundos y luego di 'Adelante' para que coma.",
        ],
        "Esto no es ser cruel — es enseñarle la lección más poderosa que existe: la calma le da acceso a TODO lo que quiere. Comida, paseos, atención, juego — todo viene cuando está calmado.",
        "Tu perro se sienta y espera con paciencia a que pongas el plato en el suelo. Solo come cuando le das la señal.",
        S2_COLOR, S2_LIGHT)

    day_block(story, 14, "DÍA DE REPASO — SEMANA 2",
        "Consolidar la calma en todas las situaciones reales que trabajaste esta semana. Identificar puntos fuertes y débiles.",
        "Todos los materiales de la semana, los mejores premios, y honestidad contigo misma sobre qué funciona y qué no.",
        [
            "Haz un recorrido mental o práctico por todos los escenarios: timbre, visitas, ruidos, salir de casa, paseo, comida.",
            "Identifica cuál de estos escenarios todavía necesita más trabajo. Sé honesta.",
            "Dedica 10 minutos extra a practicar ese escenario específico.",
            "Anota o recuerda: ¿dónde estaba tu perro el Día 1 vs. dónde está hoy? Esa diferencia es TU logro.",
        ],
        "Si un escenario todavía está difícil, no te preocupes ni te frustres. Repite esos días las veces que necesites antes de avanzar a la semana 3. Mejor lento y sólido que rápido y frágil.",
        "Tu perro maneja al menos 3 de los 5 escenarios de esta semana con calma visible y real.",
        S2_COLOR, S2_LIGHT)

    box(story,
        "<b>🔥 ¡Increíble! Completaste la Semana 2.</b><br/><br/>"
        "Tu perro ya sabe calmarse en situaciones reales del día a día. Eso lo pone por encima del 90% de los perros "
        "que nunca reciben este tipo de entrenamiento. La semana 3 es el nivel final: calma bajo presión máxima.",
        VERDE, ParagraphStyle('w2end', fontName=FB, fontSize=12, textColor=BLANCO, leading=17, alignment=TA_CENTER))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # SEMANA 3 — NARANJA
    # ═══════════════════════════════════════════════════════════
    S3_COLOR = NARANJA_DARK
    S3_LIGHT = NARANJA_LIGHT

    section_header(story, 3, "CALMA AVANZADA", S3_COLOR, "🏆")
    story.append(Paragraph(
        "Tu perro ya tiene los fundamentos y sabe aplicarlos en situaciones reales. Esta semana vamos a hacerlo "
        "<b>a prueba de todo</b>: otros perros, lugares nuevos, niños, el carro, tu ausencia, y distracciones múltiples. "
        "Cuando termines esta semana, vas a tener un perro diferente.",
        body))

    day_block(story, 15, "CALMA CON OTROS PERROS",
        "Que tu perro se mantenga tranquilo cuando ve a otro perro, en vez de jalar, ladrar o volverse loco de emoción.",
        "Correa, premios de altísimo valor (pollo es ideal), un parque o calle donde pasen perros A DISTANCIA.",
        [
            "Ubícate a una distancia donde tu perro pueda VER al otro perro pero NO reaccione. Puede ser 20 metros, puede ser 50. Esa es la distancia correcta para TU perro.",
            "Cada vez que vea pasar un perro y te mire a TI (en vez de jalar o ladrar hacia el otro perro), dale el mejor premio que tengas. Haz fiesta.",
            "Si reacciona (ladra, jala, se tensa), estás demasiado cerca. Aléjate más sin drama.",
            "En sesiones posteriores (no el mismo día), reduce la distancia poco a poco. 50 metros → 40 → 30 → 20.",
        ],
        "La DISTANCIA es tu mejor herramienta y tu mejor amiga. Si tu perro está reaccionando, estás demasiado cerca. Así de simple. No intentes forzar encuentros cercanos todavía — eso vendrá con el tiempo.",
        "Tu perro ve otro perro a 10-15 metros y te mira a ti en vez de jalar o ladrar hacia el otro perro.",
        S3_COLOR, S3_LIGHT)

    day_block(story, 16, "CALMA EN LUGARES NUEVOS",
        "Generalizar la calma a ambientes que tu perro no conoce. Que sepa calmarse en CUALQUIER lugar, no solo en casa.",
        "Colchoneta portátil (la misma de siempre), premios, un lugar nuevo pero no demasiado intenso (un café tranquilo, la casa de un amigo, un parque poco concurrido).",
        [
            "Lleva la colchoneta al lugar nuevo y ponla en el suelo. No fuerces a tu perro a hacer nada — deja que explore un poco primero.",
            "Cuando esté listo, guíalo a la colchoneta con un premio. Espera a que la reconozca y se suba voluntariamente.",
            "Premia generosamente cada segundo de calma. En un lugar nuevo, la calma vale el doble.",
            "Quédense ahí 5-10 minutos. Si el lugar es muy estimulante, empieza con lugares menos intensos y ve subiendo.",
        ],
        "La colchoneta es como un ancla de calma portátil. Donde la pongas, tu perro sabe que ahí se relaja. Es su pedacito de 'casa' en cualquier lugar del mundo.",
        "Tu perro se echa en la colchoneta en un lugar completamente nuevo y se relaja en menos de 2-3 minutos.",
        S3_COLOR, S3_LIGHT)

    day_block(story, 17, "CALMA CON NIÑOS",
        "Que tu perro mantenga la compostura cerca de niños ruidosos, que corren y gritan (el estímulo más difícil para muchos perros).",
        "Colchoneta, premios de alto valor, niños cooperadores (si los tienes) o videos de YouTube de niños jugando.",
        [
            "Si no tienes niños disponibles, busca en YouTube 'kids playing loudly' y usa el video como herramienta de desensibilización.",
            "Tu perro en la colchoneta. Reproduce el video a volumen bajo. Premia cada segundo de calma.",
            "Sube el volumen gradualmente. Si muestra estrés, baja.",
            "Con niños reales: misma lógica — colchoneta, distancia segura, premio constante por calma. Los niños no deben acercarse al perro hasta que esté completamente relajado.",
        ],
        "Regla #1 absoluta e innegociable: NUNCA dejes a un perro y un niño juntos sin supervisión adulta directa, sin importar lo calmado o entrenado que sea el perro. Nunca. Jamás.",
        "Tu perro escucha ruidos de niños jugando sin levantarse de la colchoneta ni mostrar señales de estrés o ansiedad.",
        S3_COLOR, S3_LIGHT)

    day_block(story, 18, "CALMA EN EL CARRO",
        "Que tu perro viaje tranquilo en el carro sin llorar, vomitar, temblar o destruir los asientos.",
        "Colchoneta, premios, tu carro ESTACIONADO (no vamos a manejar todavía).",
        [
            "Pon la colchoneta en el asiento trasero. Sube al perro con calma y premia que esté tranquilo. Sin encender el motor.",
            "Quédense ahí 5 minutos. Solo estar. Premia cada momento de calma.",
            "Sesión 2 (puede ser más tarde ese día): enciende el carro SIN moverte. Motor encendido, carro quieto. Premia calma.",
            "Sesión 3: maneja UNA cuadra. Para. Premia. Regresa. Aumenta la distancia gradualmente en los siguientes días.",
        ],
        "Si tu perro vomita en el carro, en el 90% de los casos es estrés, NO mareo. La desensibilización lenta y gradual resuelve la gran mayoría de estos casos. No lo fuerces a viajes largos antes de estar listo.",
        "Tu perro se sube al carro, se echa en la colchoneta y se queda tranquilo mientras manejas 10 minutos sin drama.",
        S3_COLOR, S3_LIGHT)

    day_block(story, 19, "CALMA CUANDO TE VAS DE CASA",
        "Reducir la ansiedad de separación para que tu perro no destruya, ladre ni llore cuando te vas.",
        "Premios, la colchoneta en su lugar habitual, tus llaves, zapatos, y tu rutina normal de salida.",
        [
            "Haz toda tu rutina de salida (tomar llaves, ponerte zapatos, agarrar bolso) pero NO te vayas. Siéntate en el sofá. Repite esto 5 veces seguidas.",
            "Tu perro va a dejar de reaccionar a esas señales porque ya no predicen que te vas. Eso es exactamente lo que queremos.",
            "Cuando ya no reaccione a la rutina, abre la puerta, sal 10 segundos y vuelve a entrar. Sin drama al irte. Sin fiesta al volver. Como si fueras al baño.",
            "Aumenta gradualmente: 30 segundos, 1 minuto, 3 minutos, 5 minutos, 15 minutos afuera.",
        ],
        "La clave es NO hacer drama al irte ni al volver. Nada de 'ay mi bebé, ya vengo, pórtate bien, te quiero mucho'. Sales tranquila, vuelves tranquila. El drama alimenta la ansiedad.",
        "Puedes salir de casa 15-20 minutos y tu perro no ladra, no destruye nada y no llora.",
        S3_COLOR, S3_LIGHT)

    day_block(story, 20, "CALMA BAJO PRESIÓN MÁXIMA",
        "El examen final: combinar múltiples distracciones al mismo tiempo y que tu perro mantenga la compostura.",
        "Colchoneta portátil, los mejores premios que existan, un lugar con varias distracciones simultáneas (parque concurrido, mercado, zona comercial).",
        [
            "Lleva a tu perro a un lugar con varias distracciones: gente caminando, otros perros, ruidos, olores nuevos — todo junto.",
            "Pon la colchoneta en un lugar donde puedas sentarte. Prémialo por ir a ella y quedarse.",
            "Premia cada 5 segundos de calma al principio. Reduce gradualmente la frecuencia a medida que se relaje.",
            "Si se satura (demasiado para él), aléjate a un lugar más tranquilo, recalibra, y vuelve a intentar.",
        ],
        "Este es el examen final. NO esperes perfección — espera progreso. Si tu perro se queda 30 segundos calmado en un lugar donde antes hubiera durado 0 segundos, eso es un ÉXITO enorme. Celebra el progreso, no la perfección.",
        "Tu perro se mantiene en la colchoneta al menos 2 minutos en un ambiente con distracciones moderadas a fuertes.",
        S3_COLOR, S3_LIGHT)

    day_block(story, 21, "CELEBRACIÓN Y PLAN DE MANTENIMIENTO",
        "Consolidar todo lo aprendido, celebrar el increíble progreso, y crear un plan simple de mantenimiento para toda la vida.",
        "Todos los materiales, tu perro, los mejores premios del mundo, y mucho orgullo.",
        [
            "Haz un recorrido por los mejores ejercicios de cada semana. Disfrútalo — este es TU logro tanto como el de tu perro.",
            "Identifica los 3 escenarios donde tu perro MÁS mejoró. Celébralos. Escríbelos. Recuérdalos cuando tengas un día difícil.",
            "Identifica los 2 escenarios que todavía necesitan trabajo. Esos serán tu foco las próximas semanas — repite esos días específicos.",
            "A partir de hoy: practica 5 minutos diarios de calma en la colchoneta. Solo 5 minutos. Eso es todo lo que necesitas para mantener lo aprendido para siempre.",
        ],
        "El entrenamiento formal termina hoy — pero la relación que construiste con tu perro en estos 21 días es para toda la vida. Lo más difícil ya pasó. Ahora es solo mantenimiento: 5 minutos al día.",
        "Tu perro demuestra calma en la mayoría de situaciones cotidianas. La relación entre ustedes es visiblemente más fuerte y tranquila.",
        S3_COLOR, S3_LIGHT)

    box(story,
        "<b>🏆 ¡Completaste las 3 semanas!</b> Tu perro ahora tiene herramientas reales para manejar "
        "el estrés, las distracciones y la emoción. Eso lo cambia TODO.",
        NARANJA, ParagraphStyle('w3end', fontName=FB, fontSize=12, textColor=BLANCO, leading=17, alignment=TA_CENTER))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # EMERGENCIAS
    # ═══════════════════════════════════════════════════════════
    story.append(Paragraph("🆘 Emergencias", ParagraphStyle('em_h', fontName=FR, fontSize=28, textColor=ROJO_SOFT, leading=34, spaceAfter=6)))
    story.append(Paragraph("Qué hacer cuando algo no funciona como esperabas", ParagraphStyle('em_sub', fontName=FI, fontSize=13, textColor=GRIS, leading=18, spaceAfter=20)))

    emergencias = [
        ("Mi perro no acepta premios durante el ejercicio",
         "Está demasiado estresado para comer. Cuando un perro rechaza comida, su cerebro está en modo supervivencia y no puede aprender nada. <b>Solución:</b> baja muchísimo la intensidad — más distancia del estímulo, menos distracciones, un lugar más tranquilo. Cuando acepte premios otra vez, estás en la zona correcta.",
         ROJO_SOFT),
        ("Llevo varios días y no veo ningún progreso",
         "Algunos perros tardan 5-7 días en 'hacer clic'. El aprendizaje canino no es lineal — puede parecer que no pasa nada y de repente todo conecta. <b>Solución:</b> sigue con consistencia absoluta. Si después de 7 días no hay ningún cambio visible, vuelve al Día 1 con sesiones más cortas (5 minutos máximo).",
         NARANJA),
        ("Mi perro parece empeorar cuando practicamos",
         "Estás avanzando demasiado rápido para su nivel actual. Es como ponerle un examen de universidad a un niño de primaria — se frustra y se cierra. <b>Solución:</b> vuelve al último día donde todo funcionaba bien y quédate ahí 3-5 días más antes de intentar avanzar.",
         AMARILLO),
        ("En casa funciona perfecto pero afuera es un desastre",
         "Completamente normal y esperado. Afuera hay literalmente 100 veces más estímulos que dentro de tu casa. <b>Solución:</b> empieza los ejercicios de afuera a MUCHA distancia de cualquier distracción y en el momento más tranquilo del día. Ve acercándote gradualmente.",
         VERDE),
    ]

    for titulo, texto, color in emergencias:
        box(story, f"<b>{titulo}</b>", color,
            ParagraphStyle('emt', fontName=FB, fontSize=13, textColor=BLANCO, leading=18))
        story.append(Paragraph(texto, ParagraphStyle('emb', fontName=F, fontSize=11, textColor=MARRON, leading=17, spaceAfter=14)))

    # Aviso especial de agresividad — más grande y visible
    story.append(Spacer(1, 10))
    warn_data = [[Paragraph(
        "<b>IMPORTANTE: SI TU PERRO MUESTRA AGRESIVIDAD REAL</b><br/><br/>"
        "Si tu perro gruñe, muestra los dientes o ha mordido a alguien, esta guía puede complementar "
        "el trabajo de un profesional, pero <b>NO debe ser tu única herramienta</b>.<br/><br/>"
        "La agresividad requiere evaluación presencial individualizada por un etólogo o adiestrador "
        "certificado en tu ciudad. La seguridad de tu familia y tu perro es lo primero.",
        ParagraphStyle('warn', fontName=F, fontSize=13, textColor=BLANCO, leading=20, alignment=TA_CENTER))]]
    wt = Table(warn_data, colWidths=[W])
    wt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#C0392B')),
        ('ROUNDEDCORNERS', [14, 14, 14, 14]),
        ('TOPPADDING', (0,0), (-1,-1), 22),
        ('BOTTOMPADDING', (0,0), (-1,-1), 22),
        ('LEFTPADDING', (0,0), (-1,-1), 22),
        ('RIGHTPADDING', (0,0), (-1,-1), 22),
    ]))
    story.append(wt)

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # FELICITACIONES FINAL
    # ═══════════════════════════════════════════════════════════
    story.append(Spacer(1, 0.3*inch))

    final_content = Paragraph(
        "<b><font size='36' color='#F7D44C'>FELICIDADES</font></b><br/><br/>"
        "<font size='16'><b>Completaste la Guía Zen de AZUL</b></font><br/><br/>"
        "- - - - - - - - - - - - - - -<br/><br/>"
        "Llegaste hasta el final. Eso dice más de ti como dueño de lo que "
        "cualquier certificado podría decir. Tu perro hoy es más calmado, "
        "más seguro y más feliz gracias a tu paciencia y tu amor.<br/><br/>"
        "<i>En 21 días construiste algo que muchos dueños nunca logran: "
        "una relación basada en confianza, no en miedo. "
        "En comunicación, no en gritos. En calma, no en caos.</i><br/><br/>"
        "- - - - - - - - - - - - - - -<br/><br/>"
        "<b><font size='15' color='#F7D44C'>Tu perro te eligió a ti.<br/>"
        "Y hoy, tú elegiste ser la mejor versión de su humano.</font></b><br/><br/><br/>"
        "<i>Con amor,</i><br/>"
        "<b>El equipo AZUL</b><br/><br/>"
        "<font color='#F7D44C'><b>azulapp.org</b></font>",
        ParagraphStyle('final', fontName=F, fontSize=13, textColor=BLANCO, alignment=TA_CENTER, leading=20))

    ft = Table([[final_content]], colWidths=[6.8*inch])
    ft.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), MORADO),
        ('ROUNDEDCORNERS', [20, 20, 20, 20]),
        ('TOPPADDING', (0,0), (-1,-1), 40),
        ('BOTTOMPADDING', (0,0), (-1,-1), 40),
        ('LEFTPADDING', (0,0), (-1,-1), 30),
        ('RIGHTPADDING', (0,0), (-1,-1), 30),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(ft)

    doc.build(story)
    print("✅ PDF generado exitosamente!")

if __name__ == '__main__':
    build_pdf()
