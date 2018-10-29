---
title: 常用几种可视化图表的python实现
date: 2018-04-01 12:17:11
categories: Visualization

---

*------上马击狂胡，下马草军书。*



#### 散点图
``` python
import matplotlib.pyplot as plt
import numpy as np

def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r", yscale_log=False):

    # Create the plot object
    _, ax = plt.subplots()    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 30, color = color, alpha = 0.75)
    if yscale_log == True:
        ax.set_yscale('log')    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
np.random.seed(15)
X = np.random.randint(10,size=6)
y =  np.random.randint(10,size=6)
scatterplot(X,y,x_label=u"年龄", y_label="money", title="", color = "r")
plt.show()

```
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180401122727.png)

<!-- more -->
``` python

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r",s = 10, yscale_log=False):
    _, ax = plt.subplots()  

    ax.scatter(x_data, y_data, s, color, alpha=0.5, marker="*")
    if yscale_log == True:
        ax.set_yscale('log')    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
scatterplot(x,y,x_label=u"年龄", y_label="money", title="SB", color = colors, s = area)
plt.show()
```
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180401123035.png)


#### 折线图

``` python

def lineplot(x_data, y_data, x_label="", y_label="", title=""): 
    # Create the plot object 
    _, ax = plt.subplots()    # Plot the best fit line, set the linewidth (lw), color and 
    # transparency (alpha) of the line 
    ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)    # Label the axes and provide a title 
    ax.set_title(title) 
    ax.set_xlabel(x_label) 
    ax.set_ylabel(y_label) 
x = np.arange(0, 5, 0.1)
y = np.sin(x)
lineplot(x,y)
plt.show()
```
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180401123327.png)



#### 直方图

``` python

mean = 0  
sigma = 1  
x=mean+sigma*np.random.randn(100) 

# data实际上是数据的集合（y），用于观察数据分布情况
def histogram(data, n_bins, cumulative=False, x_label = "", y_label = "", title = ""):

    _, ax = plt.subplots()

    ax.hist(data, bins = n_bins, cumulative = cumulative, color = 'r')

    ax.set_ylabel(y_label)

    ax.set_xlabel(x_label)

    ax.set_title(title)

histogram(x,len(x)/2)
plt.show()

```
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180401125146.png)


#### 柱形图

``` python
def barplot(x_cnt, y_data, error_data, x_label="", y_label="", title="", xticklabels=""):

    _, ax = plt.subplots()

    # Draw bars, position them in the center of the tick mark on the x-axis
    ind = np.arange(x_cnt)  # the x locations for the groups
    width = 0.5       # the width of the bars
    rects1 = ax.bar(ind, y_data,width, color = '#539caf', align = 'center')
    ax.errorbar(ind, y_data, yerr = error_data, color = '#297083',ls = 'none', lw = 2, capthick = 2)
    
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_xticks(ind)
    ax.set_xticklabels(xticklabels)
    ax.set_title(title)
    
    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
        
xticklabels =  ('G1', 'G2', 'G3', 'G4')    
y_data = [15,23,28,12]
error_data = [2,2,1,3]
barplot(4, y_data, error_data)

plt.show()
```

![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180401125611.png)


``` python

def stackedbarplot(x_data, y_data_list, colors, y_data_names="", x_label="", y_label="", title=""):

    _, ax = plt.subplots()
    for i in range(0, len(y_data_list)):
        if i == 0:
            ax.bar(x_data, y_data_list[i], color = colors[i], align = 'center', label = y_data_names[i])
        else:
            ax.bar(x_data, y_data_list[i], color = colors[i], bottom = y_data_list[i - 1], align = 'center', label = y_data_names[i])
        
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)
        ax.set_title(title)
        ax.legend(loc = 'upper right')
y_data_list = [[3,3,3,3],[5,5,5,5],[11,11,11,45]]
x_data = np.arange(len(y_data_list[0]))
colors = ['r', 'b', 'y']
y_data_names = ["s1", "s2", "s3"]
stackedbarplot(x_data, y_data_list, colors, y_data_names)
plt.xticks(np.arange(len(y_data_list[0])), ('G1', 'G2', 'G3', 'G4'))
plt.yticks(np.arange(0, 81, 10))
plt.show()

```
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180401125856.png)


#### 箱线图
``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.random.seed(2)

df = pd.DataFrame(np.random.rand(5,4),columns=['A', 'B', 'C', 'D'])
p = df.boxplot(sym='r*',vert=True,patch_artist=True,meanline=False,showmeans=True, return_type='axes') 

# sym='r*',表示异常点的形状,
# vert表示横向还是竖向,
# patch_artist=True,（上下四分位框内是否填充，True为填充）
# meanline=False,showmeans=True，是否有均值线及其形状，meanline=True时，均值线也像中位数线一样是条红色线段，这样容易与中位数线混淆。

# medians, 是中位值的横线, 每个median是一个Line2D对象
# whiskers, 是指从box 到error bar之间的竖线.
# fliers, 是指error bar线之外的离散点.
# caps, 是指error bar横线.
# means, 是均值的横线.
type(p)
plt.show()

```
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180401130112.png)

+ 箱线图的异常值可以通过`p['fliers'][3].get_ydata()`获得


#### 还是使用[pyecharts](https://github.com/pyecharts/pyecharts)吧,好看。


### 参考
+ [https://matplotlib.org/examples/index.html](https://matplotlib.org/examples/index.html)
+ [https://weibo.com/ttarticle/p/show?id=2309404219702023946982](https://weibo.com/ttarticle/p/show?id=2309404219702023946982)
+ [https://www.jianshu.com/p/b2f70f867a4a](https://www.jianshu.com/p/b2f70f867a4a)