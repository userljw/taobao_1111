# -*- coding: utf-8 -*-


import cv2

def cv_find_circle(filename):

    img = cv2.imread(filename)
    # 灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 以圆形框出
    candidate_circle_list=[]
    for i in range(len(contours)):
        (x, y), radius = cv2.minEnclosingCircle(contours[i])
        center = (int(x), int(y))
        radius = int(radius)
        # 对圆进行筛选
        if radius <= 400 and radius >= 90:
            #先进行一轮筛选
            candidate_circle_list.append({"center":center,"radius":radius})
            img = cv2.circle(img, center, radius, (0, 255, 0), 2)

    # TODO
    # 排除
    # for one_circle in candidate_circle_list:
    #     center=one_circle[0]
    #     radius=one_circle[1]

    cv2.imwrite(filename.split(".")[0]+"_cv.png",img)
    return candidate_circle_list