"""
本程序用于实现抽卡程序的图形界面
"""
import tkinter as tk
# 导入tkinter用于实现GUI编程

import tkinter.messagebox as tkm
# 导入该模块，使用showinfo函数来实现GUI结果显示

import gacha
# 导入用于实现抽卡的gacha模块，调用gacha模块下的三个类Pool, Recording, Crow

import visualization
# 导入用于实现数据可视化的visualization模块

class GUI_main:
    """
    利用GUI图形界面编程实现原main函数的功能
    """

    def __init__(self):
        """
        初始化类，获取gacha模块内的抽卡信息，同时初始化GUI的一些基本元素
        """
        self.R = gacha.Recording()
        self.C = gacha.Crow(self.R)


        self.main_window = tk.Tk
        self.first_frame = tk.Frame()
        self.top_frame = tk.Frame()
        self.bottom_frame = tk.Frame()

        self.label1 = tk.Label(self.first_frame,    # 以下为显示在主界面上的内容
                               text=
'''
本程序用于简单模拟游戏原神3.5版本的抽卡系统。并且在获得抽卡数据后进行数据分析。

首先，其抽卡机制如下：
1.卡池内的奖励分3个等级：
（1）3星：共13种
（2）4星：共47种
（3）5星：共7种
2.其中，每个卡池内会有3种4星奖励获取概率提升与1种5星奖励获取概率提升。
3.卡池的基本概率如下：
（1）5星奖励的获取概率为0.6%。当获取5星奖励时，又有50%的可能性获得概率提升5星奖励
（2）4星奖励的获取概率为5.1%。当获取4星奖励时，又有50%的可能性获得概率提升4星奖励
（3）3星奖励的获取概率为94.3%
4.在基本概率之上，卡池内又具有保底机制：
（1）每10抽必定获得一个4星奖励
（2）从第70抽开始，每抽一次，5星奖励获取概率便会将对应地提升一次，当到达第90抽时，5星奖励地获取概率将提升至100%
（3）每获得一次5星奖励，若该奖励不是获取概率提升的5星奖励，则当下次获取五星奖励时，必定获得概率提升的五星奖励。
（4）由于上述保底机制存在，卡池概率将会随实际情况，在基本概率的基础上波动。
5.本程序用于模拟游戏原神3.5版本下半角色祈愿-2卡池：
（1）概率提升的5星奖励为“☆5神里绫华UP!”
（2）概率提升的4星奖励为“☆4迪奥娜UP!、☆4砂糖UP!、☆4米卡UP!”

其次，其数据分析机制如下：
1.程序将记录您的抽卡记录，并且返回两个主要数据
（1）您在获得5星奖励时，耗费了多少抽
（2）您在获得5星奖励时，获得的是什么五星奖励
（3）以“获得的是什么五星奖励”为横坐标轴，以“耗费了多少抽”纵坐标轴，绘制柱状图
注：也就是说，在您获得五星角色之前，若选择选项3，将不会执行任何操作。

最后，简述一下该界面的使用方法：
1.该界面拥有3个选项，分别对应
（1）抽卡一次
（2）抽卡十次
（3）获得抽卡结果分析图
2.选择后，按下“完成选择按钮”，将会返回输出结果
3.若要退出程序，直接按“×”退出即可
'''
                               ,
                               borderwidth= 1,
                               relief= 'solid')
        self.label1.pack(side= 'left',padx= 100, pady= 100)
        self.first_frame.pack()

        self.radio_var = tk.IntVar()

        self.radio_var.set(1)

        self.rb1 = tk.Radiobutton(self.top_frame,
                                  text='单抽',
                                  variable=self.radio_var,
                                  value=1)

        self.rb2 = tk.Radiobutton(self.top_frame,
                                  text='十连抽',
                                  variable=self.radio_var,
                                  value=2)
        self.rb3 = tk.Radiobutton(self.top_frame,
                                  text='获取抽卡结果图',
                                  variable=self.radio_var,
                                  value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tk.Button(self.bottom_frame,
                                   text='完成选择',
                                   command=self.show)

        self.ok_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def show(self):
        """
        实现选项背后的运行
        """
        if self.radio_var.get() == 1:
            tkm.showinfo('结果',self.C.pray_once())
        elif self.radio_var.get() == 2:
            tkm.showinfo('结果',self.C.pray_tenth())
        elif self.radio_var.get() == 3:
           visualization.visualization(self.R.result_chara,self.R.result_num)


if __name__ == '__main__':
    MyGUI = GUI_main()

