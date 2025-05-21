import random

class Pages:

    __version__ = 'idk'

    # 书页规范 | 名称,消耗光芒,品质,攻击方式 | 攻击类型，骰子及其最大与最小值，词条(函数)
    FP1 = [["生死界限",4,3,0],[[0,1,4,
                            ["if chanPow==max and chanPow >= 4:\n\tchanPow+=46\n\taddInfo='若骰子基础值不低于4点 且为最大值 则威力+45'"]]]]
    FP2 = [["血雾弥漫",5,4,0],[[0,20,39]]]
    FP3 = [["小金的五彩骨灰",114,4],[[1,999,999,
                            ["chanPow*=-0.1\naddInfo='这就是金智勋的实力!!! - 骰子威力乘-0.1'"]]]]

class func:

    def page_Reader(page, selector=None):
        atk_method = ("近战","远程","群体攻击-交锋","群体攻击-清算")
        quality = ("平装","精装","限定","艺术","E.G.O书页")
        PATH = page[0]

        print(f"{PATH[0]} | {PATH[1]}光芒消耗 | {quality[PATH[2]]}")
        return page[1]

    def dice_Roller (page, target=None ,effect=None):
        Type = ("斩击","突刺","打击","招架","闪避","斩击-反击","突刺-反击","打击-反击","招架-反击","闪避-反击")
        Romen_Num = ("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")
        
        rolls_Result = [] # 用于收集所有骰子结果
        rollInfoSet = [] # 用于收集所有骰子附加信息

        for rolls in range(0,page.__len__()):
            # 循环读取所有骰子
            PATH = page[rolls] # 路径指向： 书页(page)/骰子(rolls)
            try:
                atk_Type = Type[PATH[0]]
                basicPow = random.randint(PATH[1],PATH[2])
                chanPow = basicPow
                # 基础威力basicPow(摇到的数值) 与 变动威力ChangeablePow(受威力加减影响的威力)
                addInfoSet = [] # 附加信息在词条触发后添加
                for entry in range(0,PATH.__len__()-3):
                    # 循环读取所有词条
                    # ? 词条有执行顺序,鉴于图书馆乘算操作实在太少,这里忽略
                    vars = {'chanPow':chanPow, 'max':PATH[2], 'addInfo':''}
                    # vars用于给予exec函数已知信息并收集函数执行结果
                    try:
                        exec(PATH[entry+3][0], vars)
                        chanPow = vars["chanPow"]
                        # 威力增减赋值与原数值

                        if chanPow <= 1:
                            chanPow = 1
                        # 防止威力出现为0或负数的情况
                        if vars["addInfo"] != '':
                            addInfoSet.append(vars["addInfo"])
                    except:
                        raise RuntimeError (
                        f"读取词条时发生错误 | 第{rolls+1}个骰子的第{Romen_Num[entry]}个词条的函数无法读取")    
            except: 
                raise RuntimeError (
                f"读取骰子时发生错误 | 第{rolls+1}个骰子的基础信息无法读取")
        
            finalPow = int(chanPow)
            # 最终威力finalPow 不再改变的数值
            
            powChangeSet = [] # 记录威力变化而不改变威力数值类型
            if chanPow > basicPow:
                powChange = (str(basicPow)+"->"+"\033[31m"+str(chanPow)+"\033[0m")
                powChangeSet.append(powChange)
            if chanPow < basicPow:
                powChange = (str(basicPow)+"->"+"\033[33m"+str(chanPow)+"\033[0m")
                powChangeSet.append(powChange)
            # 演示威力增减过程
            
            infoSet = []
            if addInfoSet != []: # 可能会有没有词条执行的情况
                for Info in range(0,addInfoSet.__len__()):
                    show_Info = ("\n\t\t| "+Romen_Num[Info]+"."+addInfoSet[Info])
                    infoSet.append(show_Info)
            rollInfoSet.append(infoSet)   # 所有骰子的附加信息
            
            rolls_Result.append(finalPow)
            # 待骰子执行完成，将其结果添加至集合内，作为函数结果输出
            # | rolls_Result 是所有骰子最终威力的集合,元素为int格式
            # | powChangeSet 是所有骰子威力变化的集合,元素为str格式
            # | rollInfoSet  是所有骰子词条的提示信息,元素为str格式
        return (rolls_Result, powChangeSet, rollInfoSet)

def roll_Reader(roll_Result, powChangeSet, rollInfoSet):  
    for rolls in range (0,roll_Result.__len__()):
        finalInfo = ''
        for info in range (0,rollInfoSet[rolls].__len__()):
            finalInfo += str(rollInfoSet[rolls][info])
        if powChangeSet != []:
            print(f"\t* 第{rolls+1}个骰子最终威力 | {powChangeSet[rolls]} {finalInfo}")
        else:
            print(f"\t* 第{rolls+1}个骰子最终威力 | {roll_Result[rolls]} {finalInfo}")

LOR = func
P = Pages
PATH = LOR.dice_Roller(LOR.page_Reader(P.FP2))
roll_Reader(PATH[0],PATH[1],PATH[2])