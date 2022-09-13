import xlwings as xw

path = './demo.xlsx'
"""
# 基础操作

# 创建
wb = xw.Book()
wb.save(path)
wb.close()

# 元数据
wb = xw.Book(path)
print(wb.fullname)

sht = wb.sheets["Sheet1"]
print(sht.name)

print(sht.range('A1').row_height)
print(sht.range('A1').column_width)

# 写数据
sht.range('A1').value = ['A', 'B', 'C', 'D']
sht.range('A2').value = [['赵六', '25', '1', '深圳'], ['钱七', '35', '1', '深圳']]

# 读数据

print(sht.range('A1').value)
print(sht.range('A1:C2').value)

# 行高自适应
sht.range('A2').rows.autofit()
# 列宽自适应
sht.range('A2').columns.autofit()
# 单于昂背景色
sht.range('A1').color = (255, 0, 0)

"""
# 可视化

import matplotlib.pyplot as plt

wb = xw.Book(path)
sht = wb.sheets["Sheet1"]
fig = plt.figure()
plt.plot([10, 20, 30, 40, 50])
plt.plot([46, 12, 66, 29, 17])
sht.pictures.add(fig, name='MyPlot', update=True)
