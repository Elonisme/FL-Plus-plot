import matplotlib.pyplot as plt
import numpy as np

# 两组示例数据
x = [0, 20, 40, 60, 80, 90]

data = {
    'FedAvg': [0.9728,0.9721,0.9718,0.9697,0.9704,0.9685],
    'FL-PLAS': [0.939339,0.9397,0.939391667,0.939065,0.93844,0.94006],
    'FLTrust': [0.9586,0.9573,0.9572,0.9572,0.9555,0.9531],
    'FLAME': [0.9698,0.97,0.9718,0.9666,0.9671,0.9667],
    'RSA': [0.9613,0.9596,0.9559,0.9487,0.9289,0.916],
    'Krum': [0.9484,0.9479,0.9468,0.9492,0.9219,0.9388],
    'NDC': [0.9694,0.9689,0.9691,0.9665,0.9658,0.9664],
    'Lfighter': [0.9897, 0.9896, 0.8888, 0.8886, 0.8892, 0.8882],
}

# 设置Y轴刻度间距为0.2递增，同时显示1的刻度
plt.yticks(np.arange(0.85, 1.01, 0.02))

# 设置X轴刻度显示90
plt.xticks(np.array([0,20,40,60,80, 90]))

# 绘制折线图
markers = ['o', '^', 's', 'D', 'v', '*', 'x', '+']
for label, values, marker in zip(data.keys(), data.values(), markers):
    plt.plot(x, values, marker=marker, label=label)

# 添加标题和标签
plt.title('MA of MNIST in trigger attack')
plt.xlabel('malicious ratio')
plt.ylabel('MA')

plt.savefig('MAmnist.pdf')
# 显示图形
plt.show()
