import os 
from PyPDF2 import PdfFileReader
dirname = "/media/morgan/新加卷1/33/"
names = os.listdir(dirname)
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False
for name in names:
    infile = dirname + name
    try:
        pdf_reader = PdfFileReader(open(infile, "rb"))
        dictionary = pdf_reader.getDocumentInfo()
        title = dictionary.get('/Title')
        if title  != "" and is_contains_chinese(title):
            outfile = dirname + title
            os.rename(infile,outfile)
            print(title)
    except:
        continue
