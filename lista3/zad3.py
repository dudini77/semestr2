
from PyPDF2 import PdfMerger

def polacz_pdf(lista_pdf, output):
    merger = PdfMerger()
    for i in lista_pdf:
        merger.append(i)
    merger.write(output)
    merger.close()
pdf_to_merge= ['pdf-sample_0.pdf', 'a559_14_9_2024.pdf']
x="polaczony-pdf.pdf"
polacz_pdf(pdf_to_merge, x)