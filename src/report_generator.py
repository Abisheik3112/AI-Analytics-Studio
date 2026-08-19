from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from src.insights import generate_insights


def generate_pdf_report(df):

    insights = generate_insights(df)

    pdf_path = "AI_Data_Report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI DATA ANALYSIS REPORT",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Rows: {df.shape[0]}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Columns: {df.shape[1]}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "AI Insights",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            insights,
            styles["Normal"]
        )
    )

    doc.build(elements)

    return pdf_path