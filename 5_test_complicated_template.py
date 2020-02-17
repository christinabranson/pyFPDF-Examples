# 0_test_basic.py
# runs a basic html file from template

import os
from weasyprint import HTML, CSS

root = os.path.dirname(os.path.abspath(__file__))
htmlpath = os.path.join(root, 'templates', '5_test_complicated_template.html')
with open(htmlpath, 'r') as file:
    html = file.read()

    pdf_file = HTML(string=html).write_pdf('pdfs/5_test_complicated_template.pdf')