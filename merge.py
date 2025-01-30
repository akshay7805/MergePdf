import os 
from PyPDF2 import PdfWriter
merger=PdfWriter()
pdf1=input("Enter pdf name ending with .pdf also: ")
pdf2=input("Enter pdf name ending with .pdf also: ")
files=[file for file in os.listdir() if file.endswith(".pdf") ]
for pdf in files:
    if pdf==pdf1 or pdf==pdf2:
        merger.append(pdf)
    else:
        continue
merger.write("combined.pdf") 
merger.close()       