import pandas as pd, numpy as np, matplotlib.pyplot as plt

csv_data = pd.read_csv('data.csv')
df_time = csv_data.groupby(['time']).size()
df_star = csv_data.groupby(['star']).size()
index = df_time.index.tolist()
value = [0] * len(index)
# 生成字典
dic = dict(zip(index, value))
result = {}
for k, v in dic.items():
    key = k[:10]
    if key > '2022-06-01':
        stars = csv_data.loc[csv_data['time'] == str(k), 'star']
        # 平均值
        avg = np.mean(list(map(int, stars.values.tolist())))
        result[key] = round(avg, 2)

x = [x[5:10] for x in list(result.keys())]
y = [int(y) for y in result.values()]

fig = plt.figure(figsize=(16, 6))  # 设置画布大小
plt.plot(x, y, '-*r')
plt.xticks(rotation=270)
plt.show()
