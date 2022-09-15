from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference

data = [['品类', '销售额'], ['布匹', 4897], ['米面', 4580], ['副食', 2340], ['水果', 1209], ['粮油', 1439]]

wb = Workbook()
ws = wb.active

for row in data:
    ws.append(row)

pie = PieChart()
pie.title = "居民消费占比"
labels = Reference(ws, min_col=1, min_row=2, max_row=6)
data = Reference(ws, min_col=2, min_row=1, max_row=6)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)

ws.add_chart(pie, "E1")

wb.save('./demo.xlsx')
