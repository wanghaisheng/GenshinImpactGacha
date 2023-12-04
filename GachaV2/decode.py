"""
本代码解包储存在文件中的角色数据库
"""


def txt5():
    """
    解包五星文件
    """
    txt5 = open('Fivestars.txt','r',encoding='utf-8')
    # 解包5星角色文件，以utf-8方式解码，打开文件
    lineS5 = txt5.readlines()
    list5 = []
    for element5 in lineS5:
        element5 = element5.strip("\n")
        list5.append(element5)
        txt5.close()
        # 将文件内内容文件转为列表，供抽卡函数调用
    return list5


def txt4():
    """
    解包四星文件
    """
    txt4 = open('Fourstars.txt','r',encoding='utf-8')
    # 解包4星角色文件
    lineS4 = txt4.readlines()
    list4 = []
    for element4 in lineS4:
        element4 = element4.strip("\n")
        list4.append(element4)
        txt4.close()
    return list4


def txt3():
    """
    解包三星文件
    """
    txt3 = open('Threestars.txt','r',encoding='utf-8')
    # 解包常驻3星角色文件
    lineS3 = txt3.readlines()
    list3 = []
    for element3 in lineS3:
        element3 = element3.strip("\n")
        list3.append(element3)
        txt3.close()
    return list3