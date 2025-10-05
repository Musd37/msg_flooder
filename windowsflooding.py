import win32api
import win32con
import win32gui
import threading as th
from time import sleep
from random import randint
from pyautogui import size

class windowsflooding(object):

    def __init__(self,title,text,num,mode,life):
        self.title = title
        self.text = text
        self.num = num
        self.life = life
        self.mode = mode

        self.width = 160
        self.height = 190

    def setpos(self,x,y):
        self.x = x
        self.y = y

    def setstep(self,sx,sy):
        self.sx = sx
        self.sy = sy

    def create_windows(self,c):
        win32gui.MessageBox(None,self.text,self.title+str(c),win32con.MB_ICONINFORMATION)

    def move_windows(self,rx,ry,c):
        hwnd = win32gui.FindWindow(None,self.title+str(c))
        win32gui.SetWindowPos(hwnd,win32con.HWND_TOP,rx,ry,self.width,self.height,win32con.SWP_SHOWWINDOW)

    def string_reset(self,num,x,y,sx,sy):
        for i in range(self.num):
            th.Thread(target=self.create_windows,args=[i,]).start()
            sleep(0.02)
            th.Thread(target=self.move_windows,args=[self.x+self.sx*i,self.y+self.sy*i,i]).start()
            if self.life != 0:
                th.Thread(target=self.destory_windows,args=[i,]).start()

    def random_reset(self,num):
        for i in range(self.num):
            th.Thread(target=self.create_windows,args=[i,]).start()
            sleep(0.02)
            th.Thread(target=self.move_windows,args=[randint(0,size()[0]),randint(0,size()[1]),i]).start()
            if self.life != 0:
                th.Thread(target=self.destory_windows,args=[i,]).start()

    def destory_windows(self,c):
        sleep(self.life)
        hwnd = win32gui.FindWindow(None,self.title+str(c))
        win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)

    def __call__(self):
        if self.mode == 'r':
            self.random_reset(self.num)
        elif self.mode == 's':
            self.string_reset(self.num,self.x,self.y,self.sx,self.sy)

'''
w = windowsflooding('Warning','System Error!',20,'r')
w()
w2 = windowsflooding("Error","System Crash!",20,'s')
w2.setpos(0,0)
w2.setstep(15,15)
w2()
w3 = windowsflooding("E","System",20,'s')
w3.setpos(1900,0)
w3.setstep(-15,0)
w3()
'''