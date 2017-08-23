import wx
import sys
import os
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from shutil import copy2
import sqlite3 as lite
import datetime as dt

print('Starting...')
usrnm = input("Please enter name of user: ")
remhis = 'C:/Users/' + usrnm + '/Desktop/chrome/History'
remcook = 'C:/Users/' + usrnm + '/Desktop/chrome/Cookies'
remweb = 'C:/Users/' + usrnm + '/Desktop/chrome/Web Data'
# removes any existing files in the controlled location
print('Copying Google Chrome...')
try:
    os.remove(remhis)
except OSError:
    pass
try:
    os.remove(remcook)
except OSError:
    pass
try:
    os.remove(remweb)
except OSError:
    pass

# copies the files from storage to controlled location
# look up command line windows folder environment variables

hispath = 'C:/Users/' + usrnm + '/AppData/Local/Google/Chrome/User Data/Default/History'
cookpath = 'C:/Users/' + usrnm + '/AppData/Local/Google/Chrome/User Data/Default/Cookies'
webpath = 'C:/Users/' + usrnm + '/AppData/Local/Google/Chrome/User Data/Default/Web Data'
copypath = 'C:/Users/' + usrnm + '/Desktop/chrome'

copy2(hispath, copypath)
copy2(cookpath, copypath)
copy2(webpath, copypath)
print('Done')
# reads the files and extracts important tables then prints out

# making the lists
urlscols = []
urlsrows = []
downloadscols = []
downloadsrows = []
searchtermscols = []
searchtermsrows = []
cookiescols = []
cookiesrows = []
webdatacols = []
webdatarows = []
loginscols = []
loginsrows = []
keywordscols = []
keywordsrows = []

print('Extracting and Analysing...')
# extracting the data from the chosen sql tables by connecting to them and setting
# the cursor to read the information
hisconpath = 'C:/Users/' + usrnm + '/Desktop/chrome/History'
conn = lite.connect(hisconpath)
cur = conn.cursor()


def get_posts():
    cur.execute("SELECT * FROM urls")
    data = cur.fetchall()
    coldata = cur.description
    for col in coldata:
        urlscols.append(col[0])
    for row in data:
        urlsrows.append(row)


get_posts()


def get_posts():
    cur.execute("SELECT * FROM downloads")
    data = cur.fetchall()
    coldata = cur.description
    for col in coldata:
        downloadscols.append(col[0])
    for row in data:
        downloadsrows.append(row)

get_posts()


def get_posts():
    cur.execute("SELECT * FROM keyword_search_terms")
    data = cur.fetchall()
    coldata = cur.description
    for col in coldata:
        searchtermscols.append(col[0])
    for row in data:
        searchtermsrows.append(row)

get_posts()
cookconpath = 'C:/Users/' + usrnm + '/Desktop/chrome/Cookies'
connc = lite.connect(cookconpath)
curc = connc.cursor()


def get_posts():
    curc.execute("SELECT * FROM cookies")
    data = curc.fetchall()
    coldata = curc.description
    for col in coldata:
        cookiescols.append(col[0])
    for row in data:
        cookiesrows.append(row)

get_posts()
webconpath = 'C:/Users/' + usrnm + '/Desktop/chrome/Web Data'
connwd = lite.connect(webconpath)
curw = connwd.cursor()


def get_posts():
    curw.execute("SELECT * FROM autofill")
    data = curw.fetchall()
    coldata = curw.description
    for col in coldata:
        webdatacols.append(col[0])
    for row in data:
        webdatarows.append(row)

get_posts()


def get_posts():
    curw.execute("SELECT * FROM ie7_logins")
    data = curw.fetchall()
    coldata = curw.description
    for col in coldata:
        loginscols.append(col[0])
    for row in data:
        loginsrows.append(row)

get_posts()


def get_posts():
    curw.execute("SELECT * FROM keywords")
    data = curw.fetchall()
    coldata = curw.description

    for col in coldata:
        keywordscols.append(col[0])

    for row in data:
        keywordsrows.append(row)

get_posts()
print('Done')
print('Building Pages...')


class AutoWidthListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT, size=wx.Size(850, 750))
        ListCtrlAutoWidthMixin.__init__(self)
# this declares the size of the table inside of the page

# the following classes are all the pages in the notebook that will be called upon


class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, -1)

        self.list = AutoWidthListCtrl(self)
        self.list.InsertColumn(0, 'ID', width=50)
        self.list.InsertColumn(1, 'URL', width=300)
        self.list.InsertColumn(2, 'Title', width=200)
        self.list.InsertColumn(3, 'Visit Count', width=50)
        self.list.InsertColumn(4, 'Last Visited', width=120)
        self.list.InsertColumn(5, 'Hidden', width=50)

        def get_posts():
            cur.execute("SELECT * FROM urls")
            data = cur.fetchall()
            for row in data:
                number = dt.datetime(1601, 1, 1) + dt.timedelta(microseconds=int(row[5]))
                index = self.list.InsertItem(sys.maxunicode, row[0])
                self.list.SetItem(index, 0, str(row[0]))
                self.list.SetItem(index, 1, str(row[1]))
                self.list.SetItem(index, 2, str(row[2]))
                self.list.SetItem(index, 3, str(row[3]))
                self.list.SetItem(index, 4, str(number))
                self.list.SetItem(index, 5, str(row[6]))

        get_posts()

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)


class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, -1)

        self.list = AutoWidthListCtrl(self)
        self.list.InsertColumn(0, 'ID', width=25)
        self.list.InsertColumn(1, 'GUID', width=250)
        self.list.InsertColumn(2, 'Current Path', width=375)
        self.list.InsertColumn(3, 'Target Path', width=375)
        self.list.InsertColumn(4, 'Start Time', width=120)
        self.list.InsertColumn(5, 'Received Bytes', width=75)
        self.list.InsertColumn(6, 'Total Bytes', width=75)
        self.list.InsertColumn(7, 'Interrupt Reason', width=75)
        self.list.InsertColumn(8, 'End Time', width=120)
        self.list.InsertColumn(9, 'Opened', width=50)
        self.list.InsertColumn(10, 'Referrer', width=300)
        self.list.InsertColumn(11, 'Site URL', width=300)
        self.list.InsertColumn(12, 'Tab URL', width=300)
        self.list.InsertColumn(13, 'Tab Referrer URL', width=300)
        self.list.InsertColumn(14, 'Etag', width=100)
        self.list.InsertColumn(15, 'Last Modified', width=200)
        self.list.InsertColumn(16, 'Mime Type', width=150)
        self.list.InsertColumn(17, 'Original Mime Type', width=150)

        def get_posts():
            cur.execute("SELECT * FROM downloads")
            data = cur.fetchall()
            for row in data:
                number1 = dt.datetime(1601, 1, 1) + dt.timedelta(microseconds=int(row[4]))
                number2 = dt.datetime(1601, 1, 1) + dt.timedelta(microseconds=int(row[11]))
                index = self.list.InsertItem(sys.maxunicode, row[0])
                self.list.SetItem(index, 0, str(row[0]))
                self.list.SetItem(index, 1, str(row[1]))
                self.list.SetItem(index, 2, str(row[2]))
                self.list.SetItem(index, 3, str(row[3]))
                self.list.SetItem(index, 4, str(number1))
                self.list.SetItem(index, 5, str(row[5]))
                self.list.SetItem(index, 6, str(row[6]))
                self.list.SetItem(index, 7, str(row[9]))
                self.list.SetItem(index, 8, str(number2))
                self.list.SetItem(index, 9, str(row[12]))
                self.list.SetItem(index, 10, str(row[13]))
                self.list.SetItem(index, 11, str(row[14]))
                self.list.SetItem(index, 12, str(row[15]))
                self.list.SetItem(index, 13, str(row[16]))
                self.list.SetItem(index, 14, str(row[20]))
                self.list.SetItem(index, 15, str(row[21]))
                self.list.SetItem(index, 16, str(row[22]))
                self.list.SetItem(index, 17, str(row[23]))

        get_posts()

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)


class PageThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, -1)

        self.list = AutoWidthListCtrl(self)
        self.list.InsertColumn(0, 'Keyword ID', width=75)
        self.list.InsertColumn(1, 'URL ID', width=50)
        self.list.InsertColumn(2, 'Lower Term', width=120)
        self.list.InsertColumn(3, 'Term', width=120)

        def get_posts():
            cur.execute("SELECT * FROM keyword_search_terms")
            data = cur.fetchall()
            for row in data:
                index = self.list.InsertItem(sys.maxunicode, row[0])
                self.list.SetItem(index, 0, str(row[0]))
                self.list.SetItem(index, 1, str(row[1]))
                self.list.SetItem(index, 2, str(row[2]))
                self.list.SetItem(index, 3, str(row[3]))

        get_posts()

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)


class PageFour(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, -1)

        self.list = AutoWidthListCtrl(self)
        self.list.InsertColumn(0, 'Creation UTC', width=120)
        self.list.InsertColumn(1, 'Host Key', width=120)
        self.list.InsertColumn(2, 'Name', width=200)
        self.list.InsertColumn(3, 'Path', width=120)
        self.list.InsertColumn(4, 'Expires UTC', width=120)
        self.list.InsertColumn(5, 'Secure', width=75)
        self.list.InsertColumn(6, 'HTTP Only', width=75)
        self.list.InsertColumn(7, 'Last Access UTC', width=120)
        self.list.InsertColumn(8, 'Has Expires', width=75)
        self.list.InsertColumn(9, 'Persistent', width=75)
        self.list.InsertColumn(10, 'Priority', width=75)
        self.list.InsertColumn(11, 'Encrypted Value', width=250)

        def get_posts():
            curc.execute("SELECT * FROM cookies")
            data = curc.fetchall()
            for row in data:
                number1 = dt.datetime(1601, 1, 1) + dt.timedelta(microseconds=int(row[0]))
                number2 = dt.datetime(1601, 1, 1) + dt.timedelta(microseconds=int(row[5]))
                number3 = dt.datetime(1601, 1, 1) + dt.timedelta(microseconds=int(row[8]))
                index = self.list.InsertItem(sys.maxunicode, row[0])
                self.list.SetItem(index, 0, str(number1))
                self.list.SetItem(index, 1, str(row[1]))
                self.list.SetItem(index, 2, str(row[2]))
                self.list.SetItem(index, 3, str(row[4]))
                self.list.SetItem(index, 4, str(number2))
                self.list.SetItem(index, 5, str(row[6]))
                self.list.SetItem(index, 6, str(row[7]))
                self.list.SetItem(index, 7, str(number3))
                self.list.SetItem(index, 8, str(row[9]))
                self.list.SetItem(index, 9, str(row[10]))
                self.list.SetItem(index, 10, str(row[11]))
                self.list.SetItem(index, 11, str(row[12]))

        get_posts()

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)


class PageFive(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, -1)

        self.list = AutoWidthListCtrl(self)
        self.list.InsertColumn(0, 'Type', width=50)
        self.list.InsertColumn(1, 'Value', width=200)
        self.list.InsertColumn(2, 'Value Lower', width=200)
        self.list.InsertColumn(3, 'Date First Used', width=120)
        self.list.InsertColumn(4, 'Date Last Used', width=120)
        self.list.InsertColumn(5, 'Counter', width=75)

        def get_posts():
            curw.execute("SELECT * FROM autofill")
            data = curw.fetchall()
            for row in data:
                index = self.list.InsertItem(sys.maxunicode, row[0])
                self.list.SetItem(index, 0, str(row[0]))
                self.list.SetItem(index, 1, str(row[1]))
                self.list.SetItem(index, 2, str(row[2]))
                self.list.SetItem(index, 3, dt.datetime.fromtimestamp(int(row[3])).strftime('%Y-%m-%d %H:%M:%S'))
                self.list.SetItem(index, 4, dt.datetime.fromtimestamp(int(row[4])).strftime('%Y-%m-%d %H:%M:%S'))
                self.list.SetItem(index, 5, str(row[5]))

        get_posts()

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)


class MainFrame(wx.Frame):
    def __init__(self):
        frame_style_no_resize = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION
        # this will stop the windows being resized
        wx.Frame.__init__(self, None, title="FIDE", size=(875, 735), style=frame_style_no_resize)
        # call the toolbar
        self.initui()

        # open the panel and build a notebook with 5 pages and call upon those classes to build
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        page1 = PageOne(nb)
        page2 = PageTwo(nb)
        page3 = PageThree(nb)
        page4 = PageFour(nb)
        page5 = PageFive(nb)

        nb.AddPage(page1, "URL's Visited")
        nb.AddPage(page2, "Downloads")
        nb.AddPage(page3, "Keywords Searched")
        nb.AddPage(page4, "Cookies")
        nb.AddPage(page5, "Autofill Data")

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)
        print('Done')
        print('FIDE Built in Background')

    # below is the toolbar that is called upon earlier
    def initui(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        ri = wx.MenuItem(filemenu, wx.ID_ANY, '&Reload\tCtrl+R')
        filemenu.Append(ri)
        self.Bind(wx.EVT_MENU, self.reload, ri)
        filemenu.AppendSeparator()
        qmi = wx.MenuItem(filemenu, wx.ID_EXIT, '&Quit\tCtrl+Q')
        filemenu.Append(qmi)
        self.Bind(wx.EVT_MENU, self.onquit, qmi)
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)
        # The options in the menu are tied to an event declared below and a keyboard shortcut assigned

    def onquit(self):
        print('Ending Program...')
        self.Close()

    def reload(self):
        print('Reloading...')
        python = sys.executable
        os.execl(python, python, * sys.argv)
        # This should be completely refreshing the whole code however all this does is quit

if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
    # This all calls upon the lasses and executes itself
