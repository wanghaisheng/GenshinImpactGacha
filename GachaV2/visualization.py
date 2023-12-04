"""
本程序用于实现抽卡结果的可视化
"""

import matplotlib.pyplot as plt
# 导入数据可视化matplotlib.pyplot模块用于数据可视化

from pylab import mpl
# 导入该模块用于设置可视化图标中的中文显示字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]


def visualization(list_chara,list_num):
    # 先将数据处理为x，y轴上的数据
    x_data = list_chara
    y_data_pre = list_num
    y_data = [y_data_pre[0]]
    for i in range(0,len(y_data_pre)-1):
        y_data.append(y_data_pre[i + 1] - y_data_pre[i])

    # 开始绘图
    plt.bar(x= x_data, height= y_data, label= '使用抽数', color= ['r','b','y'])
    plt.title('模拟器抽卡分析')
    plt.xlabel('角色')
    plt.ylabel('抽数')
    plt.legend()

    # 输出结果
    plt.savefig('result.jpg')
    plt.show()