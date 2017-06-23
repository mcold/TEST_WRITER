# coding:utf-8

import wx



class BaseList(wx.ListCtrl):
    def __init__(self, parent):
        super(BaseList, self).__init__(parent, style=wx.LC_REPORT, pos=(5, 200), size = (400, 400))

        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnRClick)
        self.Bind(wx.EVT_MENU, self.OnMenu, id=wx.ID_COPY)
        self.Bind(wx.EVT_MENU, self.OnMenu, id=wx.ID_SELECTALL)

    def OnRClick(self, event):
        menu = wx.Menu()
        menu.Append(wx.ID_COPY)
        menu.Append(wx.ID_SELECTALL)
        self.PopupMenu(menu)
        menu.Destroy()

    def OnMenu(self, event):
        if event.Id == wx.ID_COPY:
            self.Copy()
        elif event.Id == wx.ID_SELECTALL:
            self.SelectAll()
        else:
            event.Skip()

    def Copy(self):
        """Copy selected data to clipboard"""
        text = self.GetSelectedText()
        data_o = wx.TextDataObject()
        data_o.SetText(text)
        if wx.TheClipboard.IsOpened() or wx.TheClipboard.Open():
            wx.TheClipboard.SetData(data_o)
            wx.TheClipboard.Flush()
            wx.TheClipboard.Close()

    def GetSelectedText(self):
        items = list()
        nColumns = self.ColumnCount
        for item in range(self.ItemCount):
            if self.IsSelected(item):
                items.append(self.GetRowText(item))
        text = "\n".join(items)
        return text

    def GetRowText(self, idx):
        txt = list()
        for col in range(self.ColumnCount):
            txt.append(self.GetItemText(idx, col))
        return "\t".join(txt)

    def SelectAll(self):
        """Select all items"""
        for item in range(self.ItemCount):
            self.Select(item, 1)



class PersonnelList(BaseList):
    def __init__(self, parent):
        super(PersonnelList, self).__init__(parent)

        # Add column headers
        self.InsertColumn(0, "ID")
        self.InsertColumn(1, "Name")
        self.InsertColumn(2, "Email")
        self.InsertColumn(3, "Phone#")

    def AddEmployee(self, id, name, email, phone):
        item = self.Append((id, name, email, phone))


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        # StaticBox(parent, id=ID_ANY, label=EmptyString, pos=DefaultPosition, size=DefaultSize, style=0, name=StaticBoxNameStr)
        # self.sb = wx.StaticBox(self, -1, 'Example', (5, 30), size=(100, 50))

        # TreeCtrl(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=TR_DEFAULT_STYLE, validator=DefaultValidator, name=TreeCtrlNameStr)
        self.trl = wx.TreeCtrl(self, 1, pos=(5, 5), size = (400, 150), name='treeCtrl_ObjectsBrowser', style=wx.TR_HAS_BUTTONS)

        # ListCtrl(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=LC_ICON, validator=DefaultValidator, name=ListCtrlNameStr)
        #self.lst = wx.ListCtrl(self, 2, pos=(5, 30), size = (100, 100))

        self._list = PersonnelList(self)
        # self._list2 = PersonnelList(self)
        # add some data
        self._list.AddEmployee("123", "Frank", "f@email.com", "555-1234")
        self._list.AddEmployee("124", "Jane", "j@email.com", "555-1434")
        self._list.AddEmployee("125", "Thor", "t@email.com", "555-1274")

    def AddEmployee(self, id, name, email, phone):
        item = self.lst.Append((id, name, email, phone))

        #self.Bind(wx.EVT_PAINT, self.OnPaint)
        # StaticBox(parent, id=ID_ANY, label=EmptyString, pos=DefaultPosition, size=DefaultSize, style=0, name=StaticBoxNameStr)
        #self.staticBox_Editor = wx.StaticBox(id=wx.ID_FRAME1STATICBOX_PROPRTIES,label='Properties', name='staticBox_Proprties', parent=self)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawLine(50, 10, 80, 10)
        dc.DrawLine(50, 140, 80, 140)
        dc.DrawLine(50, 300, 80, 300)

class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Window",size=(420,480))
        panel = MainPanel(self)
        self.CenterOnParent()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
