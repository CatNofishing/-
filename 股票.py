
import pyautogui
import time

from pyautogui import PAUSE
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

script = '''

currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置
print(currentMouseX, currentMouseY)

# 控制鼠标移动,duration为持续时间
for i in range(2):
  pyautogui.moveTo(100, 100, duration=0.25) # 移动到 (100,100)
  pyautogui.moveTo(200, 100, duration=0.25)
  pyautogui.moveTo(200, 200, duration=0.25)
  pyautogui.moveTo(100, 200, duration=0.25)

for i in range(2):
  pyautogui.moveRel(50, 0, duration=0.25) # 从当前位置右移100像素
  pyautogui.moveRel(0, 50, duration=0.25) # 向下
  pyautogui.moveRel(-50, 0, duration=0.25) # 向左
  pyautogui.moveRel(0, -50, duration=0.25) # 向上

# 按住鼠标左键，把鼠标拖拽到(100, 200)位置
pyautogui.dragTo(100, 200, button='left')
# 按住鼠标左键，用2秒钟把鼠标拖拽到(300, 400)位置
pyautogui.dragTo(300, 400, 2, button='left')
# 按住鼠标左键，用0.2秒钟把鼠标向上拖拽
pyautogui.dragRel(0, -60, duration=0.2)

# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# 其中，button属性可以设置成left，middle和right。
pyautogui.click(10, 20, 2, 0.25, button='left')
pyautogui.click(x=100, y=200, duration=2) # 先移动到(100, 200)再单击
pyautogui.click() # 鼠标当前位置点击一下
pyautogui.doubleClick() # 鼠标当前位置左击两下
pyautogui.doubleClick(x=100, y=150, button="left") # 鼠标在（100，150）位置左击两下
pyautogui.tripleClick() # 鼠标当前位置左击三下

pyautogui.mouseDown() # 鼠标左键按下再松开
pyautogui.mouseUp()
pyautogui.mouseDown(button='right') # 按下鼠标右键
pyautogui.mouseUp(button='right', x=100, y=200) # 移动到(100, 200)位置，然后松开鼠标右键

# scroll函数控制鼠标滚轮的滚动，amount_to_scroll参数表示滚动的格数。正数则页面向上滚动，负数则向下滚动
# pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
pyautogui.scroll(5, 20, 2)
pyautogui.scroll(10) # 向上滚动10格
pyautogui.scroll(-10) # 向下滚动10格
pyautogui.scroll(10, x=100, y=100) # 移动到(100, 100)位置再向上滚动10格

# 缓动/渐变函数可以改变光标移动过程的速度和方向。通常鼠标是匀速直线运动，这就是线性缓动/渐变函数。
# PyAutoGUI有30种缓动/渐变函数，可以通过pyautogui.ease*?查看。
# 开始很慢，不断加速
pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
# 开始很快，不断减速
pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
# 开始和结束都快，中间比较慢
pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)
# 一步一徘徊前进
pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)
# 徘徊幅度更大，甚至超过起点和终点
pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)
'''
haddle = compile(script, '', 'exec')


def download_file(x, y):  # 每个股票所在行的坐标
    pyautogui.moveTo(x, y)
    pyautogui.click(button='left')
    pyautogui.press('f10')
    pyautogui.moveTo(x=475, y=88)  # 财务透视按钮坐标
    pyautogui.click(button='left')
    file_list_cord = [(175, 249), (175, 284), (175, 315),
                      (167, 346), (182, 383), (181, 410)]  # 文件列表坐标
    import_data_cord = (199, 445)  # 导出数据按钮坐标
    for x_cord, y_cord in file_list_cord:
        pyautogui.click(button='left', x=x_cord, y=y_cord)
        pyautogui.click(
            button='left', x=import_data_cord[0], y=import_data_cord[1])
        pyautogui.click(button='left', x=394, y=686)  # 保存盘符按钮坐标
        pyautogui.click(button='left', x=1083, y=829)  # 保存按钮坐标
    pyautogui.click(button='left', x=1490, y=88)  # 单页关闭按钮坐标


def download(page_num, page_start=0, page_end=30, error_detact=True, pause_time=0.5):
    pyautogui.FAILSAFE = error_detact
    pyautogui.PAUSE = pause_time
    start_time = time.time()
    for i in range(page_num):
        for j in range(page_start, page_end):
            download_file(100, 110+j*22)
            if (j+1) % 30 == 0:
                pyautogui.click(button='left', x=1593, y=779)

    end = time.time()
    print("下载已经完成,共消耗时间%f" % (end-start_time))


if __name__ == '__main__':
    page_num = 2  # 总共下载页数
    page_start = 29  # 每页下载起始点
    pause_time = 0.5  # 鼠标点击暂停时间
    download(page_num=page_num, page_start=page_start, pause_time=pause_time)
