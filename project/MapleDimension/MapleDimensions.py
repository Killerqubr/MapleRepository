import threading
import time      
import math
import wx
import re   # ! 弃用
import os

class MapleDimensions:

    def __init__(self, ImportData):
        
        # 导入所有存档数据
        self.GP = ImportData['GameProgress']
        self.Item = ImportData['Item'] 
        self.MD = ImportData['MD']           
        self.ID = ImportData['ID']
        self.TD = ImportData['TD']
        self.MD_Price = ImportData['MD_Price']
        self.ID_Price = ImportData['ID_Price']
        self.TD_Price = ImportData['TD_Price']

        self.Item_Name = ('枫叶','无限点数','永恒点数')

        self.CF = ImportData['CountFrequency']      # 计数频率
        self.UT = ImportData['UnitTime']            # 单位时间
        self.PC = ImportData['ProductionCapacity']  # 生产效率
        self.RR = ImportData['RefreshRate']         # 界面刷新
        

        self.MDBought = [0,0,0,0,0,0,0,0]
        self.unlock_Price = [0,0,0,0,0,0,1e54000,1e60000,             # 解锁ID需要的ML
                            0,0,0,0,1e6]                              # 解锁ED需要的TT


    # 物质更新获得的量： 计数频率 * 时间(1s) * 生产器数量(编号i+1) * 生产效率(0.1/s)
    def Update(self):
        
        # 枫叶维度 | 精确到一位
        for target in range(0,self.GP[0]):
            self.MD[target] += round(self.MD[target+1] * self.UT * self.CF * self.PC,1)

        # 无限维度
        for target in range(0,self.GP[1]):
            self.ID[target] += round(self.ID[target][target+1] * self.UT * self.CF * self.PC,1)
        
        # 时间维度
        for target in range(0,self.GP[2]):
            self.TD[target] += round(self.TD[target][target+1] * self.UT * self.CF * self.PC,1)

        # 资源数据更新
        self.Item[0] += round(self.MD[0] * self.UT * self.CF * self.PC,1)
        self.Item[1] += round(self.ID[0] * self.UT * self.CF * self.PC,1)
        self.Item[2] += round(self.TD[0] * self.UT * self.CF * self.PC,1)

    def Buy(self, target, id):

        if target == 0:
            Var = self.MD_Price
        elif target == 1:
            Var = self.ID_Price
        elif target == 2:
            Var = self.TD_Price

        # Value 为批量购买
        Value = math.floor(self.Item[target]/math.pow(10,Var[id]))
        print(Value)
        Remain = self.Item[target] - math.pow(10,Var[id-(8*target)]) * Value
            
        if Remain >= 0:
            if target == 0:           
                self.Item[target] -= math.pow(10,self.MD_Price[id]) * Value
                self.MD[id] += 1 * Value
                self.MDBought[id] += Value 
                if (self.MDBought[id] % 10 == 0) and (Value != 0):
                    self.MD_Price[id] *= math.pow(10,Anti.MDPMulitor[id]) 
            elif target == 1:
                self.Item[target] -= self.ID_Price[id] * 10
                self.ID[id] += 1 * 10
                self.ID_Price[id] *= Anti.IDPMulitor[id]
            elif target == 2:
                self.Item[target] -= self.TD_Price[id] * 10          
                self.TD[id] += 1 * 10        
                self.TD_Price[id] *= Anti.TDPMulitor[id]               
        else:
            if target == 0:
                print(f"{Sys.CRed}{self.Item_Name[0]}不足! | 价格: {self.MD_Price[id] * Value}{Sys.CRm}")

    def Run(self):
        while Sys.End != True:
            time.sleep(1/20)  # 始终以40CF/s的频率运行,CF只是更新item时的乘数(AD说明)
            self.Update()

    def PriceCheck(self,Value):
        if Value >= 10:
            Value = 10
        if Value >= 10 - self.MDBought[MapleFrame.id]:
            Value = 10 - self.MDBought[MapleFrame.id]
            print(self.MDBought)
    
    # ? 这里的所有操作都会影响 ShowThread 线程的运行！
    def Show(self):
        while Sys.End != True:
            time.sleep(self.RR)
            MsgML = "你拥有%s枫叶" % (math.floor(self.Item[0]))
            MsgIP = "你拥有%s无限点数" % (math.floor(self.Item[1]))
            MsgEP = "你拥有%s永恒点数" % (math.floor(self.Item[2]))
            
#            for item in range(0,f.Dat['GameProgress'][0]):
#                self.dMsg = (f"{self.md_name[item]} | You Have: {f.Dat['MD'][item]} | Cost: {self.MD_Price[item]}")
#                dMsgs.insert(item,self.dMsg)
            Value = int(math.floor(self.Item[0]/math.pow(10,self.MD_Price[0])))
            if Sys.End != True:
                if self.GP[0] != 0:
                    Frame.InfoML.SetLabel(MsgML)
                if self.GP[1] != 0:
                    Frame.InfoIP.SetLabel(MsgIP)
                if self.GP[2] != 0:
                    Frame.InfoEP.SetLabel(MsgEP)
                self.PriceCheck(Value)
                Frame.Button_MD1.SetLabel(f"你拥有{self.MD[0]}\n可以购买{Value}个,价格:{math.pow(10,self.MD_Price[0])}")
    
    # System 类用于存放有关程序的运行数据
    class System:
        def __init__(self):

            # ! 颜色数据 | 弃用
            self.CRm = '\033[0m'
            self.CRed = '\033[31m'
            self.CPur = '\033[35m'
            
            # 忙碌信息
            self.Msg_waiting_for_Update = '等待数据更新...' 

            # 终止所有进程的循环 | 需要 Frame.on_close传递参数
            self.End = False

        
    # AntiMatter 类仅用于存放有关Antimatter Dimension有关的数据
    class AntiMatter:
        
        def __init__(self):
            
            self.TD_Name = ('第一永恒维度','第二永恒维度','第三永恒维度','第四永恒维度',
                            '第五永恒维度','第六永恒维度','第七永恒维度','第八永恒维度')         
            self.ID_Name = ('第一无限维度','第二无限维度','第三无限维度','第四无限维度',
                            '第五无限维度','第六无限维度','第七无限维度','第八无限维度')
            self.MD_Name = ('第一枫叶维度','第二枫叶维度','第三枫叶维度','第四枫叶维度',
                            '第五枫叶维度','第六枫叶维度','第七枫叶维度','第八枫叶维度')  
            
            # * 所有的数据类型都是 a*10^b | 储存的数一般是 b

            # Basic Price 即维度基础价格,任意重置时恢复此价格
            self.AD_BPrice = (1,2,4,6,9,13,18,24)                 # 已确认
            self.ID_BPrice = (8,9,10,20,140,200,250,280)
            self.TD_BPrice = (1,5,2,3,2350,2650,3000,3350)        # 已确认 | 前两个数据储存的为 int 而非 b

            # Price Multiplication 即维度价格增速，购买资源后价格的乘数
            self.MDPMulitor = [3,4,5,6,8,10,12,15]               
            self.IDPMulitor = [1e2,1e6,1e8,1e10,1e15,1e20,1e25,1e30]
            self.TDPMulitor = [3,9,27,2e4,7e4,2e5,7e5]

# MapleFrame 类构建窗口框架
class MapleFrame(wx.Frame):
        
    def __init__(self, parent=None, size=(1236,753)):

        # 基本的 Frame 框架
        wx.Frame.__init__(self, parent, title='Maple Dimension', size=size)
        self.Center()
        self.SetWindowStyle(self.GetWindowStyle()
                            & ~wx.RESIZE_BORDER 
                            #& ~wx.MINIMIZE_BOX
                            #& ~wx.MAXIMIZE_BOX
                            & ~wx.STAY_ON_TOP)
        self.SetBackgroundColour(wx.Colour(17,16,20))
        
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # 创建 Panel 面板
        panel = wx.Panel(self)
        
        # 只读信息
        self.InfoML = wx.StaticText(panel, -1, label=Sys.Msg_waiting_for_Update, pos=[500,30])
        self.InfoIP = wx.StaticText(panel, -1, label=Sys.Msg_waiting_for_Update)
        self.InfoEP = wx.StaticText(panel, -1, label=Sys.Msg_waiting_for_Update)

        self.InfoML.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.InfoML.SetForegroundColour([200,200,200])
        
        self.Button_MD1 = wx.Button(panel, 0,'等待更新...', pos=[900,100], size=[200,100])
        self.Button_MD1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))

        # 绑定事件
        self.Button_MD1.Bind(wx.EVT_BUTTON,self.FrameEvent_MDBuy)
        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.Show()

    def on_close(self, event):
        EndConfirm = wx.MessageBox("关闭枫叶维度？",
                            "确认", wx.YES_NO | wx.ICON_ASTERISK)
        if EndConfirm == wx.YES:
            Sys.End = True
            print('[控制台] 等待线程结束...')
            Counter = 1
            ShowThreadDead = False
            UpgradeThreadDead = False
 #           timer = threading.Timer(3.0, self.Exit)  # 时间事件,五秒后触发
 #           timer.start()
            while True:
                if ShowThread.is_alive() == False and ShowThreadDead == False:
                    print(f'[控制台] 线程结束[{Counter}/2] ShowThread 结束')
                    ShowThreadDead = True
                    Counter += 1

                elif UpgradeThread.is_alive() == False and UpgradeThreadDead == False:
                    print(f'[控制台] 线程结束[{Counter}/2] UpgradeThread 结束')
                    UpgradeThreadDead = True
                    Counter += 1

                if Counter == 3:
                    print('[控制台] 程序终止')
                    self.Destroy()
                    break
                
    def Exit(self):
        self.Destroy()
        raise SystemExit()

    def FrameEvent_MDBuy(self, event):
        self.id = event.GetId()
        Maple.Buy(0,self.id)


ImportData = {
        'CountFrequency':1,
        'UnitTime':1,
        'ProductionCapacity':0.1,
        'RefreshRate':0.02,
        'Item':[10,0,0],             # 枫叶,无限点数,永恒点数
        'Maple-Upgrade':[],   
        'Infinity-Upgrade':[],
        'Eternity-Upgrade':[],
        'Time-Research':[''],        # 时间研究的导入为字符串形式,与AD相同
        'Maple-Autobuyer':[],        # 自动购买器通过集合长度判断67 是否解锁,数字代表状态或升级
        'Infinity-Autobuyer':[],
        'Eternity-Autobuyer':[],
        'MD':[0,0,0,0,0,0,0,0],      # 枫叶1~8维度
        'ID':[0,0,0,0,0,0,0,0],      # 无限1~8维度
        'TD':[0,0,0,0,0,0,0,0],      # 时间1~8维度
        'MD_Price':[1,2,4,6,9,13,18,24],
        'ID_Price':[4,6,8,10,140,200,250,280],
        'TD_Price':[1,5,2,3,2350,2650,3000,3350],
        'TTSelledCount':0,
        'GameProgress':[1,0,0]}      # 枫叶/无限/永恒

# 实例化 MapleDimensions, AntiMatter 与 System 类,导入所有数据
Maple = MapleDimensions(ImportData)
Anti = Maple.AntiMatter() 
Sys = Maple.System()

# 实例化 wx 类，wx.App 类必须先初始化
App = wx.App()     
Frame = MapleFrame()

# 启用 Thread 多线程
UpgradeThread = threading.Thread(target=Maple.Run)
UpgradeThread.start()
ShowThread = threading.Thread(target=Maple.Show)
ShowThread.start()

# wx 窗口进程
Frame.Show()
App.MainLoop()