from simple_ddl_parser import DDLParser
from openpyxl import Workbook
import json

with open('ddl.sql', 'r') as file:
    ddl = file.read()

parser = DDLParser(ddl)
table_data = parser.run()

wb = Workbook()
table_sheet = None

for item in table_data:
    if table_sheet is None:
        table_sheet = wb.active
        table_sheet.title = item['table_name']
    else:
      table_sheet = wb.create_sheet(title=item['table_name'])
    table_sheet.append(["column name", "type", "size", "nullable", "default", "description"])

    for column in item['columns']:
        print(column)
        row = [str(column['name']), str(column['type']), str(column['size']), str(column['nullable']), str(column['default'])]
        table_sheet.append(row)

wb.save("dcr.xlsx")
