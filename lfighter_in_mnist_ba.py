import matplotlib.pyplot as plt
import numpy as np

x = [0, 20, 40, 60, 80, 90]

data = {
    'FedAvg': [0.0992, 1, 1, 1, 1, 1],
    'FL-PLAS': [0.0993,0.1013,0.1015,0.1014,0.1016,0.1013],
    'FLTrust': [0.0992,0.1015,0.1024,0.1029,0.1026,0.1034],
    'FLAME': [0.0994,0.1002,0.0998,1,1,1],
    'RSA': [0.0997,0.1033,0.1129,0.157,0.2624,0.3421],
    'Krum': [0.0992,0.1013,0.1017,0.1009,0.9857,1],
    'NDC': [0.0992,0.2947,1,1,1,1],
    'Lfighter': [0.19, 0.29, 0.9708, 0.9805, 0.9844, 0.9874],
}

# 设置Y轴刻度间距为0.2递增，同时显示1的刻度
plt.yticks(np.array([0.2,0.4,0.6,0.8, 1]))

# 设置X轴刻度显示90
plt.xticks(np.array([0,20,40,60,80, 90]))

# 绘制折线图
markers = ['o', '^', 's', 'D', 'v', '*', 'x', '+']
for label, values, marker in zip(data.keys(), data.values(), markers):
    plt.plot(x, values, marker=marker, label=label)

# 添加标题和标签
plt.title('BA of MNIST in trigger attack')
plt.xlabel('malicious ratio')
plt.ylabel('BA')

plt.savefig('BAmnist.pdf')
# 显示图形
plt.show()