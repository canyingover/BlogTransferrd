---
title: 图像像素块统计（with OpenCV）
date: 2017-06-06 22:54:09
categories: Python
---

*------十年热血写信仰，荣耀永不散场*

只有一个问题，统计如下`测试素材`图中有多少个连在一起的像素块。
![识别素材（test.png）](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20170606230724.png)
<!-- more --> 
### 实现过程
基本参考[这篇文章](http://sixthresearcher.com/counting-blue-and-white-bacteria-colonies-with-python-and-opencv/)简单修改，测试结果为13个像素块，原理不懂，看着看着才发现这个需求就是数细胞啊，当年还听老师讲过，我居然没有第一时间反应过来，Anyway，感谢google。

``` python


# -*- coding: utf-8 -*-

import numpy as np
import imutils
import cv2

def counter(filename):
    counter = {}

    image_orig = cv2.imread(filename)
    height_orig, width_orig = image_orig.shape[:2]

    # output image with contours
    image_contours = image_orig.copy()

    # DETECTING BLUE AND WHITE COLONIES
    colors = ['red']
    for color in colors:

        # copy of original image
        image_to_process = image_orig.copy()

        # initializes counter
        counter[color] = 0

        # define NumPy arrays of color boundaries (GBR vectors)
        if color == 'red':
            lower = np.array([ 0, 0, 255])
            upper = np.array([ 0, 0, 255])

        # find the colors within the specified boundaries
        image_mask = cv2.inRange(image_to_process, lower, upper)
        # apply the mask
        image_res = cv2.bitwise_and(image_to_process, image_to_process, mask = image_mask)

        ## load the image, convert it to grayscale, and blur it slightly
        image_gray = cv2.cvtColor(image_res, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.GaussianBlur(image_gray, (5, 5), 0)

        # perform edge detection, then perform a dilation + erosion to close gaps in between object edges
        image_edged = cv2.Canny(image_gray, 50, 100)
        image_edged = cv2.dilate(image_edged, None, iterations=1)
        image_edged = cv2.erode(image_edged, None, iterations=1)

        # find contours in the edge map
        cnts = cv2.findContours(image_edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        # loop over the contours individually
        for c in cnts:
            # if the contour is not sufficiently large, ignore it
            if cv2.contourArea(c) < 5:
                continue
            # compute the Convex Hull of the contour
            hull = cv2.convexHull(c)
            if color == 'red':
                # prints contours in red color
                cv2.drawContours(image_contours,[hull],0,(0,0,0),1)

            counter[color] += 1
            #cv2.putText(image_contours, "{:.0f}".format(cv2.contourArea(c)), (int(hull[0][0][0]), int(hull[0][0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

        # Print the number of colonies of each color
        return counter[color]
        #print("{} {} colonies".format(counter[color],color))

    # Writes the output image
    # cv2.imwrite(args["output"],image_contours)

if __name__ == '__main__':
    print counter(u'test.png')

```

### 主要坑点
1、 没法直接安装*cv2*，通过`pip install opencv-python`安装*opencv*,后`import cv2`成功。
2、 这里最难的应该是设置合适的像素值，红色的RGB代码是（255，0，0），但是这里`lower = np.array([ 0, 0, 255])`,用的是GBR（叫你不认真看注释）