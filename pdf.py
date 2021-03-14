import PyPDF2

book = []

# pdf file object
pdfFileObj = open('data\course19-20.pdf', 'rb')

# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# get number of pages
pages = range(pdfReader.numPages)

# print each page
for x in pages:
    pageObj = pdfReader.getPage(x)
    book.append(pageObj.extractText())

print(book[1])

for line in book[1]:
    if line.startswith()

print(book[2])
# closing the pdf file object
pdfFileObj.close()