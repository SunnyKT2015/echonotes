import io
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
)
from reportlab.lib.units import inch
from reportlab.lib.units import mm

def add_page_number(canvas, doc):
    page_num = canvas.getPageNumber()
    text = f"Page {page_num}"
    canvas.drawRightString(200 * mm, 15 * mm, text)

def get_text_file(transcript, summary, keypoints, topics, mnemonic):
    """Return TXT bytes with notes."""
    content = []
    if transcript:
        content.append("=== Transcript ===\n" + transcript + "\n")
    if summary:
        content.append("=== Summary ===\n" + summary + "\n")
    if keypoints:
        content.append("=== Keypoints ===\n" + keypoints + "\n")
    if topics:
        content.append("=== Topics ===\n" + ", ".join(topics) + "\n")
    if mnemonic:
        content.append("=== Mnemonic ===\n" + mnemonic + "\n")

    return "\n".join(content).encode("utf-8")


def get_pdf_file(transcript, summary, keypoints, topics, mnemonic):
    """Return PDF bytes with nicely formatted notes like a report."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )
    story = []

    # Styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    section_style = ParagraphStyle('SectionHeading', parent=styles['Heading1'], spaceAfter=10)
    normal_style = styles['Normal']
    bullet_style = ParagraphStyle('Bullet', parent=normal_style, leftIndent=20, spaceAfter=4)

    # --- Title Page ---
    story.append(Spacer(1, 2 * inch))
    story.append(Paragraph("Lecture Voice → Notes", title_style))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph("Auto-generated Notes", normal_style))
    story.append(PageBreak())

    # --- Transcript ---
    if transcript:
        story.append(Paragraph("Transcript", section_style))
        for line in transcript.split("\n"):
            if line.strip():
                story.append(Paragraph(line.strip(), normal_style))
        story.append(Spacer(1, 0.3 * inch))

    # --- Summary ---
    if summary:
        story.append(Paragraph("Summary", section_style))
        for line in summary.split("\n"):
            if line.strip():
                story.append(Paragraph(line.strip(), normal_style))
        story.append(Spacer(1, 0.3 * inch))

    # --- Keypoints ---
    if keypoints:
        story.append(Paragraph("Keypoints", section_style))
        bullet_items = []
        for line in keypoints.split("\n"):
            if line.strip():
                bullet_items.append(ListItem(Paragraph(line.strip().lstrip("- "), normal_style)))
        story.append(ListFlowable(bullet_items, bulletType='bullet'))
        story.append(Spacer(1, 0.3 * inch))

    # --- Topics ---
    if topics:
        story.append(Paragraph("Topics", section_style))
        story.append(Paragraph(", ".join(topics), normal_style))
        story.append(Spacer(1, 0.3 * inch))

    # --- Mnemonic ---
    if mnemonic:
        story.append(Paragraph("Mnemonic", section_style))
        story.append(Paragraph(mnemonic, normal_style))

    # Build PDF with footer
    doc.build(story, onLaterPages=add_page_number, onFirstPage=add_page_number)
    buffer.seek(0)
    return buffer.getvalue()
