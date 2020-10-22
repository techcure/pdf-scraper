# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('Report_20201009000009646.pdf', 'rb') 
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# printing number of pages in pdf file 
print(pdfReader.numPages) 
# creating a page object 
pageObj = pdfReader.getPage(0) 

import pdb; pdb.set_trace()
# extracting text from page 
# print(pageObj.extractText())

sdf = pageObj.extractText()

data = sdf.split()
print(data[50])
  
# closing the pdf file object 
# pdfFileObj.close()
