# 0_test_basic.py
# runs a basic html file from template

import os
from fpdf import FPDF, HTMLMixin

class HTML2PDF(FPDF, HTMLMixin):
    pass


def html2pdf():
    root = os.path.dirname(os.path.abspath(__file__))
    htmlpath = os.path.join(root, 'templates', '0_test_basic.html')
    with open(htmlpath, 'r') as file:
        html = file.read()

        pdf = HTML2PDF()
        pdf.add_page()
        pdf.write_html(html)
        pdf.output('pdfs/0_text_basic.pdf')


if __name__ == '__main__':
    html2pdf()