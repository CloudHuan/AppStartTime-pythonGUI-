#!_*_coding=utf-8_*_

import wx,thread
from core import cCode

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title=u'启动时间测试 拜 cloudhuan',size=(600,200),pos=(500,200))
        self.SetMaxSize(wx.Size(600,500))
        mPanel = wx.Panel(parent=self)
        mSizer = wx.GridBagSizer(5,2)
        mSizer.AddGrowableCol(0,1)
        mSizer.AddGrowableCol(1,3)
        #
        t_pkg = wx.StaticText(parent=mPanel,label='包名/.类名:')
        self.e_pkg = wx.TextCtrl(parent=mPanel)
        mSizer.Add(t_pkg,pos=(0,0),flag=wx.ALIGN_CENTER)
        mSizer.Add(self.e_pkg,pos=(0,1),flag=wx.EXPAND)
        #
        t_num = wx.StaticText(parent=mPanel,label='次数:')
        self.e_num = wx.TextCtrl(parent=mPanel)        
        mSizer.Add(t_num,pos=(1,0),flag=wx.ALIGN_CENTER)
        mSizer.Add(self.e_num,pos=(1,1),flag=wx.EXPAND)             
        #
        btn = wx.Button(parent=mPanel,label=u'执行')
        mSizer.Add(btn,pos=(3,0),flag=wx.ALIGN_CENTER)
        self.c_box = wx.CheckBox(parent=mPanel,label=u'每次清除数据')
        mSizer.Add(self.c_box,pos=(3,1))
        #
        btn_check = wx.Button(parent=mPanel,label=u'当前activity')
        mSizer.Add(btn_check,pos=(4,0),flag=wx.ALIGN_CENTER)    
        self.t_show = wx.TextCtrl(parent=mPanel)
        mSizer.Add(self.t_show,pos=(4,1),flag=wx.EXPAND)
        
        #bindevent
        btn.Bind(event=wx.EVT_BUTTON,handler=self.execShell)
        btn_check.Bind(event=wx.EVT_BUTTON,handler=self.getActivity)
        
        #test
        self.e_pkg.SetValue(cCode.C_Tools().readConfig())
        
        mPanel.SetSizer(mSizer)
        mPanel.Fit()

    def execShell(self,event):
        pkgName = self.e_pkg.GetValue()
        num = self.e_num.GetValue()
        cCode.C_Tools().writeConfig(pkgName)
        flag = False
        if self.c_box.GetValue() == True:
            flag = True
        thread.start_new_thread(cCode.C_Tools().startTimeLoop,(pkgName,num,flag))

    def getActivity(self,event):
        self.t_show.SetValue(cCode.C_Tools().getCurrentActivity())

if __name__ == '__main__':
    app = wx.App()
    Frame().Show()
    app.MainLoop()
   