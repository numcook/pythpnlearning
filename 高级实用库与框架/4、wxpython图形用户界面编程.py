#pip install wxpython安装

#图形用户界面编程 简称GUI

#wxpython主要提供如下GUI内容
#1、窗口
#2、控件
#3、事件处理
#4、布局管理

#编写GUI程序的主要过程就是创建窗口和添加控件过程

#1）窗口
#窗口类主要有wx.Frame和wx.Dialog两种
#wx.Frame：普通窗口
#wx.Dialog：对话框窗口

#构建一个最简单的WXpython程序至少需要一个wx.App对象和一个wx.Frame对象

#界面构造层次：层级结构 如下
#          frame
#菜单栏                panel
#             statictext   其他控件


#2）事件处理