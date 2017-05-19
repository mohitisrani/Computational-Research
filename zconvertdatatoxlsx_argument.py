import xlsxwriter 
import sys

#f=open(str(sys.argv)[1]+'.xlsx','w+')
#f.close()
#print sys.argv[1]

workbook=xlsxwriter.Workbook((sys.argv)[1]+'.xlsx')
worksheet=workbook.add_worksheet()
rown=0 
rows=open(sys.argv[1]).readlines()
for row in rows:
    coln=0
    columns=row.split()
    for column in columns:
        try:
            column=float(column) 
        except:
            x=1
        worksheet.write(rown, coln, column)
        coln=coln+1
    rown=rown+1
workbook.close()  

