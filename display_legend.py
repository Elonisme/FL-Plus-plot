import matplotlib.pyplot as plt

markers = ['o', '^', 's', 'D', 'v', '*', 'x', '+']
name = [
    'FedAvg',
    'FL-PLAS',
    'FLTrust',
    'FLAME',
    'RSA',
    'Krum',
    'NDC',
    'Lfighter',
]
# 创建一个空的图例
fig, ax = plt.subplots()

# 将每个标记添加到图例中，同时设置 linestyle 为空字符串
for indx, marker in enumerate(markers):
    line, = ax.plot([], [], marker=marker, linestyle='', label=f'{name[indx]}')

# 设置图例的显示样式，横向显示
ax.legend(loc='upper left', bbox_to_anchor=(0, 1.15), ncol=len(markers),frameon=False)

# 关闭坐标轴显示
ax.axis('off')
# 保存图例为 PDF 文件
plt.savefig('legend.pdf', format='pdf', bbox_inches='tight')
# 显示图例
plt.show()
