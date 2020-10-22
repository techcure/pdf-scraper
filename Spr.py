# importing required modules 
import PyPDF2 
from tabula import read_pdf
import pandas as pd
import tabula
	
# creating a pdf file object 
pdfFileObj = open('Report_20201009000009646.pdf', 'rb')
	
tabula.convert_into("Report_20201009000009646.pdf", "output.csv", output_format="csv", pages='all')
#tabula.convert_into("Report_20201009000009646.pdf", "output.json", output_format = "json", pages = "all")
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	
# printing number of pages in pdf file 
print(pdfReader.numPages) 
	
# creating a page object 
pageObj = pdfReader.getPage(0) 
	
# extracting text from page 
data1=pageObj.extractText()
print(data1)
# closing the pdf file object 
pdfFileObj.close() 

f = open("demofile2.txt", "a")
f.write(pageObj.extractText())
f.close()