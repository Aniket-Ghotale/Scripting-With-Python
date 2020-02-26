import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_file):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_file:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)