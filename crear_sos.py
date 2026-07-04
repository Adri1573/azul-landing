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

# Colores
ROJO = HexColor('#E74C3C')
ROJO_DARK = HexColor('#C0392B')
ROJO_LIGHT = HexColor('#FDEDEC')
AZUL = HexColor('#60B8E8')
AZUL_DARK = HexColor('#2B8CC4')
VERDE = HexColor('#2ECC71')
VERDE_LIGHT = HexColor('#E8F8F0')
NARANJA = HexColor('#FF8C42')
NARANJA_LIGHT = HexColor('#FFF3EB')
MORADO = HexColor('#9B59B6')
MORADO_LIGHT = HexColor('#F5EEFF')
AMARILLO = HexColor('#F7D44C')
AMARILLO_DARK = HexColor('#D4A017')
AMARILLO_LIGHT = HexColor('#FFF9E6')
MARRON = HexColor('#2C1810')
CREMA = HexColor('#F5EAD6')
GRIS = HexColor('#6B7280')
BLANCO = HexColor('#FFFFFF')
CORAL = HexColor('#FF6B6B')
CORAL_LIGHT = HexColor('#FFE8E8')
TEAL = HexColor('#1ABC9C')
TEAL_LIGHT = HexColor('#E8FDF5')
ROSA = HexColor('#E84393')
ROSA_LIGHT = HexColor('#FDE8F4')

W = 6.5 * inch

body = ParagraphStyle('b', fontName=F, fontSize=11.5, textColor=MARRON, leading=18, spaceAfter=10)

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

def problema_block(story, num, titulo, emoji, color, color_light, por_que, pasos, script, error, senal):
    elements = []

    # Header
    hdr = [[Paragraph(f"PROBLEMA #{num}  |  {emoji} {titulo}", ParagraphStyle('ph', fontName=FB, fontSize=17, textColor=BLANCO, leading=22))]]
    ht = Table(hdr, colWidths=[W])
    ht.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('ROUNDEDCORNERS', [12, 12, 0, 0]),
        ('TOPPADDING', (0,0), (-1,-1), 16),
        ('BOTTOMPADDING', (0,0), (-1,-1), 16),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
    ]))
    elements.append(ht)

    # Por qué
    why_parts = []
    why_parts.append(Paragraph(f"<b><font color='{color.hexval()}'> Qué pasa en su cabeza:</font></b>", ParagraphStyle('wh', fontName=FB, fontSize=13, textColor=color, leading=18, spaceAfter=6)))
    why_parts.append(Paragraph(por_que, ParagraphStyle('wp', fontName=F, fontSize=11, textColor=MARRON, leading=16, spaceAfter=12)))

    # Protocolo
    why_parts.append(Paragraph(f"<b><font color='{color.hexval()}'> Protocolo SOS (48h):</font></b>", ParagraphStyle('pr', fontName=FB, fontSize=13, textColor=color, leading=18, spaceAfter=6)))
    for i, paso in enumerate(pasos, 1):
        why_parts.append(Paragraph(f"<b>Paso {i}.</b> {paso}", ParagraphStyle(f'ps{i}', fontName=F, fontSize=11, textColor=MARRON, leading=16, spaceAfter=5, leftIndent=16)))

    why_content = [[p] for p in why_parts]
    wt = Table(why_content, colWidths=[W - 36])
    wt.setStyle(TableStyle([('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0),
                             ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))

    body_wrap = [[wt]]
    bw = Table(body_wrap, colWidths=[W])
    bw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color_light),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
    ]))
    elements.append(bw)

    # Script
    sc_data = [[Paragraph(f"<b> Script exacto:</b> {script}", ParagraphStyle('sc', fontName=F, fontSize=11, textColor=MARRON, leading=16))]]
    sc_t = Table(sc_data, colWidths=[W])
    sc_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CREMA),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
    ]))
    elements.append(sc_t)

    # Error #1
    er_data = [[Paragraph(f"<b> Error #1 que cometen los dueños:</b> {error}", ParagraphStyle('er', fontName=F, fontSize=10, textColor=HexColor('#C0392B'), leading=15))]]
    er_t = Table(er_data, colWidths=[W])
    er_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), ROJO_LIGHT),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 18),
        ('RIGHTPADDING', (0,0), (-1,-1), 18),
    ]))
    elements.append(er_t)

    # Señal de éxito
    ex_data = [[Paragraph(f"<b> Señal de que funciona:</b> {senal}", ParagraphStyle('ex', fontName=F, fontSize=10, textColor=HexColor('#1FAF5C'), leading=15))]]
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
        "/Users/nana1516/azul-landing/sos-comportamiento.pdf",
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
        [Paragraph("SOS", ParagraphStyle('b3', fontName=FR, fontSize=56, textColor=BLANCO, alignment=TA_CENTER, leading=64))],
        [Paragraph("COMPORTAMIENTO", ParagraphStyle('b3b', fontName=FB, fontSize=22, textColor=AMARILLO, alignment=TA_CENTER, leading=28))],
        [Spacer(1, 10)],
        [Paragraph("Soluciones en 48 horas", ParagraphStyle('b4', fontName=FR, fontSize=28, textColor=BLANCO, alignment=TA_CENTER, leading=36))],
        [Spacer(1, 20)],
        [Paragraph("Guía urgente para los 9 problemas de\ncomportamiento más comunes en perros", ParagraphStyle('b5', fontName=F, fontSize=13, textColor=HexColor('#FFFFFFCC'), alignment=TA_CENTER, leading=20))],
        [Spacer(1, 20)],
        [Paragraph("Scripts exactos  ·  Sin castigos  ·  Resultados reales", ParagraphStyle('b6', fontName=FB, fontSize=11, textColor=BLANCO, alignment=TA_CENTER, leading=16))],
        [Spacer(1, 16)],
        [Paragraph("azulapp.org", ParagraphStyle('b8', fontName=FB, fontSize=14, textColor=AMARILLO, alignment=TA_CENTER))],
    ]

    ct = Table([[item[0]] for item in cover_items], colWidths=[6.8*inch])
    ct.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), ROJO_DARK),
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
    story.append(Paragraph("ÍNDICE", ParagraphStyle('idx', fontName=FR, fontSize=32, textColor=ROJO_DARK, alignment=TA_CENTER, leading=40)))
    story.append(Paragraph("9 problemas, 9 soluciones inmediatas", ParagraphStyle('idx2', fontName=FI, fontSize=13, textColor=GRIS, alignment=TA_CENTER, leading=18, spaceAfter=24)))

    problemas_idx = [
        ("1", "Ladrido excesivo", "Protocolo silencio en 3 pasos", CORAL),
        ("2", "Morder / mordisquear", "Técnica de redirección", NARANJA),
        ("3", "Jalar la correa", "Método estatua", AZUL_DARK),
        ("4", "Ansiedad de separación", "Plan de desensibilización", MORADO),
        ("5", "Saltar sobre personas", "Protocolo 4 patas en el suelo", VERDE),
        ("6", "Agresividad con otros perros", "Control a distancia", ROJO),
        ("7", "No obedecer 'ven'", "Recall infalible", TEAL),
        ("8", "Destrucción en casa", "Protocolo anti-destrucción", ROSA),
        ("9", "Llanto y lloriqueo excesivo", "Protocolo de calma emocional", AMARILLO_DARK),
    ]

    for num, title, sub, color in problemas_idx:
        row = [[
            Paragraph(f"<b>{num}</b>", ParagraphStyle('in', fontName=FR, fontSize=24, textColor=BLANCO, alignment=TA_CENTER, leading=30)),
            Paragraph(f"<b>{title}</b><br/><font size='10' color='#6B7280'>{sub}</font>", ParagraphStyle('it', fontName=F, fontSize=14, textColor=MARRON, leading=20)),
        ]]
        num_cell = Table([[Paragraph(f"<b>{num}</b>", ParagraphStyle(f'nc{num}', fontName=FR, fontSize=20, textColor=BLANCO, alignment=TA_CENTER, leading=26))]], colWidths=[0.5*inch], rowHeights=[0.45*inch])
        num_cell.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), color),
            ('ROUNDEDCORNERS', [8, 8, 8, 8]),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ]))

        rt = Table([[num_cell, Paragraph(f"<b>{title}</b><br/><font size='10' color='#6B7280'>{sub}</font>", ParagraphStyle(f'tt{num}', fontName=F, fontSize=13, textColor=MARRON, leading=19))]], colWidths=[0.7*inch, W - 0.7*inch])
        rt.setStyle(TableStyle([
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LINEBELOW', (0,0), (-1,-1), 0.5, HexColor('#E5E7EB')),
        ]))
        story.append(rt)

    story.append(Spacer(1, 20))
    box(story,
        "<b>Cómo usar esta guía:</b> Ve directo al problema que necesitas resolver. "
        "Cada protocolo está diseñado para que veas resultados en las primeras 48 horas. "
        "No necesitas leer todo — solo lo que necesitas AHORA.",
        ROJO_DARK, ParagraphStyle('how', fontName=F, fontSize=11, textColor=BLANCO, leading=17))

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 1: LADRIDO EXCESIVO
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 1, "LADRIDO EXCESIVO", "🔊", CORAL, CORAL_LIGHT,
        "Tu perro NO ladra para molestarte. Ladra porque en algún momento aprendió que funciona. "
        "Alguien se fue y él ladró — y eventualmente esa persona volvió. Alguien tocó el timbre, él ladró "
        "— y alguien le hizo caso. Cada vez que el ladrido 'logró' algo, su cerebro lo anotó: "
        "'ladrar = conseguir lo que quiero'. Es comunicación, no maldad.",
        [
            "Identifica el DETONANTE. ¿Cuándo ladra? ¿Al ver personas por la ventana? ¿Cuando suena el timbre? ¿Cuando te vas? Anótalo. El detonante es la clave de todo.",
            "Cuando empiece a ladrar, NO le hables, NO le grites 'cállate' (eso para él es que TÚ también estás ladrando), NO lo mires. Dale la espalda completamente.",
            "En el INSTANTE en que se calle — aunque sea medio segundo para tomar aire — di '¡Bien!' y dale un premio increíble. El timing es todo: premia el SILENCIO, no el ladrido.",
            "Si ladra por el timbre o ventana: bloquea el acceso visual (cortina, mover muebles) y trabaja la desensibilización gradual al sonido.",
            "Repite 15-20 veces al día durante 48 horas. La consistencia absoluta es lo que hace que funcione.",
        ],
        "Cuando tu perro empiece a ladrar, dale la espalda sin decir UNA palabra. Cuando se calle, gira, míralo y di con voz alegre: '¡Eso! ¡Bien callado!' y dale un premio. Repite CADA VEZ.",
        "Gritar '¡CÁLLATE!' o '¡NO!'. Para tu perro, tú gritando = tú ladrando con él. Le estás dando exactamente lo que quiere: atención y compañía en el escándalo.",
        "Tu perro ladra, se detiene más rápido que antes, y te mira esperando el premio. El tiempo de ladrido se reduce visiblemente en 24-48 horas.")

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 2: MORDER / MORDISQUEAR
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 2, "MORDER / MORDISQUEAR", "🦷", NARANJA, NARANJA_LIGHT,
        "Los cachorros muerden porque están explorando el mundo con la boca — es su forma de conocer texturas, "
        "límites y juego. Los perros adultos que muerden las manos, zapatos o muebles generalmente tienen "
        "energía acumulada sin canalizar, aburrimiento, o nunca aprendieron la 'inhibición de mordida' "
        "(cuánta presión es aceptable y cuánta no).",
        [
            "Cuando muerda tu mano o ropa, di 'AY' en voz aguda (como un cachorro que se queja) e inmediatamente retira la mano y dale la espalda. Cero atención por 10 segundos.",
            "Después de los 10 segundos, vuelve a interactuar. Si muerde otra vez, repite: 'AY' + espalda + 10 segundos sin atención.",
            "Ten SIEMPRE un juguete de morder a la mano. Cuando veas que va a morder tu mano, intercepta con el juguete: 'Esto SÍ puedes morder'. Premia cuando muerda el juguete.",
            "Si muerde muebles o zapatos: rocía spray amargo (vinagre de manzana diluido) en los objetos y pon juguetes masticables atractivos cerca como alternativa.",
            "Asegúrate de que tenga al menos 30 minutos de ejercicio físico y 15 de estimulación mental al día. Un perro cansado no destruye.",
        ],
        "Cuando tu perro ponga los dientes en tu piel, di 'AY' de forma aguda inmediatamente, retira la mano y cruza los brazos mirando al techo. Cuenta hasta 10. Vuelve a jugar. Si muerde de nuevo: mismo proceso.",
        "Jalarle el hocico, sujetarle la boca cerrada o pegarle en la nariz. Esto causa MIEDO, no aprendizaje. Un perro que muerde por miedo muerde más fuerte.",
        "Tu perro empieza a morder, escucha tu 'AY', y suelta inmediatamente. Busca su juguete como alternativa.")

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 3: JALAR LA CORREA
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 3, "JALAR LA CORREA", "🦮", AZUL_DARK, HexColor('#EBF5FC'),
        "Tu perro jala porque nadie le enseñó que caminar a tu lado es mejor que correr adelante. "
        "Para él, jalar FUNCIONA: llega más rápido a los olores interesantes, a los otros perros, "
        "a todo lo que le emociona. Mientras jalar lo lleve a donde quiere ir, va a seguir jalando. "
        "Tenemos que invertir esa ecuación.",
        [
            "Usa una correa de longitud fija (1.5-2 metros). NUNCA retráctil — las retráctiles le enseñan que jalar = más cuerda = más libertad.",
            "Camina normalmente. En el INSTANTE en que la correa se tense, PARA. No digas nada. No jales de vuelta. Simplemente quédate como una ESTATUA.",
            "Espera. Tu perro va a jalonearse, confundirse, tal vez mirarte. Cuando la correa se afloje — aunque sea porque giró confundido — di '¡Bien!' y avanza inmediatamente.",
            "Cada vez que camine a tu lado con la correa suelta (aunque sean 2 pasos), dale un premio y dile lo increíble que es.",
            "Si algo lo excita mucho (otro perro, gato, persona), PARA antes de que jale. Espera a que te mire. Cuando te mire: premio triple y avanza.",
        ],
        "Cuando tu perro jale: PARA como una estatua. No digas nada. Cuando la correa se afloje: '¡Vamos!' con entusiasmo y camina. Jala: paras. Afloja: caminas. Así de simple, así de poderoso.",
        "Jalar la correa de vuelta. Esto se convierte en un juego de 'tira y afloja' donde AMBOS jalan. Además puede dañar su cuello y tráquea, especialmente en razas pequeñas.",
        "Tu perro empieza a parar antes de que la correa se tense, porque aprendió que la correa tensa = no avanzar. Mira hacia ti más seguido buscando aprobación.")

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 4: ANSIEDAD DE SEPARACIÓN
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 4, "ANSIEDAD DE SEPARACIÓN", "😰", MORADO, MORADO_LIGHT,
        "Tu perro no destruye tu casa por maldad ni por venganza. Cuando te vas, su cerebro entra literalmente en "
        "modo PÁNICO. Libera cortisol (la hormona del estrés) a niveles similares a los que experimentarías tú en "
        "una emergencia real. Para él, cada vez que sales por esa puerta existe la posibilidad de que no vuelvas. "
        "La ansiedad de separación es la causa #1 de abandono de mascotas en Latinoamérica.",
        [
            "DESENSIBILIZA las señales de salida. Toma tus llaves, ponte los zapatos, agarra el bolso... y siéntate en el sofá. No te vayas. Haz esto 10 veces seguidas hasta que tu perro deje de reaccionar a esas señales.",
            "Practica salidas ULTRA cortas. Abre la puerta, sal 5 segundos, vuelve a entrar. Sin drama al irte. Sin fiesta al volver. Como si fueras al baño.",
            "Aumenta gradualmente: 10 segundos, 30 segundos, 1 minuto, 3 minutos, 5 minutos. Si en algún punto ladra o llora, regresa al último tiempo que funcionó.",
            "Dale algo INCREÍBLE cuando te vayas: un Kong relleno de mantequilla de maní congelada, un hueso largo. Que tu salida prediga algo BUENO, no algo aterrador.",
            "Nunca castigues la destrucción cuando vuelvas. Él no recuerda qué hizo — solo ve que llegaste enojado. Eso aumenta la ansiedad para la próxima vez.",
        ],
        "Al salir: no digas nada. No lo mires. No digas 'ya vengo bebé'. Toma tus cosas y sal en silencio. Al volver: entra en silencio. Espera 2 minutos. Cuando esté calmado, salúdalo tranquilamente.",
        "Despedirse con drama: 'Ay mi amor, ya vengo, pórtate bien, no llores'. Esto le CONFIRMA que irte es algo terrible. Cuanto más drama hagas, más ansiedad siente.",
        "Tu perro ve que tomas las llaves y NO reacciona (no llora, no jadea, no te sigue desesperadamente). Puedes salir 5-10 minutos sin que ladre o destruya.")

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 5: SALTAR SOBRE PERSONAS
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 5, "SALTAR SOBRE PERSONAS", "🦘", VERDE, VERDE_LIGHT,
        "Tu perro salta porque en algún momento FUNCIONÓ. Alguien lo acarició cuando saltó. Alguien se rió. "
        "Alguien dijo 'ay qué lindo' mientras le ponía las patas encima. Cada reacción — buena o mala — reforzó "
        "el comportamiento. Incluso empujarlo es atención. Para un perro, atención negativa es mejor que cero atención.",
        [
            "La regla es absoluta: si salta, CERO atención. Le das la espalda inmediatamente. Brazos cruzados. Sin mirarlo, sin hablarle, sin tocarlo. CERO.",
            "Cuando tenga las 4 patas en el suelo — ahí sí: vuélvete, agáchate a su nivel, y dale toda la atención y cariño del mundo. Premia con comida y afecto.",
            "Cuando lleguen visitas: ponle la correa ANTES de que toquen la puerta. Pisa la correa con el pie dejando solo lo suficiente para que esté parado pero NO pueda saltar.",
            "Enséñale un comportamiento ALTERNATIVO: 'Siéntate para saludar'. Cada persona que llega le pide sentarse primero — solo lo saludan si está sentado.",
            "Avisa a TODA persona que interactúe con tu perro: 'Si salta, dale la espalda. Si se sienta, puedes saludarlo.' La consistencia de todos es clave.",
        ],
        "Tu perro salta: giras la espalda sin decir UNA palabra. Cuando baja las patas: te agachas y dices '¡Eso! ¡Patas abajo!' con mucho cariño. Le pides 'siéntate' y cuando se sienta lo llenas de atención.",
        "Empujarlo con las manos o la rodilla. Para el perro, que lo toques (aunque sea para empujarlo) ES atención, y atención ES lo que quiere. Empujar = premiar el salto.",
        "Tu perro ve que alguien llega y en vez de saltar, se sienta automáticamente esperando ser saludado. Ese momento es mágico cuando pasa.")

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 6: AGRESIVIDAD CON OTROS PERROS
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 6, "AGRESIVIDAD CON OTROS PERROS", "😤", ROJO, ROJO_LIGHT,
        "En el 95% de los casos, la agresividad NO es dominancia — es MIEDO o inseguridad. Tu perro no ataca "
        "porque quiere pelear. Ataca porque no sabe cómo manejar la situación de otra forma. Es su forma "
        "de decir 'tengo miedo, aléjate'. El problema es que funciona: cuando gruñe o se lanza, el otro perro "
        "(y su dueño) se alejan. Comportamiento reforzado.",
        [
            "DISTANCIA es tu mejor herramienta. Identifica a qué distancia tu perro VE al otro perro pero NO reacciona. Esa es tu 'zona segura'. Puede ser 30 metros, puede ser 50.",
            "Cada vez que vea un perro a esa distancia y NO reaccione (no gruñe, no se tensa, no jala), prémialo con lo mejor que tengas: pollo, queso, salchicha. Fiesta.",
            "Si reacciona: te alejaste demasiado poco. Sin drama, da media vuelta y aléjate. No lo regañes. No jales la correa con fuerza.",
            "En sesiones posteriores (NO el mismo día), reduce la distancia 2-3 metros. Gradualmente, su cerebro aprende: 'otro perro = premios increíbles para mí'.",
            "NUNCA fuerces un encuentro cara a cara. Eso puede terminar en una mordida y retroceder semanas de progreso.",
        ],
        "Ves un perro a lo lejos. Antes de que tu perro reaccione, di su nombre en tono alegre. Cuando te mire: 'SÍ, ¡bien!' y dale 3 premios seguidos. Repite cada vez que pase un perro.",
        "Jalar la correa y regañarlo cuando se lanza hacia otro perro. La tensión en la correa AUMENTA la reactividad. Y el regaño le confirma que la situación es estresante.",
        "Tu perro ve otro perro a distancia media y en vez de tensarse o ladrar, te mira a ti buscando su premio. Eso significa que su asociación emocional está cambiando.")

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 7: NO OBEDECER "VEN"
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 7, "NO OBEDECER 'VEN'", "🏃", TEAL, TEAL_LIGHT,
        "Si tu perro no viene cuando lo llamas, es porque 'ven' perdió su valor. Probablemente lo llamas "
        "para cosas que no le gustan (bañarlo, cortarle las uñas, regañarlo, encerrarlo). Su cerebro aprendió: "
        "'cuando dice ven, pasa algo malo'. ¿Por qué iría? Tenemos que resetear completamente la palabra.",
        [
            "Elige una palabra NUEVA. No uses 'ven' si ya está quemada. Usa 'aquí', 'vamos', o un silbido específico. Esa palabra nueva va a ser SAGRADA — solo para cosas buenas.",
            "En tu casa, sin distracciones: di la palabra nueva y MUÉSTRALE un premio irresistible. Cuando venga, fiesta absoluta: 5 premios seguidos, cariño, celebración.",
            "Practica 20 veces al día en momentos random. Mientras cocinas, mientras ves TV, mientras estás en el patio. Palabra nueva = fiesta.",
            "NUNCA uses la palabra nueva para algo que no le gusta. Si necesitas bañarlo, ve tú a buscarlo. La palabra nueva es SAGRADA: solo predice cosas increíbles.",
            "Gradualmente practica en lugares con más distracción: patio, parque tranquilo, calle. Siempre con correa larga al principio, por seguridad.",
        ],
        "Di la palabra nueva ('AQUÍ') UNA sola vez, en tono alegre y agudo. Muestra el premio. Cuando venga: '¡SÍ! ¡Increíble!' y dale 5 premios seguidos, uno por uno. Hazlo la mejor decisión de su día.",
        "Repetir 'ven, ven, ven, VEN, VEN AQUÍ, VEEEEN' mil veces. Cada repetición le enseña que puede ignorarte las primeras 10 veces porque siempre repites. Di la palabra UNA vez.",
        "Dices la palabra nueva y tu perro DEJA lo que está haciendo para correr hacia ti con entusiasmo. No importa dónde estés ni qué estaba haciendo — viene porque sabe que tú eres lo mejor.")

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 8: DESTRUCCIÓN EN CASA
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 8, "DESTRUCCIÓN EN CASA", "🏠", ROSA, ROSA_LIGHT,
        "Los perros destruyen por 3 razones principales: aburrimiento (no tiene nada mejor que hacer), "
        "ansiedad (está estresado cuando te vas), o exceso de energía (necesita más ejercicio del que recibe). "
        "Un perro que destruye NO es vengativo ni rencoroso — los perros no tienen la capacidad cognitiva para "
        "la venganza. Destruye porque su cerebro necesita algo que no está recibiendo.",
        [
            "DIAGNÓSTICA la causa. ¿Destruye solo cuando te vas? → Ansiedad (ve al Problema #4). ¿Destruye siempre? → Aburrimiento o energía. ¿Destruye cosas específicas? → Asociación con tu olor (zapatos, ropa).",
            "AUMENTA el ejercicio: mínimo 30-45 minutos de caminata activa al día + 15 minutos de juego mental (buscar premios escondidos, Kong relleno, juegos de olfato).",
            "Haz tu casa A PRUEBA DE PERRO: recoge zapatos, cierra puertas de cuartos que no debe entrar, usa barreras físicas. Si no tiene acceso, no puede destruir.",
            "Dale ALTERNATIVAS legítimas para masticar: huesos naturales, juguetes Kong, cuerdas de morder. Cuando lo veas masticando algo permitido, prémialo efusivamente.",
            "Si lo encuentras destruyendo algo: NO lo regañes. Simplemente retira el objeto en silencio, dale su juguete permitido, y premia cuando lo muerda. El regaño no funciona si no lo atrapas en el acto.",
        ],
        "Antes de irte: esconde 5 premios por la casa para que los busque. Déjale un Kong relleno y congelado. Pon música suave. Dale una caminata de 20 minutos. Un perro cansado y entretenido no destruye.",
        "Regañarlo cuando llegas y ves la destrucción. Él NO conecta tu enojo con algo que hizo hace horas. Solo aprende que cuando llegas, estás enojado. Eso aumenta la ansiedad y... la destrucción.",
        "Tu perro tiene sus juguetes y los usa en vez de tus cosas. La destrucción se reduce dramáticamente en 48 horas cuando combinas ejercicio + alternativas + prevención.")

    # ═══════════════════════════════════════════════════════════
    # PROBLEMA 9: LLANTO Y LLORIQUEO EXCESIVO
    # ═══════════════════════════════════════════════════════════
    problema_block(story, 9, "LLANTO Y LLORIQUEO EXCESIVO", "😢", AMARILLO_DARK, AMARILLO_LIGHT,
        "El llanto en los perros es una forma de comunicación primitiva que aprendieron desde cachorros. "
        "Cuando eran bebés, lloraban y su mamá venía. Ese patrón quedó grabado: 'si lloro, alguien viene a rescatarme'. "
        "Los perros adultos lloran por atención, por ansiedad, por frustración o por dolor. Lo primero es descartar "
        "un problema de salud con tu veterinario. Si está sano, el llanto es un hábito aprendido que podemos cambiar.",
        [
            "DESCARTA dolor o enfermedad. Si el llanto es repentino o acompañado de otros síntomas (no come, cojea, se lame una zona), llévalo al veterinario primero. Si está sano, continúa con los siguientes pasos.",
            "Identifica CUÁNDO llora. ¿Cuando te vas? → Ansiedad (ve Problema #4). ¿Cuando quiere comida o atención? → Llanto aprendido. ¿En la noche? → Necesita rutina. ¿En el carro/vet? → Miedo.",
            "Para llanto por atención: cuando empiece a llorar, NO lo mires, NO le hables, NO lo acaricies. Absolutamente CERO respuesta. Cada vez que le hagas caso cuando llora, le enseñas que llorar funciona.",
            "Espera a que se calle — aunque sea un segundo de silencio — e inmediatamente prémialo con atención y cariño: '¡Eso! ¡Qué tranquilo!' con voz dulce. Estás premiando el SILENCIO.",
            "Para llanto nocturno: establece una rutina firme antes de dormir (paseo de 15 min, última comida, último baño). Ponlo en su lugar de dormir y no vuelvas cuando llore. Las primeras 2-3 noches serán difíciles, pero si resistes sin ceder, se resuelve.",
        ],
        "Tu perro empieza a llorar buscando atención: cero contacto visual, cero palabras, cero caricias. Cuando se calle por al menos 3 segundos: te volteas, lo miras con amor y dices '¡Muy bien, así tranquilo!' con voz suave. Premio.",
        "Ir corriendo a consolarlo cada vez que llora. Eso le enseña que llorar = atención inmediata. También gritarle '¡YA CÁLLATE!' — eso es atención negativa, pero sigue siendo atención.",
        "Tu perro llora menos frecuentemente y por menos tiempo. Empieza a buscar tu atención con comportamientos tranquilos (sentarse cerca, mirarte) en vez de con llanto.")

    story.append(PageBreak())

    # ═══════════════════════════════════════════════════════════
    # AVISO IMPORTANTE
    # ═══════════════════════════════════════════════════════════
    story.append(Spacer(1, 10))
    warn = [[Paragraph(
        "<b>NOTA IMPORTANTE</b><br/><br/>"
        "Esta guía está diseñada para problemas de comportamiento comunes y manejables. "
        "Si tu perro muestra agresividad severa hacia personas (gruñe, muestra dientes, "
        "ha mordido), busca un etólogo o adiestrador profesional certificado en tu ciudad. "
        "La seguridad de tu familia siempre es lo primero.<br/><br/>"
        "Todos los métodos de esta guía están basados en refuerzo positivo y ciencia del "
        "comportamiento canino. Sin castigos, sin dolor, sin miedo.",
        ParagraphStyle('warn', fontName=F, fontSize=13, textColor=BLANCO, leading=20, alignment=TA_CENTER))]]
    wt = Table(warn, colWidths=[W])
    wt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), ROJO_DARK),
        ('ROUNDEDCORNERS', [14, 14, 14, 14]),
        ('TOPPADDING', (0,0), (-1,-1), 24),
        ('BOTTOMPADDING', (0,0), (-1,-1), 24),
        ('LEFTPADDING', (0,0), (-1,-1), 24),
        ('RIGHTPADDING', (0,0), (-1,-1), 24),
    ]))
    story.append(wt)

    story.append(Spacer(1, 30))

    # ═══════════════════════════════════════════════════════════
    # CIERRE
    # ═══════════════════════════════════════════════════════════
    final = [[Paragraph(
        "<b><font size='28' color='#F7D44C'>Tu perro cuenta contigo.</font></b><br/><br/>"
        "El hecho de que estés leyendo esta guía significa que te importa. "
        "Que no te rendiste. Que buscaste una solución en vez de conformarte con el caos.<br/><br/>"
        "<i>Cada problema tiene solución. Y ahora tienes las herramientas.</i><br/><br/>"
        "- - - - - - - - - - - - - -<br/><br/>"
        "<i>Con amor,</i><br/>"
        "<b>El equipo AZUL</b><br/><br/>"
        "<font color='#F7D44C'><b>azulapp.org</b></font>",
        ParagraphStyle('final', fontName=F, fontSize=13, textColor=BLANCO, alignment=TA_CENTER, leading=20))]]
    ft = Table(final, colWidths=[W])
    ft.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), AZUL_DARK),
        ('ROUNDEDCORNERS', [20, 20, 20, 20]),
        ('TOPPADDING', (0,0), (-1,-1), 30),
        ('BOTTOMPADDING', (0,0), (-1,-1), 30),
        ('LEFTPADDING', (0,0), (-1,-1), 30),
        ('RIGHTPADDING', (0,0), (-1,-1), 30),
    ]))
    story.append(ft)

    doc.build(story)
    print("✅ SOS Comportamiento generado!")

if __name__ == '__main__':
    build_pdf()
