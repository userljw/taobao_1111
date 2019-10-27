# -*- coding: utf-8 -*-
import os
import time
from xiaoliudeAI import cv_find_circle
from baiduOCR import getCode

#配置环境变量
ADB_TOOL_PAHT=r"D:\CODE\taobao_1111\adb_tool"

os.environ['path']=os.environ['path']+";"+ADB_TOOL_PAHT


def pull_screenshot(filname):
    os.system('adb shell screencap -p /sdcard/{}'.format(filname))
    os.system('adb pull /sdcard/{} .'.format(filname))
    return filname


def swipe_up(px=1350):
    os.system('adb shell input swipe 100 {} 100 100 500'.format(1350+100))

def tap(x=0,y=0):
    os.system('adb shell input tap {x} {y}'.format(x=x,y=y))

def back():
    os.system('adb shell input keyevent 4')

def look_detail():
    for i in range(5):
        os.system('adb shell input swipe 200 1000 200 100 500')
        time.sleep(3)

if __name__ == '__main__':
    #手动进入首屏

    for i in range(4):
        # 滑动到店铺列表
        swipe_up()
        filename="screencut{}.png".format(str(i))
        pull_screenshot(filename)
        #分析图像
        candidate_circle_list=cv_find_circle(filename)

        for circle in candidate_circle_list:
            xy_point=circle.get("center")
            x_point=xy_point[0]
            y_point=xy_point[1]
            # 进入店铺
            tap(x=x_point,y=y_point)


            # 判断是否逛过
            time.sleep(1)
            detial_file_name='detial.png'
            pull_screenshot(detial_file_name)
            res=getCode(detial_file_name)
            if '今日已达上限' in res:
                import sys
                print("今日已达上限")
                sys.exit()
            if "任务完成" in res or "继续逛逛吧" in res:
                back()
            else:
                print("逛店中...................")
                look_detail()
                back()



