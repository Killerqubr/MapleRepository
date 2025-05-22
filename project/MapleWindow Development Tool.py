
import wx

#---------------------------------------------------
# Name:        MapleWindow Development Tool
# Author:      Ropeway
# 
# Created:     1-Jun-2024
# Coryright:   
# Licence:     
# --------------------------------------------------

class MapleFrame(wx.Frame):

    # ID
    ID_HAIL = 0
    ID_LIGHT = 1

    # ERROR
    ERROR_MODULE = 0
    ERROR_USER_MEANT = 1

    # LUA
    LUA_MF_TITLE = ['Maple Windows Development Tool','枫窗开发工具']

    LUA_MENUBAR_FILE_OPEN = ['&Open\tCtrl+O','&打开\tCtrl+O']
    LUA_MENUBAR_FILE_QUIT = ['&Quit\tCtrl+Q','&退出\tCtrl+Q']
    LUA_MENUBAR_FILE = ['&File','&文件']

    LUA_MENUBAR_EXTENSION = ['&Extension','&扩展']

    LUA_MENUBAR_SETTING = ['&Setting','&设置']
    LUA_MENUBAR_SETTING_HELP = ['&Help\tCtrl+Shift+H','&帮助\tCtrl+Shift+H']
    LUA_MENUBAR_SETTING_ABOUT = ['&About','&关于']
    LUA_MENUBAR_SETTING_ABOUT_MSG = ['Virsion : dev\nAuthor : Ropeway','版本 : 开发\n作者 : Ropeway']
    LUA_MENUBAR_SETTING_ABOUT_MSGTITLE = ['About This Development Tool','关于此开发工具']

    LUA_EVT_ON_CLOSE = [['Quit Maple Window Development Tool?','Confirmation'],['退出枫窗开发工具？','确认']]
    

    def __init__(self, parent=None, size=(400,370), lua=0):

        self.MF_LANGUAGE = lua

        wx.Frame.__init__(self, parent, title=self.LUA_MF_TITLE[self.MF_LANGUAGE], size=size)
        self.Center()
        self.SetWindowStyle(self.GetWindowStyle() 
                            & ~wx.RESIZE_BORDER 
                            & ~wx.MINIMIZE_BOX
                            & ~wx.MAXIMIZE_BOX)
        
        # Packages
        self.MenuBar = wx.MenuBar()
        self.sb = self.CreateStatusBar()
        MaplePanel = wx.Panel()

        # Event
        MaplePanel.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        self.Bind(wx.EVT_CLOSE, self.On_Close)
        
        # Functions
        self.MapleMenuBar()
        
    def MapleMenuBar(self):

        fileMenu = wx.Menu()
        extensionsMenu = wx.Menu()
        settingMenu = wx.Menu()
    
        # * MenuBar / fileMenu
        # 'Open' Button
        MenuOpen = wx.MenuItem(fileMenu, wx.ID_OPEN, self.LUA_MENUBAR_FILE_OPEN[self.MF_LANGUAGE])
        fileMenu.Append(MenuOpen)

        fileMenu.AppendSeparator()

        # Quit Button
        quit = wx.MenuItem(fileMenu, wx.ID_EXIT, self.LUA_MENUBAR_FILE_QUIT[self.MF_LANGUAGE]) 
        fileMenu.Append(quit)

        # * MenuBar / extensionsMenu
        # 'Hail' Button
        HailButton = wx.MenuItem(extensionsMenu, MapleFrame.ID_HAIL, '&Hail')
        extensionsMenu.Append(HailButton)

        # 'Light' Button
        LightButton = wx.MenuItem(extensionsMenu, MapleFrame.ID_LIGHT, '&Light')
        extensionsMenu.Append(LightButton)

        # * MenuBar / settingMenu
        # 'Help' Button
        Help = wx.MenuItem(settingMenu, wx.ID_HELP, self.LUA_MENUBAR_SETTING_HELP[self.MF_LANGUAGE])
        settingMenu.Append(Help)

        settingMenu.AppendSeparator()

        # 'About' Button
        About = wx.MenuItem(settingMenu, wx.ID_ABOUT, self.LUA_MENUBAR_SETTING_ABOUT[self.MF_LANGUAGE])
        settingMenu.Append(About)

        # * MenuBar Set up
        self.MenuBar.Append(fileMenu, self.LUA_MENUBAR_FILE[self.MF_LANGUAGE])
        self.MenuBar.Append(extensionsMenu, self.LUA_MENUBAR_EXTENSION[self.MF_LANGUAGE])
        self.MenuBar.Append(settingMenu, self.LUA_MENUBAR_SETTING[self.MF_LANGUAGE])

        self.SetMenuBar(self.MenuBar)
        self.Bind(wx.EVT_MENU, self.Handler)

    def Handler(self, event):
        id = event.GetId() 
        if id == wx.ID_EXIT:
            self.OnWidgetEnter(event)
            self.On_Close(event)

        elif id == wx.ID_OPEN:
            self.On_Open()

        elif id == wx.ID_ABOUT:
            self.Msg_About()

        elif id == MapleFrame.ID_HAIL:
            self.Hail()

        elif id == MapleFrame.ID_LIGHT:
            self.Light()

        elif id == wx.ID_HELP:
            self.Help()

    # Funcs
    def OnWidgetEnter(self, e):
        name = e.GetEventObject().GetClassName()
        if name =='wxPanel':
            name = 'MapleFrame > Panel'
        self.sb.SetStatusText(f"{name}")

    def On_Open(self):
        self.Error_Occurred(MapleFrame.ERROR_MODULE,'(Method) MapleFrame.Open')

    def Msg_About(self):
        wx.MessageBox(
f'{self.LUA_MF_TITLE[self.MF_LANGUAGE]}\n{self.LUA_MENUBAR_SETTING_ABOUT_MSG[self.MF_LANGUAGE]}'

, f"{self.LUA_MENUBAR_SETTING_ABOUT_MSGTITLE[self.MF_LANGUAGE]}", wx.ICON_INFORMATION)
        
    def On_Close(self, e):
        dlg = wx.MessageBox(self.LUA_EVT_ON_CLOSE[self.MF_LANGUAGE][0],
                            self.LUA_EVT_ON_CLOSE[self.MF_LANGUAGE][1], wx.YES_NO | wx.ICON_ASTERISK)
        if dlg == wx.YES:
            self.Destroy()

    def Error_Occurred(self,Class,info=None):
        dig = wx.MessageBox(
f"Maple Frame Development Tool was stopped by\n{info}\nError Code: {Class}\nEnd This Program Immediatly?"
,"An Error Occurred"
,wx.YES_NO | wx.ICON_ERROR)
        
        if dig == wx.YES:
            self.Destroy()
            if Class == MapleFrame.ERROR_MODULE:
                raise AttributeError(
                    f' This Fuction/Class is unable to use:\033[31m {info} \033[0m')
            if Class == MapleFrame.ERROR_USER_MEANT:
                raise ConnectionRefusedError(
                    f'\033[31mYou Meant It.\033[0m')
        
    def Hail(self):
        HailFrame()

    def Light(self):
        self.Error_Occurred(MapleFrame.ERROR_MODULE,'(Class) MapleFrame.Light')

    def Help(self):
        dig = wx.MessageBox(
f'''{self.LUA_MF_TITLE[self.MF_LANGUAGE]}

ClASS : MapleFrame
ID : ID_HAIL | ID_LIGHT
ERR : ERROR_UNABLE_TO_USE
LUA : LUA_MF_TITLE | LUA_MENUBAR_FILE_OPEN | LUA_MENUBAR_FILE_QUIT | LUA_MENUBAR_FILE | LUA_MENUBAR_EXTENSION
        LUA_MENUBAR_SETTING | LUA_MENUBAR_SETTING_HELP | LUA_MENUBAR_SETTING_ABOUT | LUA_EVT_ON_CLOSE ''',
'Help',wx.ID_NETWORK)
        if dig == 4096:
            self.Error_Occurred(MapleFrame.ERROR_USER_MEANT,"(String) I Don't Think You Need More Help")

class HailFrame(MapleFrame):

    def __init__(self):
        pass

    def Singal(self):
        pass

    def Multi(self):
        pass

    def MPL(self):
        pass

if __name__ == '__main__':
    App = wx.App()
    Frame = MapleFrame(lua=1)
    Frame.Show()
    App.MainLoop()
