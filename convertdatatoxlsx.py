import xlsxwriter 

data=raw_input("Enter the name of data file to convert to XLSX")
#f=open(str(data)+'.xlsx','w+')
#f.close()
workbook=xlsxwriter.Workbook(str(data)+'.xlsx')
worksheet=workbook.add_worksheet()
rown=0 
rows=open(data).readlines()
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

