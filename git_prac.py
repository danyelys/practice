import fitz
import pandas
import docx
from collections import defaultdict

pdf_path = r"C:\Users\danyel\Downloads\Resume_danyel_final_final.pdf"

def read_pdf(pdf):
    #content = fitz.open(stream = pdf, filetype = "pdf")
    content = fitz.open(pdf, filetype = "pdf")
    return "".join([page.get_text(sort = True) for page in content])

test_pdf = read_pdf(pdf_path)


print(test_pdf)