# 1_test_with_image.py
# CURRENTLY FAILS

import os
from fpdf import FPDF, HTMLMixin


class HTML2PDF(FPDF, HTMLMixin):
    pass


def html2pdf():
    root = os.path.dirname(os.path.abspath(__file__))
    htmlpath = os.path.join(root, 'templates', '1_test_with_image.html')
    with open(htmlpath, 'r') as file:
        html = file.read()

        pdf = HTML2PDF()
        pdf.add_page()
        pdf.write_html(html)
        pdf.output('pdfs/1_test_with_image.pdf')


if __name__ == '__main__':
    html2pdf()