import matplotlib.pyplot as plt
import numpy as np

# 两组示例数据
x = [0, 20, 40, 60, 80, 90]

data = {
    'FedAvg': [0.79,0.78,0.76,0.73,0.69,0.65],
    'FL-PLAS': [0.79, 0.79, 0.78, 0.78, 0.77, 0.76],
    'FLTrust': [0.79, 0.79, 0.79, 0.79, 0.79, 0.79],
    'FLAME': [0.79, 0.78, 0.781, 0.72, 0.72, 0.72],
    'RSA': [0.79,0.76,0.72,0.65,0.54,0.44],
    'Krum': [0.79,0.78,0.78,0.78,0.78,0.68],
    'NDC': [0.79,0.79,0.76,0.73,0.68,0.66],
    'Lfighter': [0.7423, 0.7365, 0.7313, 0.6711, 0.7091, 0.6975],
}


# 设置Y轴刻度间距为0.2递增，同时显示1的刻度
plt.yticks(np.arange(0.45, 0.85, 0.05))

# 设置X轴刻度显示90
plt.xticks(np.array([0,20,40,60,80, 90]))

# 绘制折线图
markers = ['o', '^', 's', 'D', 'v', '*', 'x', '+']
for label, values, marker in zip(data.keys(), data.values(), markers):
    plt.plot(x, values, marker=marker, label=label)

# 添加标题和标签
plt.title('MA of CIFAR-10 in trigger attack')
plt.xlabel('malicious ratio')
plt.ylabel('MA')

plt.savefig('MAcifar10.pdf')
# 显示图形
plt.show()
