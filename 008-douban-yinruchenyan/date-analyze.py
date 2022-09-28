import pandas as pd, matplotlib.pyplot as plt

csv_data = pd.read_csv('data.csv')
df = pd.DataFrame(csv_data)
df_gp = df.groupby(['time']).size()
index = df_gp.index.tolist()

values = [value[5:10] for value in index if value > '2022-06-01']
result = pd.value_counts(values).to_dict()
result = sorted(result.items(), key=lambda v: v[0])
result = dict(result)
x = list(result.keys())
y = list(result.values())
fig = plt.figure(figsize=(16, 6))  # 设置画布大小
plt.plot(x, y, '-*r')
plt.xticks(rotation=270)
plt.show()
