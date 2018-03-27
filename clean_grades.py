import os
from PyPDF2 import PdfFileWriter, PdfFileReader

TARGET_DIR = './assignment_66116_export'
OUTPUT_DIR = './grades-removed'

def getAssignments():
  print("Getting PDFS...")
  for f in os.listdir(TARGET_DIR):
    if f[0] == '.': continue
    print(f)
    outputPDF = PdfFileWriter()
    inputPDF = PdfFileReader(open(os.path.join(TARGET_DIR, f), "rb"))
    num_pages = inputPDF.getNumPages()
    if num_pages == 2: continue
    for i in range(1, num_pages-1):
      outputPDF.addPage(inputPDF.getPage(i))
    outputStream = open(os.path.join(OUTPUT_DIR ,f), "wb")
    outputPDF.write(outputStream)

def main():
  getAssignments()

if __name__ == '__main__':
  main()
