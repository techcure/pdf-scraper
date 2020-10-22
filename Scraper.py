
#Copy Right @TechCure

#for single pdf page

from tabula import read_pdf
import tabula

import textract
text = textract.process("Report_20201009000009646.pdf")
#text =tabula.convert_into("Report_20201009000009646.pdf", "output.csv", output_format="csv", pages='all')
data  = text.split()

y=[]
for x in data:
    y.append(x.decode('utf-8'))
a = "Day of Week"
words = a.split()
length= len(words)

if words[0] in y:
    c =y.count(words[0]) 
def list_duplicates_of(seq, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs
x=list_duplicates_of(y, words[0])
print(x[1], length)
c = x[1]+1
if length == 4:
    if y[c] == words[1] and y[c+1] == words[2] and y[c+2] == words[3]:
            print(y[c+3])

if length == 3:
    if y[c] == words[1] and y[c+1] == words[2]:
            print(y[c+3])
