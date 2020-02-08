# pyFPDF Examples

Working my way up to a fully-functional PDF generating tool that substitutes user values from the command line

![alt text](https://raw.githubusercontent.com/christinabranson/pyFPDF-Examples/master/templates/assets/img/PDF_Examples_Screenshot.png "Example PDF screenshot")

Only requires fpdf


| Script                                    | Description   |
| -------------                             |-------------  |
| 0_test_basic.py                           | Creates a PDF from an HTML template |
| 1_test_with_image.py                      | Created a PDF with a hardcoded image      |
| 2_test_substitution.py                    | Creates a PDF with variables within the HTML template. For example, `{% title %}` is substituted with a string title from within the Python code      |
| 3_test_substitution_with_image.py         | The PDF is created using substitutions, including an image coming from the Python code     |
| 3a_test_substitution_with_image_base64.py | An attempt at the one above, but using a base64 encoded image string instead of a local file. This is not currently working      |
| 4_test_substitution_with_arguments.py     | Uses `argparse` to pull in argument from the command line, instead of using hardcoded variables within the Python code. Run with: `python3 4_test_substitution_with_arguments.py --title "Title From Arguments"`      |