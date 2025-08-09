from fpdf import FPDF
import os
import re

def generate_pdf(name, analysis_html):
    text_only = re.sub(r'<[^>]+>', '', analysis_html)  # HTML 태그 제거
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"{name}님의 사주 분석 보고서", align='L')
    pdf.multi_cell(0, 10, text_only, align='L')
    file_path = f"{name}_saju_report.pdf"
    pdf.output(file_path)
    return file_path
