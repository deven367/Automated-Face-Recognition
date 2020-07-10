import xlwt 
from xlwt import Workbook 
import datetime
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
  
sheet1.write(1, 0, 'ISBT DEHRADUN') 
sheet1.write(2, 0, 'SHASTRADHARA') 
sheet1.write(3, 0, 'CLEMEN TOWN') 
sheet1.write(4, 0, 'RAJPUR ROAD') 
sheet1.write(5, 0, 'CLOCK TOWER') 
time = datetime.datetime.now()
print(time)
sheet1.write(6,0, str(time))
wb.save('xlwt example.xls') 