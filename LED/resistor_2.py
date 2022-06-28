import time
import RPi.GPIO as GPIO

INC = 8
UD = 10
CS = 12

'''
|========|=======|======|================================|
|   CS   |  INC  |  UD  |             MODE               |
|========|=======|======|================================|
|  L     |  down |  H   | Wiper up                       |
|--------|-------|------|--------------------------------|
|  L     |  down |  L   | Wiper down                     |
|--------|-------|------|--------------------------------|
|  up    |  H    |  X   | Store wiper position           |
|--------|-------|------|--------------------------------|
|  H     |  X    |  X   | Standby current                |
|--------|-------|------|--------------------------------|
|  up    |  L    |  X   | No store, return to standby    |
|--------|-------|------|--------------------------------|
|  down  |  L    |  H   | Wiper up ( not recommended )   |
|--------|-------|------|--------------------------------|
|  down  |  L    |  L   | Wiper down ( not recommended ) |
|--------|-------|------|--------------------------------|
'''
class changeR2:
    def __init__(self,k1 = 0):
        self.ud_present = 0
        self.k1 = k1
        self.num_of_scale_past = 1
    def setup(self): # 類似於 Arduino 的 setup func.
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(INC,GPIO.OUT,initial=0) # 設定 INC 為輸出 pin，初始值設定為 LOW
        GPIO.setup(UD,GPIO.OUT,initial=0) # 設定 UD 為輸出 pin，初始值設定為 LOW
        GPIO.setup(CS,GPIO.OUT,initial=0) # 設定 CS 為輸出 pin，初始值設定為 LOW
    def cleanup(self): # 把所有 pin 腳回歸原始狀態
        GPIO.cleanup()
    def inc(self,iter): # 定義 INC 的負緣觸發方法，重複觸發 iter 次，並且最後停留在 HIGH 電位
        for _ in range(iter):
            GPIO.output(INC,1)
            time.sleep(0.001)
            GPIO.output(INC,0)
            time.sleep(0.001)
        GPIO.output(INC,1)

        '''
        a wave in one iter:
        |============|- - - - - - |- - - - - 3.3 V
        |            |            |
        |            |            |
        |            |            |
        |- - - - - - |============|- - - - - 0 V

        |----1 ms----|----1 ms----|
        '''
    def ud(self,number): # 根據輸入內容改變電阻大小，num 的輸入範圍是 0 到 99，電阻值約為 (1.17K * num) ohm
        GPIO.output(CS,0) # 首先拉低 CS 電位
        if(number<=0): # 輸入小於 0 時，輸入為 0
            number=0
        if(number>99): # 輸入大於 99 時，輸入為 99
            number=99
        diff=number-self.ud_present # 計算目前輸入與上次輸入的差植
        if(diff>0):
            GPIO.output(UD,1) # 如果目前輸入大於上次輸入，則拉高 ud 電位
        else:
            GPIO.output(UD,0) # 如果目前輸入小於上次輸入，則拉低 ud 電位
        if(diff!=0): # 如果目前輸入不等於上次輸入，則改變電阻值
            self.inc(abs(diff))
        GPIO.output(CS,1) # 拉高 CS 電位，產生 CS 的正緣觸發，儲存以穩定輸出電阻值
        self.ud_present=number # 紀錄當前輸入，提供下次使用 ( *重點觀念: static var. in func. )

    def ud_zero(self): # 電阻值歸 0 ( 初始化晶片電路 )
        GPIO.output(CS,0)
        GPIO.output(UD,0)
        self.inc(100)
        GPIO.output(CS,1)
    def conduct(self,num_of_scale):
        try:
            if(num_of_scale != self.num_of_scale_past):
                self.ud(num_of_scale)
              # print(self.num_of_scale_past)
              # print(num_of_scale)
                self.num_of_scale_past = num_of_scale
              # print("done")
        except:
            self.cleanup()

if __name__=='__main__':
    act=changeR(0)
    act.setup()
    act.ud_zero()
    try:
        while 1:
            number = int(input("please input a number:"))
            act.ud(number)
            print("done")
    except:
        act.cleanup()
        print("goodbye")
