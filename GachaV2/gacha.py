"""
本程序用于构建实现抽卡模块gacha的三个主要类 Pool, Recording和Crow
"""

import random
# 导入内置random模块实现抽卡

import decode
# 导入decode模块解码储存在文件中的角色卡池数据



class Pool:
    """
    Pool类用于初始化卡池，创捷概率字典
    """
    def __init__(self):
        """
        初始化卡池
        """
        self.FiveStar = decode.txt5()
        self.FourStar = decode.txt4()
        self.ThreeStar = decode.txt3()

    @staticmethod
    def analysis(r):
        """
        解析水位生成概率数据
        """
        probability = {'Five': None, 'Four': None, 'Three': None}
        if r.Five <= 70:                                                # 70发以前概率一律为0.6
            probability['Five'] = 0.60
        else:
            probability['Five'] = 5 * (r.Five - 70)                     # 70发以后每一次增加
        if r.Four < 8:                                                  # 8发以前四星一直为5.10
            probability['Four'] = 5.10
        elif probability['Five'] == 100.00:                             # 如果五星水满四星让位
            probability['Four'] = 0.00
        elif r.Four == 8:
            probability['Four'] = 56.10
        else:
            probability['Four'] = (10000 - int(probability['Five'] * 100)) / 100          # 给五星让位
        if r.Four == 10:                                                                  # 四星水满五星让位
            probability['Four'] = 100.00
            probability['Five'] = 0.00

        probability['Three'] = (10000 - int(probability['Five'] * 100) - int(probability['Four'] * 100)) / 100
        return probability


class Recording:
    """
    Recording类用于更新水位，记录抽卡结果
    """

    def __init__(self):
        """初始化水位"""
        self.Five = 0
        self.Four = 0
        self.FiveFlag = False
        self.FourFlag = False
        self.result_chara = []
        self.result_num = []
        self.index = 0

    def update(self,result,pool):
        """
        更新水位,且记录结果
        """
        self.index += 1
        if result in pool.FiveStar:
            self.Five = 0
            self.Four += 1
            self.result_num.append(self.index)
            self.result_chara.append(str(self.index) + ' ' + result)
            if result != pool.FiveStar[0]:
                self.FiveFlag = True
            else:
                self.FiveFlag = False
        elif result in pool.FourStar:
            self.Five += 1
            self.Four = 0
            if result not in pool.FourStar[0:3]:
                self.FourFlag = True
            else:
                self.FourFlag = False
        elif result in pool.ThreeStar:
            self.Five += 1
            self.Four += 1


class Crow():
    """
    Crow类用于实现抽卡与保底机制
    """
    def __init__(self, record):
        """
        初始化卡池,获得记录对象
        """
        self.pool = Pool()
        self.record = record
        self.Recording = Recording()

    def pray(self):
        """
        决定是几星
        """
        probability = self.pool.analysis(self.record)
        seed = random.randint(0, 10000) / 100
        state = 0.00
        for i, j in probability.items():
            state += j
            if seed <= state:
                result = i
                break
        return self.pray2(result)

    def pray2(self,r):
        """
        决定歪不歪
        """
        if r == 'Five':
            if random.randint(1,2) == 1 or self.record.FiveFlag:
                result = self.pool.FiveStar[0]
            else:
                result = self.pool.FiveStar[random.randint(1,len(self.pool.FiveStar)-1)]
        elif r == 'Four':
            if random.randint(1,2) == 1 or self.record.FourFlag:
                result = self.pool.FourStar[random.randint(0,2)]
            else:
                result = self.pool.FourStar[random.randint(3,len(self.pool.FourStar)-1)]
        elif r == 'Three':
            result = self.pool.ThreeStar[random.randint(0,len(self.pool.ThreeStar)-1)]
        print(result)
        return result

    def pray_once(self):
        """
        单抽
        """
        result = self.pray()
        self.record.update(result, self.pool)
        return result

    def pray_tenth(self):
        """
        十连
        """
        record_str = ''
        for i in range(10):
            result = self.pray()
            self.record.update(result, self.pool)
            record_str = record_str + result + '\n'
        return record_str
