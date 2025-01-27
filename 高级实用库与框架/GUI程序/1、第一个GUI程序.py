import wx
#创建一个应用程序对象
app = wx.App()
#创建一个窗口对象
frame = wx.Frame(None, title='第一个GUI程序!',size=(400,300),pos=(650,350))
#显示窗口
frame.Show()
#进入主事件循环
app.MainLoop()