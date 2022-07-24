import wx

class BlueFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,id,'Blue', size=(300,200))

        #Panel for frame
        self.panel = wx.Panel(self)
        self.SetBackgroundColour(wx.BLUE)

app=wx.App()
frame=BlueFrame(parent=None,id=-1)
frame.Show()
app.MainLoop()