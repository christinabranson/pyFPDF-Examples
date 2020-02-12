# 0_test_basic.py
# runs a basic html file from template

import os
from weasyprint import HTML, CSS
import argparse

parser = argparse.ArgumentParser(description='PDF maker with custom arguments')
parser.add_argument("--title", default="", help="This is the title of the PDF")
parser.add_argument("--subtitle", default="", help="This is the subtitle of the PDF")
parser.add_argument("--text", default="", help="This is the text of the PDF")
parser.add_argument("--outputpath", default="", help="This is the output path")
args = parser.parse_args()
title = args.title
subtitle = args.subtitle
text = args.text
outputpath = args.outputpath
if not outputpath:
    outputpath = 'pdfs/5_test_complicated_template_with_arguments.pdf'

root = os.path.dirname(os.path.abspath(__file__))
htmlpath = os.path.join(root, 'templates', '5_test_complicated_template_with_arguments.html')
with open(htmlpath, 'r') as file:
    html = file.read()

    html = html.replace("{% title %}", title)
    html = html.replace("{% subtitle %}", subtitle)
    html = html.replace("{% text %}", text)

    # now add the substitutions

    pdf_file = HTML(string=html).write_pdf(outputpath)