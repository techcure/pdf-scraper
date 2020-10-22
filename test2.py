import pdfplumber
import os, sys


#pdf = pdfplumber.open("Report_20201009000009646.pdf")
path = "pdf"
dirs = os.listdir(path)

    # #print(file)

dict = {}
dict2 ={}
for file in dirs:
    print(file)
    pdf = pdfplumber.open(file)
    page = pdf.pages[0]
    crcn = page.extract_text()[66:73]
    for c1,table in enumerate(page.extract_tables()):
        for c2,list in enumerate(table):
            for c3,x in enumerate(list):
                if x != None:
                    # print(f"{c1},{c2},{c3}-->{x}")
                    d = {"Crash Report Case No.": crcn}
                    dict.update(d)
                    if (c1 == 2 and c2 == 0 and c3 == 0):
                        d = {"Local Case No.": x[15:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 3):
                        d= {"Date_Month":x}
                        dict.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 4):
                        d = {"Date_Day": x}
                        dict.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 8):
                        d = {"Date_year": x}
                        dict.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 13):
                        d = {"Time": x[5:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 21):
                        d = {"Day of Week": x[12:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 26):
                        d = {"County": x[7:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 38):
                        d = {"City": x[11:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 7 and c3 == 2):
                        d = {"Driver Full Name, Street Address, City and State": x[47:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 7 and c3 == 46):
                        d = {"ZIP": x[4:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 7 and c3 == 50):
                        d = {"Telephone": x[10:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 8 and c3 == 3):
                        d = {"DOB_Month": x}
                        dict.update(d)
                    if (c1 == 0 and c2 == 8 and c3 == 4):
                        d = {"DOB_Day": x}
                        dict.update(d)
                    if (c1 == 0 and c2 == 8 and c3 == 8):
                        d = {"DOB_Year": x}
                        dict.update(d)
                    if (c1 == 0 and c2 == 8 and c3 == 12):
                        d = {"Race": x[5:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 8 and c3 == 15):
                        d = {"Sex": x[4:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 8 and c3 == 16):
                        d = {"DL State": x[9:]}
                        dict.update(d)
                    if (c1 == 0 and c2 == 8 and c3 == 20):
                        d = {"Driver License No.": x[19:]}
                        dict.update(d)
                    d = {"Crash Report Case No.": crcn}
                    dict2.update(d)
                    if (c1 == 2 and c2 == 0 and c3 == 0):
                        d = {"Local Case No.": x[15:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 3):
                        d= {"Date_Month":x}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 4):
                        d = {"Date_Day": x}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 8):
                        d = {"Date_year": x}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 13):
                        d = {"Time": x[5:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 21):
                        d = {"Day of Week": x[12:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 26):
                        d = {"County": x[7:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 38):
                        d = {"City": x[11:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 24 and c3 == 2):
                        d = {"Driver Full Name, Street Address, City and State": x[47:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 24 and c3 == 46):
                        d = {"ZIP": x[4:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 24 and c3 == 50):
                        d = {"Telephone": x[10:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 25 and c3 == 3):
                        d = {"DOB_Month": x}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 25 and c3 == 4):
                        d = {"DOB_Day": x}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 25 and c3 == 8):
                        d = {"DOB_Year": x}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 25 and c3 == 12):
                        d = {"Race": x[5:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 25 and c3 == 15):
                        d = {"Sex": x[4:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 25 and c3 == 16):
                        d = {"DL State": x[9:]}
                        dict2.update(d)
                    if (c1 == 0 and c2 == 25 and c3 == 20):
                        d = {"Driver License No.": x[19:]}
                        dict2.update(d)




print(dict)
print(dict2)