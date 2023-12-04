import random


txtUP5 = open('listUP5_f.txt','r',encoding='utf-8')
lineSUP5 = txtUP5.readlines()
listUP5 = []
for elementUP5 in lineSUP5:
    elementUP5 = elementUP5.strip("\n")
    listUP5.append(elementUP5)


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



def A1(i,j,b):#A1函数用于计算四星抽数<10且五星抽数<=70时的情况（小保底）
    a = random.randint(1,1000000)#生成随机数表来表示概率
    i1 = i
    j1 = j
    b1 = b
    if a in range(1,6001):#模拟出五星情况 0.6
        if a in range(1,3001):#模拟UP五星 0.3
            result = random.choices(listUP5, k=1)
            i1 = 1
            j1 = 1
            b1 = 0
        elif a in range(3001,6001):#模拟歪常驻5星 0.3
            result = random.choices(listCZ5, k=1)
            i1 = 1
            j1 = 1
            b1 = 1
    elif a in range(6001,57001):#模拟出四星情况 5.1
        if a in range(6001,44251):#模拟UP4星 3.825
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(44251,50626):#模拟4星角色 0.6375
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(50626,57001):#模拟4星武器 0.6375
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
    elif a in range(57001,1000001):#模拟3星角色 94.3
        result = random.choices(listCZ3, k=1)
        i1 += 1
        j1 += 1
    return i1, j1, b1, result


def A2(i,j,b):#A2函数用于计算四星抽数=10且五星抽数<=70的情况（小保底）
    a = random.randint(1, 1000001)  # 生成随机数表来表示概率
    i1 = i
    j1 = j
    b1 = b
    if a in range(1,6001):#模拟出五星情况 0.6
        if a in range(1,3001):#模拟UP五星 0.3
            result = random.choices(listUP5, k=1)
            i1 = 1
            j1 = 1
            b1 = 0
        elif a in range(3001,6001):#模拟歪常驻5星 0.3
            result = random.choices(listCZ5, k=1)
            i1 = 1
            j1 = 1
            b1 = 1
    elif a in range(6001,1000001):#模拟出四星情况 99.4
        if a in range(6001,751501):#模拟UP4星 74.55
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(751501,875751):#模拟4星角色 12.425
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(875751,1000001):#模拟4星武器 12.425
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
    return i1, j1, b1, result


def A3(i,j,b):#A3函数用于计算四星抽数<10且五星抽数<=70的情况（大保底）
    a = random.randint(1, 1000000)  # 生成随机数表来表示概率
    i1 = i
    j1 = j
    b1 = b
    if a in range(1, 6001):  # 模拟出五星情况 0.6
        result = random.choices(listUP5, k=1)
        i1 = 1
        j1 = 1
        b1 = 0
    elif a in range(6001, 57001):  # 模拟出四星情况 5.1
        if a in range(6001, 44251):  # 模拟UP4星 3.825
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(44251, 50626):  # 模拟4星角色 0.6375
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(50626, 57001):  # 模拟4星武器 0.6375
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
    elif a in range(57001, 1000001):  # 模拟3星武器 94.3
        result = random.choices(listCZ3, k=1)
        i1 += 1
        j1 += 1
    return i1, j1, b1, result


def A4(i,j,b):#A4函数用于计算四星抽数=10且五星抽数<=70的情况（大保底）
    a = random.randint(1, 1000000)  # 生成随机数表来表示概率
    i1 = i
    j1 = j
    b1 = b
    if a in range(1, 6001):  # 模拟出五星情况 0.6
        result = random.choices(listUP5, k=1)
        i1 = 1
        j1 = 1
        b1 = 0
    elif a in range(6001, 1000001):  # 模拟出四星情况 99.4
        if a in range(6001, 751501):  # 模拟UP4星 74.55
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 +=1
        elif a in range(751501, 875751):  # 模拟4星角色 12.425
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        elif a in range(875751, 1000001):  # 模拟4星武器 12.425
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
    return i1, j1, b1, result


def B1(i,j,b,probability):#B1函数用于计算五星抽数>70的情况（小保底）
    a = random.randint(1, 1000000)  # 生成随机数表来表示概率
    i1 = i
    j1 = j
    b1 = b
    probability = probability
    if a in range(1,probability+1):#模拟出五星情况
        if a in range(1,(probability//2)+1):#模拟UP五星
            result = random.choices(listUP5, k=1)
            i1 = 1
            j1 = 1
            b1 = 0
        if a in range((probability//2)+1,probability+1):#模拟常驻五星
            result = random.choices(listCZ5, k=1)
            i1 = 1
            j1 = 1
            b1 = 1
    elif a in range(probability+1,probability+51001):
        if a in range(probability+1,probability+38251):#模拟UP4星
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        if a in range(probability+38251,probability+44626):#模拟4星角色
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        if a in range(probability+44626,probability+51001):#模拟4星武器
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
        probability = probability + 50000
    elif a in range(probability+51001,1000001):#模拟3星武器
        result = random.choices(listCZ3, k=1)
        i1 += 1
        j1 += 1
        probability = probability + 50000
    return i1, j1, b1, result,probability


def B2(i,j,b,probability):#B1函数用于计算五星抽数>70的情况（大保底）
    a = random.randint(1, 1000000)  # 生成随机数表来表示概率
    i1 = i
    j1 = j
    b1 = b
    probability = probability
    if a in range(1,probability+1):#模拟出五星情况
        result = random.choices(listUP5, k=1)
        i1 = 1
        j1 = 1
        b1 = 0
    elif a in range(probability+1,probability+51001):
        if a in range(probability+1,probability+38251):#模拟UP4星
            result = random.choices(listUP4, k=1)
            i1 = 1
            j1 += 1
        if a in range(probability+38251,probability+44626):#模拟4星角色
            result = random.choices(listCH4, k=1)
            i1 = 1
            j1 += 1
        if a in range(probability+44626,probability+51001):#模拟4星武器
            result = random.choices(listWP4, k=1)
            i1 = 1
            j1 += 1
        probability = probability + 50000
    elif a in range(probability+51001,1000001):#模拟3星武器
        result = random.choices(listCZ3, k=1)
        i1 += 1
        j1 += 1
        probability = probability + 50000
    return i1, j1, b1, result,probability


def main():
    i = 1
    j = 1
    b = 0
    probability = 50000
    while True:
        times = int(input("请输入抽卡的次数"))
        for m in range(times):
            if i<10 and j<=70 and b==0:
                i,j,b,result = A1(i,j,b)
            elif i>=10 and j<=70 and b==0:
                i,j,b,result = A2(i,j,b)
            elif i<10 and j<=70 and b==1:
                i,j,b,result = A3(i,j,b)
            elif i>=10 and j<=70 and b==1:
                i,j,b,result = A4(i,j,b)
            elif j>70 and b==0:
                i,j,b,result,probability = B1(i,j,b,probability)
            elif j>70 and b==1:
                i,j,b,result,probability = B2(i,j,b,probability)
            print(m+1,result)
        con = input("继续抽卡还是结束抽卡？（若继续输入”是“，若结束输入”否“）")
        if con == "是":
            continue
        if con == "否":
            break


input("本程序用于模拟游戏“原神”的角色卡池抽卡情况，其机制如下：\n"
      "1.每10次抽卡，至少一次获得4星角色\n"
      "2.前70次抽卡，5星角色获得概率为0.6%，每次获得5星角色有50%的概率会出常驻5星角色，有50%概率出UP5星角色\n"
      "3.前70次抽卡，4星角色获得概率为5.1%，每次获得4星角色会有75%的概率出UP4星角色，25%概率出其他4星角色\n"
      "4.从第71次抽卡开始，每次获得5星角色的概率提升，第90抽时，5星角色出率达到100%\n"
      "5.每次获得非UP5星角色（即获得常驻5星角色）后，下次获得5星角色必为UP5星角色\n"
      "6.本次V3.2.1.1版本模拟器：UP5星角色为”5星角色纳西妲“\n"
      "按下Enter开始抽卡")



if __name__ == '__main__':
    main()