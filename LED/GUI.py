from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image,ImageDraw

import sys 
sys.path.append('c:/users/user/source/repos/resistor/PythonApplication2/')
sys.path.append('c:/users/user/source/repos/GUI/resistor 2/')
sys.path.append('c:/users/user/source/repos/GUI/resistor 3/')
sys.path.append('c:/users/user/source/repos/GUI/resistor 4/')
from resistor import  changeR0
from resistor_1 import  changeR1
from resistor_2 import  changeR2
from resistor_3 import  changeR3

import threading
import time
import RPi.GPIO as GPIO
## 600nm用GPIO6 31腳
## 750nm用GPIO13 33腳
## 900nm用GPIO19 35腳
## 白光用GPIO26 37腳

class GUI:
    ##產生左側按鈕
    def __init__(self,win):
        self.win = win
        self.chan1 = 0
        self.a = 0
        self.i0 = 0
        self.i1 = 0
        self.i2 = 0
        self.i3 = 0

    def set_win(self):
        win.title('my window')
        win.geometry('600x600')
    def setup(self): 
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(31,GPIO.OUT,initial=0) 
        GPIO.setup(33,GPIO.OUT,initial=0) 
        GPIO.setup(35,GPIO.OUT,initial=0)
        GPIO.setup(37,GPIO.OUT,initial=0)

    def show_bt(self):
        btn = Button(win,text = "600nm", command= self.bt_work_L0) 
        btn.place(relx=0.05, rely=0.3, relwidth=0.1, relheight=0.1)
        btn1 = Button(win,text = "750nm", command= self.bt_work_L1)
        btn1.place(relx=0.25, rely=0.2, relwidth=0.1, relheight=0.1)
        btn2 = Button(win,text = "900nm", command= self.bt_work_L2)
        btn2.place(relx=0.25, rely=0.3, relwidth=0.1, relheight=0.1)
        btn3 = Button(win,text = "白光", command= self.bt_work_L3)
        btn3.place(relx=0.05, rely=0.2, relwidth=0.1, relheight=0.1)
        btn4 = Button(win, text ='-', command= self.minus)
        btn4.place(relx=0.55, rely=0.3, relheight=0.1,relwidth=0.1)
        btn5 = Button(win, text ='+', command= self.plus)
        btn5.place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.1)
        btn6 = Button(win, text ='off', command= self.bt_work_L4)
        btn6.place(relx=0.075, rely=0.4, relwidth=0.25, relheight=0.1)

    def show_lab_sca(self):
         ## 產生顯示數值的背景
        label_result = Label(win, textvariable = result ,bg='skyblue', font=('Arial', 20), width=30, height=2)
        label_result.place(relx=0.05 ,rely=0.05, relwidth=0.3, relheight=0.1)
        scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) 
        scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
        ## 產生顯示600nm的背景
        label_result_0 = Label(win, textvariable = result_0 ,bg='skyblue', font=('Arial', 20), width=30, height=2) 
        label_result_0.place(relx=0.05 ,rely=0.85, relwidth=0.15, relheight=0.1)
        ## 產生顯示750nm的背景
        label_result_1 = Label(win, textvariable = result_1 ,bg='skyblue', font=('Arial', 20), width=30, height=2) 
        label_result_1.place(relx=0.225 ,rely=0.85, relwidth=0.15, relheight=0.1)
        ## 產生顯示900nm的背景
        label_result_2 = Label(win, textvariable = result_2 ,bg='skyblue', font=('Arial', 20), width=30, height=2) 
        label_result_2.place(relx=0.4 ,rely=0.85, relwidth=0.15, relheight=0.1)
        ## 產生顯示白光的背景
        label_result_3 = Label(win, textvariable = result_2 ,bg='skyblue', font=('Arial', 20), width=30, height=2) 
        label_result_3.place(relx=0.575 ,rely=0.85, relwidth=0.15, relheight=0.1)

    def bt_work_L0(self): ##600nm工作
        if(self.i0 == 0):
            GPIO.output(31,GPIO.HIGH)
            scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) 
            scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
            self.a = scale_result.get()
            result_0.set(self.a)
            resistor0.conduct(self.a)
            lab_result_0 = Label(win, textvariable = result_0 ,bg='skyblue', font=('Arial', 20), width=30, height=2) ## 產生顯示數值的背景
            lab_result_0.place(relx=0.05 ,rely=0.85, relwidth=0.15, relheight=0.1)
            print(self.a)
            self.i0 = 1

        if(self.i0 == 1):
            GPIO.output(31,GPIO.LOW)
            self.i0 = 0

    def bt_work_L1(self): ##750nm工作
        if(self.i1 == 0):
            GPIO.output(33,GPIO.HIGH)
            scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) 
            scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
            self.a = scale_result.get()
            result_1.set(self.a)
            resistor1.conduct(self.a)
            lab_result_1 = Label(win, textvariable = result_1 ,bg='skyblue', font=('Arial', 20), width=30, height=2) ## 產生顯示數值的背景
            lab_result_1.place(relx=0.225 ,rely=0.85, relwidth=0.15, relheight=0.1)
            print(self.a)
            self.i1 =1

        if(self.i1 == 1):
            GPIO.output(33,GPIO.LOW)
            self.i1 =0
        
    def bt_work_L2(self): ##900nm工作
        if(self.i2 == 0):
            GPIO.output(35,GPIO.HIGH)
            scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) 
            scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
            self.a = scale_result.get()
            result_2.set(self.a)
            resistor2.conduct(self.a)
            lab_result_2 = Label(win, textvariable = result_2 ,bg='skyblue', font=('Arial', 20), width=30, height=2) ## 產生顯示數值的背景
            lab_result_2.place(relx=0.4 ,rely=0.85, relwidth=0.15, relheight=0.1)
            print(self.a)
            self.i2 =1

        if(self.i2 == 1):
            GPIO.output(35,GPIO.LOW)
            self.i2 =0

    def bt_work_L3(self): ##白光nm工作
        if(self.i1 == 0):
            GPIO.output(37,GPIO.HIGH)
            scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) 
            scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
            self.a = scale_result.get()
            result_3.set(self.a)
            resistor3.conduct(self.a)
            lab_result_3 = Label(win, textvariable = result_3 ,bg='skyblue', font=('Arial', 20), width=30, height=2) ## 產生顯示數值的背景
            lab_result_3.place(relx=0.575 ,rely=0.85, relwidth=0.15, relheight=0.1)
            print(self.a)
            self.i3 =1

        if(self.i3 == 1):
            GPIO.output(37,GPIO.LOW)
            self.i3 =0

    def bt_work_L4(self): ##無輸出
        GPIO.output(31,GPIO.LOW)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)
        result_0.set(0)
        result_1.set(0)
        result_2.set(0)
        result_3.set(0)
        result.set(0)
        label_result = Label(win, textvariable = result ,bg='skyblue', font=('Arial', 20), width=30, height=2)
        label_result.place(relx=0.05 ,rely=0.05, relwidth=0.3, relheight=0.1)
        label_result_0 = Label(win, textvariable = result_0 ,bg='skyblue', font=('Arial', 20), width=30, height=2) 
        label_result_0.place(relx=0.575 ,rely=0.85, relwidth=0.15, relheight=0.1)
        label_result_1 = Label(win, textvariable = result_1 ,bg='skyblue', font=('Arial', 20), width=30, height=2) 
        label_result_1.place(relx=0.575 ,rely=0.85, relwidth=0.15, relheight=0.1)
        label_result_2 = Label(win, textvariable = result_2 ,bg='skyblue', font=('Arial', 20), width=30, height=2) 
        label_result_2.place(relx=0.575 ,rely=0.85, relwidth=0.15, relheight=0.1)
        label_result_3 = Label(win, textvariable = result_3 ,bg='skyblue', font=('Arial', 20), width=30, height=2) 
        label_result_3.place(relx=0.575 ,rely=0.85, relwidth=0.15, relheight=0.1)

    ## 定義+按鈕作用
    def plus(self):
        scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) 
        scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
        self.a = scale_result.get() #吃上個滑條狀態的值
        self.a += 1 
        if(self.a > 100):
            self.a = 100
        scale_result.set(self.a)
        label_result = Label(win, textvariable = result ,bg='skyblue', font=('Arial', 20), width=30, height=2) ## 產生顯示數值的背景
        label_result.place(relx=0.05 ,rely=0.05, relwidth=0.3, relheight=0.1)
        scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,)
        scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
        #a = result.get()
        #resistor.conduct(a)
        #print(resistor.k1)

    ## 定義-按鈕作用
    def minus(self):
        scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) ##顯示滑條的狀態
        scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
        self.a = scale_result.get() #吃上個滑條狀態的值
        self.a -= 1
        if(self.a < 0):
            self.a = 0
        scale_result.set(self.a)
        label_result = Label(win, textvariable = result ,bg='skyblue', font=('Arial', 20), width=30, height=2) ## 產生顯示數值的背景
        label_result.place(relx=0.05 ,rely=0.05, relwidth=0.3, relheight=0.1)
        scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,)
        scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
       #print(resistor.k1)

    ## 定義暗燈泡按鈕動作
    def set1(self):
        self.a=100
        result.set(self.a)
        label_result = Label(win, textvariable = result ,bg='skyblue', font=('Arial', 20), width=30, height=2) ## 產生顯示數值的背景
        label_result.place(relx=0.05 ,rely=0.05, relwidth=0.3, relheight=0.1)
        scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) ##產生滑條
        scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)  
        
    ## 定義亮燈泡按鈕動作
    def set2(self):
        self.a=0
        result.set(self.a)
        label_result = Label(win, textvariable = result ,bg='skyblue', font=('Arial', 20), width=30, height=2) ## 產生顯示數值的背景
        label_result.place(relx=0.05 ,rely=0.05, relwidth=0.3, relheight=0.1)
        scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) ##產生滑條
        scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)

    '''def changeR_run(self):
        while 1:
        #def chan():
            #scale_result = Scale(win,orient=HORIZONTAL,variable = result ,length=300,width=20,sliderlength=10,from_=0,to=100,tickinterval=10,) ##產生滑條
            #scale_result.place(relx=0.45, rely=0.05, relwidth=0.5, relheight=0.1)
             self.a=result.get()
             resistor.conduct(self.a)
            
            #print(result.get())
        #chan() 
        '''
        

if __name__=='__main__':
    resistor0 = changeR0()
    resistor1 = changeR1()
    resistor2 = changeR2()
    resistor3 = changeR3()
    win = tk.Tk()
    win.resizable()
    test123 = GUI(win)
    result =IntVar()
    result_0 =IntVar()
    result_1 =IntVar()
    result_2 =IntVar()
    result_3 =IntVar()

    img = Image.open("C:/Users/USER/Downloads/1.jpg")        ##把圖片引進
    img = img.resize((90,90))                             ##設定圖片大小
    img = ImageTk.PhotoImage(img)  
    img1 = Image.open("C:/Users/USER/Downloads/5.jpg")          
    img1 = img1.resize((90,90))
    img1 = ImageTk.PhotoImage(img1)
   
    label1=tk.Button(win,image=img, command= test123.set1)              #＃把圖片設成按鈕
    label1.place(relx=0.7 ,rely=0.15, relwidth=0.3, relheight=0.15) 
    label2=tk.Button(win,image=img1, command= test123.set2)              
    label2.place(relx=0.4 ,rely=0.15, relwidth=0.3, relheight=0.15) 

    test123.set_win()
    test123.setup()
    test123.show_lab_sca()
    test123.show_bt()
    resistor0.setup()
    resistor0.ud_zero()
    resistor1.setup()
    resistor1.ud_zero()
    resistor2.setup()
    resistor2.ud_zero()
    resistor3.setup()
    resistor3.ud_zero()

    ## threading.Thread(target = test123.changeR_run , daemon = True, args = ()).start()
    win.mainloop()