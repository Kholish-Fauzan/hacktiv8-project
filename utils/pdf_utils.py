# utils/pdf_utils.py
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from io import BytesIO
from datetime import datetime

def create_styles():
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['h1'],
        fontSize=24,
        leading=28,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    normal_style = ParagraphStyle(
        'NormalStyle',
        parent=styles['Normal'],
        fontSize=12,
        leading=14,
        alignment=TA_LEFT,
        spaceAfter=12
    )

    section_title_style = ParagraphStyle(
        'SectionTitleStyle',
        parent=styles['h2'],
        fontSize=18,
        leading=22,
        spaceAfter=10,
        textColor='#34495E'
    )

    point_style = ParagraphStyle(
        'PointStyle',
        parent=styles['h3'],
        fontSize=14,
        leading=16,
        spaceBefore=10,
        spaceAfter=5,
        textColor='#2C3E50'
    )

    description_style = ParagraphStyle(
        'DescriptionStyle',
        parent=styles['Normal'],
        fontSize=11,
        leading=13,
        spaceAfter=10,
        leftIndent=20
    )

    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontSize=9,
        alignment=TA_CENTER,
        textColor='#777777',
        spaceBefore=30
    )

    return {
        'title_style': title_style,
        'normal_style': normal_style,
        'section_title_style': section_title_style,
        'point_style': point_style,
        'description_style': description_style,
        'footer_style': footer_style
    }

def generate_pdf_from_text(text_content, title="Dokumen Streamlit"):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = create_styles()
    story = []

    story.append(Paragraph(title, styles['title_style']))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(text_content.replace('\n', '<br/>'), styles['normal_style']))

    try:
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return None

def generate_analysis_pdf(analysis_data, title="Analisis Promosi"):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = create_styles()
    story = []

    story.append(Paragraph(title, styles['title_style']))
    story.append(Spacer(1, 0.3 * inch))

    add_section(story, "Poin Jual Utama", analysis_data.get("Poin Jual Utama", []), styles['section_title_style'], styles['point_style'], styles['description_style'])
    add_section(story, "Segmen Wisatawan Ideal", analysis_data.get("Segmen Wisatawan Ideal", []), styles['section_title_style'], styles['point_style'], styles['description_style'])
    add_section(story, "Ide Monetisasi & Produk Pariwisata", analysis_data.get("Ide Monetisasi & Produk Pariwisata", []), styles['section_title_style'], styles['point_style'], styles['description_style'])
    add_section(story, "Saran Peningkatan Pesan Promosi", analysis_data.get("Saran Peningkatan Pesan Promosi", []), styles['section_title_style'], styles['point_style'], styles['description_style'])
    add_section(story, "Potensi Kolaborasi Lokal", analysis_data.get("Potensi Kolaborasi Lokal", []), styles['section_title_style'], styles['point_style'], styles['description_style'])

    story.append(Paragraph("", styles['footer_style']))

    try:
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    except Exception as e:
        print(f"Error generating analysis PDF: {e}")
        return None

def add_section(story, section_title, data, section_title_style, point_style, description_style):
    story.append(Paragraph(section_title, section_title_style))
    story.append(Spacer(1, 0.1 * inch))

    if data:
        for item in data:
            story.append(Paragraph(f"👉 {item.get('poin', '')}", point_style))
            story.append(Paragraph(item.get('deskripsi', ''), description_style))
    story.append(Spacer(1, 0.2 * inch))