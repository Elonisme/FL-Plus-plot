import matplotlib.pyplot as plt
import numpy as np

x = [0, 20, 40, 60, 80, 90]

data = {
    'FedAvg': [0.1, 0.13, 0.18, 0.22, 0.29, 0.35],
    'FL-PLAS': [0.1, 0.08, 0.08, 0.08, 0.07, 0.05],
    'FLTrust': [0.1, 0.1, 0.1, 0.1, 0.11, 0.11],
    'FLAME': [0.1, 0.1, 0.1, 0.21, 0.21, 0.21],
    'RSA': [0.1, 0.11, 0.16, 0.21, 0.44, 0.59],
    'Krum': [0.1, 0.1, 0.1, 0.11, 0.13, 0.29],
    'NDC': [0.1, 0.12, 0.17, 0.22, 0.29, 0.33],
    'Lfighter': [0.105, 0.128, 0.131, 0.838, 0.826, 0.832],
}


# 设置Y轴刻度间距为0.2递增，同时显示1的刻度
# plt.yticks(np.array([0.2,0.4,0.6,0.8, 1]))

# 设置X轴刻度显示90
plt.xticks(np.array([0,20,40,60,80, 90]))

# 绘制折线图
markers = ['o', '^', 's', 'D', 'v', '*', 'x', '+']
for label, values, marker in zip(data.keys(), data.values(), markers):
    plt.plot(x, values, marker=marker, label=label)

# 添加标题和标签
plt.title('BA of CIFAR-10 in trigger attack')
plt.xlabel('malicious ratio')
plt.ylabel('BA')

plt.savefig('BAcifar10.pdf')
# 显示图形
plt.show()
