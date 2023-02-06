import pandas as pd
import os
out = open('out.txt', 'a')

def excel_parse (location, column):
    df = pd.read_excel(location, sheet_name='Sheet1', usecols=column)  # reads xlsx
    output_list_x = df["Accession_Number"]      # assigns values of one column to list
    return output_list_x



def compare (xlsx_lst, os_lst):
    ## compares two lists of strings to determine if there are any mismatches

    missing_os = []
    i = 0
    while i < len(xlsx_lst):
        count = 0
        for j in os_lst:
            count += 1
            if xlsx_lst[i][4:13] == j[4:13]:
                xlsx_lst.pop(i)
                os_lst.pop(os_lst.index(j))
                break
            elif count == (len(os_lst)):
                i += 1
                break
    for a in os_lst:
        missing_os.append(i)
    for l in xlsx_lst:
        out.write(l + '\n')
    for j in os_lst:
        out.write('\t' + j + '\n')
    return missing_os

x = "/Users/eliascrum/Desktop/all_gasseri_paragasseri.xlsx"
y = "Accession_Number"


z = os.listdir('/Users/eliascrum/fastANI/Lacto_G/')  # contains the genome names we have
os_g = []
for i in z:
    if i[-4:] == '.fna':
        os_g.append(i)

xlsx_g = []  # contains only the genome names we want
e = excel_parse(x,y)
for i in e:                     # gets rid of null sections of xlsx
    try:
        if str(i[:3]) == 'GCA' or str(i[:3]) == 'GCF':
            xlsx_g.append(i)
    except:
        None

missing = compare(xlsx_g, os_g)

out.close()
