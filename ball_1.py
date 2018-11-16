# 人生写的第一个游戏， 弹球
import random  # 随机模块
import time    # 时间模块 控制刷新频率
from tkinter import * # 动画模块 * 一个或者任意字符 # 通配符
tk = Tk()
tk.title("人生写的第一个游戏， 弹球")
tk.resizable(0, 0)  # x ,y 允许调节的大小
tk.wm_attributes("-topmost", 1) #tk 窗口置顶
# 画布类 Canvas
canvas = Canvas(tk, width = 500, height = 400)
canvas.pack() # pack()函数将canvas 根据参数进行打包显示出来
tk.update() # 更新动画tk 并刷新

class Ball:
    def __init__(self, canvas, color): #初始化  self 局部
        self.canvas = canvas   # 保证小球与 画布在同一平面
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        # 创建一个左上角坐标为10,10 右下角坐标为25,25的球 存到 self.id =球
        self.canvas.move(self.id, 245, 100) # 一开始将球移动到 245,100坐标
        self.x = 3
        self.y = -3
        self.canvas_height = self.canvas.winfo_height() #获取画布的高度
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # x 在水平方向上每次位移的距离  y 垂直
        # x 为正值时  向右  y 为正值 向下
        a = self.canvas.coords( self.id )  #获取小球坐标
        # a = [x1, y1, x2, y2]  a[0] = x1 , a[1] = y1, a[2] = x2, a[3] = y3
        if a[1] <= 0:
            self.y = 5
        if a[3] >= self.canvas_height:
            self.y = -5
        if a[2] >= self.canvas_width:  # 碰到最右边
            self.x = -5
        if a[0] <= 0:
            self.x = 5


ball = Ball(canvas, "blue")

while 1: # True  不断执行循环体 
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)  # 刷新 每间隔0.01秒 
    
    

    
