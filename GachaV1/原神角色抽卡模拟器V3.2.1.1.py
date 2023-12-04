import random
# 引入随机数模块来实现随机抽卡

txtUP5 = open('listUP5_f.txt','r',encoding='utf-8')
# 以utf-8方式解码（含有@字符，用utf-8而非gbk），打开文件
lineSUP5 = txtUP5.readlines()
listUP5 = []
for elementUP5 in lineSUP5:
    elementUP5 = elementUP5.strip("\n")
    listUP5.append(elementUP5)
# 将文件内内容文件转为列表，供后续抽卡函数调用。
# 后续5个代码段同理，可以使用for循环优化

txtCZ5 = open('listCZ5_f.txt','r',encoding='utf-8')
lineSCZ5 = txtCZ5.readlines()
listCZ5 = []
for elementCZ5 in lineSCZ5:
    elementCZ5 = elementCZ5.strip("\n")
    listCZ5.append(elementCZ5)


txtUP4 = open('listUP4_f.txt','r',encoding='utf-8')
lineSUP4 = txtUP4.readlines()
listUP4 = []
for elementUP4 in lineSUP4:
    elementUP4 = elementUP4.strip("\n")
    listUP4.append(elementUP4)


txtCH4 = open('listCH4_f.txt','r',encoding='utf-8')
lineSCH4 = txtCH4.readlines()
listCH4 = []
for elementCH4 in lineSCH4:
    elementCH4 = elementCH4.strip("\n")
    listCH4.append(elementCH4)


txtWP4 = open('listWP4_f.txt','r',encoding='utf-8')
lineSWP4 = txtWP4.readlines()
listWP4 = []
for elementWP4 in lineSWP4:
    elementWP4 = elementWP4.strip("\n")
    listWP4.append(elementWP4)


txtCZ3 = open('listCZ3_f.txt','r',encoding='utf-8')
lineSCZ3 = txtCZ3.readlines()
listCZ3 = []
for elementCZ3 in lineSCZ3:
    elementCZ3 = elementCZ3.strip("\n")
    listCZ3.append(elementCZ3)



def A1(i,j,b):
    # A1函数用于计算四星抽数<10且五星抽数<=70时的情况（小保底）
    a = random.randint(1,1000000)
    # 生成随机数表来表示概率
    i1 = i
    j1 = j
    b1 = b
    # 分别用于标记，四星保底，五星小保底，五星大保底
    if a in range(1,6001):
        # 模拟出五星情况 概率为0.6%
        if a in range(1,3001):
            # 模拟UP五星 概率为0.3%
            result = random.choices(listUP5, k=1)
            # 随机从listUP5列表内抽取一个对象，result变量引用该对象
            i1 = 1
            j1 = 1
            b1 = 0
            # 标记保底情况
        elif a in range(3001,6001):
            # 模拟歪常驻5星 概率为0.3%
            result = random.choices(listCZ5, k=1)
            i1 = 1
            j1 = 1
            b1 = 1
    elif a in range(6001,57001):
        # 模拟出四星情况 概率为5.1%
        if a in range(6001,44251):
            # 模拟UP4星 概率为3.825%
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(44251,50626):
            # 模拟4星角色 概率为0.6375%
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(50626,57001):
            # 模拟4星武器 概率为0.6375%
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
    elif a in range(57001,1000001):
        # 模拟3星角色 概率为94.3%
        result = random.choices(listCZ3, k=1)
        i1 += 1
        j1 += 1
    return i1, j1, b1, result
    # 返回本次抽卡结果与保底情况


def A2(i,j,b):
    # A2函数用于计算四星抽数=10且五星抽数<=70的情况（小保底）
    a = random.randint(1, 1000000)
    i1 = i
    j1 = j
    b1 = b
    if a in range(1,6001):
        # 模拟出五星情况 概率为0.6%
        if a in range(1,3001):
            # 模拟UP五星 概率为0.3%
            result = random.choices(listUP5, k=1)
            i1 = 1
            j1 = 1
            b1 = 0
        elif a in range(3001,6001):
            # 模拟歪常驻5星 概率为0.3%
            result = random.choices(listCZ5, k=1)
            i1 = 1
            j1 = 1
            b1 = 1
    elif a in range(6001,1000001):
        # 模拟出四星情况 概率为99.4%
        if a in range(6001,751501):
            # 模拟UP4星 概率为74.55%
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(751501,875751):
            # 模拟4星角色 概率为12.425%
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(875751,1000001):
            # 模拟4星武器 概率为12.425%
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
    return i1, j1, b1, result


def A3(i,j,b):
    # A3函数用于计算四星抽数<10且五星抽数<=70的情况（大保底）
    a = random.randint(1, 1000000)
    i1 = i
    j1 = j
    b1 = b
    if a in range(1, 6001):  # 模拟出五星情况 概率为0.6%
        result = random.choices(listUP5, k=1)
        i1 = 1
        j1 = 1
        b1 = 0
    elif a in range(6001, 57001):  # 模拟出四星情况 概率为5.1%
        if a in range(6001, 44251):  # 模拟UP4星 概率为3.825%
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(44251, 50626):  # 模拟4星角色 概率为0.6375%
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(50626, 57001):  # 模拟4星武器 概率为0.6375%
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
    elif a in range(57001, 1000001):  # 模拟3星武器 概率为94.3%
        result = random.choices(listCZ3, k=1)
        i1 += 1
        j1 += 1
    return i1, j1, b1, result


def A4(i,j,b):
    # A4函数用于计算四星抽数=10且五星抽数<=70的情况（大保底）
    a = random.randint(1, 1000000)
    i1 = i
    j1 = j
    b1 = b
    if a in range(1, 6001):  # 模拟出五星情况 概率为0.6%
        result = random.choices(listUP5, k=1)
        i1 = 1
        j1 = 1
        b1 = 0
    elif a in range(6001, 1000001):  # 模拟出四星情况 概率为99.4%
        if a in range(6001, 751501):  # 模拟UP4星 概率为74.55%
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 +=1
        elif a in range(751501, 875751):  # 模拟4星角色 概率为12.425%
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(875751, 1000001):  # 模拟4星武器 概率为12.425%
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
    return i1, j1, b1, result


def B1(i,j,b,probability):
    # B1函数用于计算五星抽数>70的情况（小保底）
    a = random.randint(1, 1000000)
    i1 = i
    j1 = j
    b1 = b
    probability = probability
    if a in range(1,probability+1):
        # 模拟出五星情况
        if a in range(1,(probability//2)+1):
            # 模拟UP五星
            result = random.choices(listUP5, k=1)
            i1 = 1
            j1 = 1
            b1 = 0
        if a in range((probability//2)+1,probability+1):
            # 模拟常驻五星
            result = random.choices(listCZ5, k=1)
            i1 = 1
            j1 = 1
            b1 = 1
    elif a in range(probability+1,probability+51001):
        if a in range(probability+1,probability+38251):
            # 模拟UP4星
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        if a in range(probability+38251,probability+44626):
            # 模拟4星角色
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        if a in range(probability+44626,probability+51001):
            # 模拟4星武器
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
        probability = probability + 50000
    elif a in range(probability+51001,1000001):
        # 模拟3星武器
        result = random.choices(listCZ3, k=1)
        i1 += 1
        j1 += 1
        probability = probability + 50000
    return i1, j1, b1, result,probability


def B2(i,j,b,probability):
    # B2函数用于计算五星抽数>70的情况（大保底）
    a = random.randint(1, 1000000)
    i1 = i
    j1 = j
    b1 = b
    probability = probability
    if a in range(1,probability+1):
        # 模拟出五星情况
        result = random.choices(listUP5, k=1)
        i1 = 1
        j1 = 1
        b1 = 0
    elif a in range(probability+1,probability+51001):
        if a in range(probability+1,probability+38251):
            # 模拟UP4星
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        if a in range(probability+38251,probability+44626):
            # 模拟4星角色
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        if a in range(probability+44626,probability+51001):
            # 模拟4星武器
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
        probability = probability + 50000
    elif a in range(probability+51001,1000001):
        # 模拟3星武器
        result = random.choices(listCZ3, k=1)
        i1 += 1
        j1 += 1
        probability = probability + 50000
    return i1, j1, b1, result,probability


def main():
    i = 1
    j = 1
    b = 0
    # 初始化保底数，注意程序流程，此处关于四星保底与小保底应当从1开始计数
    probability = 50000
    # 初始化概率，用于计算从70抽开始时的概率提升
    while True:
        # 此语句会无限循环直至使用break语句跳出循环
        times = int(input("请输入抽卡的次数"))
        for m in range(times):
            # 循环用户需要的次数
            if i<10 and j<=70 and b==0:
                # 无四星保底，概率不提升，且无大保底
                i,j,b,result = A1(i,j,b)
            elif i>=10 and j<=70 and b==0:
                # 有四星保底，概率不提升，且无大保底
                i,j,b,result = A2(i,j,b)
            elif i<10 and j<=70 and b==1:
                # 无四星保底，概率不提升，且有大保底
                i,j,b,result = A3(i,j,b)
            elif i>=10 and j<=70 and b==1:
                # 有四星保底，概率不提升，且有大保底
                i,j,b,result = A4(i,j,b)
            elif j>70 and b==0:
                # 概率提升，且无大保底
                i,j,b,result,probability = B1(i,j,b,probability)
            elif j>70 and b==1:
                # 概率提升，且有大保底
                i,j,b,result,probability = B2(i,j,b,probability)
            print(m+1,result)
            # 显示结果，并且显示对应的抽数
        con = input("继续抽卡还是结束抽卡？（若继续输入”是“，若结束输入”否“）")
        # 判断是否继续运行程序
        if con == "是":
            continue
        if con == "否":
            break


print("本程序用于模拟游戏“原神”的角色卡池抽卡情况，其机制如下：")
print("1.每10次抽卡，至少一次获得4星角色")
print("2.前70次抽卡，5星角色获得概率为0.6%，每次获得5星角色有50%的概率会出常驻5星角色，有50%概率出UP5星角色")
print("3.前70次抽卡，4星角色获得概率为5.1%，每次获得4星角色会有75%的概率出UP4星角色，25%概率出其他4星角色")
print("4.从第71次抽卡开始，每次获得5星角色的概率提升，第90抽时，5星角色出率达到100%")
print("5.每次获得非UP5星角色（即获得常驻5星角色）后，下次获得5星角色必为UP5星角色")
print("6.本次V3.2.1.1版本模拟器：UP5星角色为”5星角色纳西妲”")
print("下面开始抽卡\n")


if __name__ == '__main__':
    main()
