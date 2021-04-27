import xlrd
loc=("c:\\user\\admin\\desktop\\book.xlsx")
op=xlrd.open_workbook(loc)

#it indicat in which sheet do operations
sheet=op.sheet_by_index(0)
print(sheet.cell_value(1))

#print the value of cell which row no is 3 and column number is 0
print(sheet.cell_value(3,0))

#give number of columns
print(sheet.ncols)

#give number of rows
print(sheet.nrows)

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))

#print the row values
print(sheet.row_values(1))
