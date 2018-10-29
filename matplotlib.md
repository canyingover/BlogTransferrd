---
title: matplotlib
date: 2017-02-26 16:01:05
categories: Visualization

---

*------愿你不惧荒唐，敢爱如初*

从需求出发，第一次体验`matplotlib`模块。
### 需求描述
为每位玩家生成一张图表，反映其在过去一周游戏货币来源途径的占比，以及其与人工预设的上一阶层的来源对比情况。效果如下：<!-- more --> 
![效果图](http://okqlmzer2.bkt.clouddn.com/role_id2.png)

### 生成简单的条形图
参考文档内容：[barchart_demo.py](http://matplotlib.org/examples/api/barchart_demo.html)
代码已经很接近需求，稍微修改一下，设置了不透明度参数、使用中文标注和稍微修改了一下颜色。实现效果：
![条线图效果](http://okqlmzer2.bkt.clouddn.com/figure_1.png)

``` python
   # -*- coding:utf-8 -*-
   import numpy as np
   import matplotlib.pyplot as plt

   N = 5
   yoursdata = (20, 35, 30, 35, 27)
   men_std = (2, 3, 4, 1, 2)

   ind = np.arange(N)  # the x locations for the groups
   width = 0.35       # the width of the bars
   opacity = 0.4      # 不透明级别
   fig, ax = plt.subplots()
   rects1 = ax.bar(ind, yoursdata, width, 
                color='b', 
                alpha=opacity, 
                yerr=men_std)

   target_data = (25, 32, 34, 20, 25)
   women_std = (3, 5, 2, 3, 3)
   rects2 = ax.bar(ind + width, target_data, width, 
                color='r', 
                alpha=opacity, 
                yerr=women_std)

   # add some text for labels, title and axes ticks
   ax.set_ylabel(u'数量(单位：万)')
   ax.set_title(u'金币周获得量对比图')
   ax.set_xticks(ind + width)
   ax.set_xticklabels(('way1', 'way2', 'way3', 'way4', 'way5'))

   ax.legend((rects1[0], rects2[0]), (u'您', u'对比群体'))


   def autolabel(rects):
       """
       Attach a text label above each bar displaying its height
       """
       for rect in rects:
           height = rect.get_height()
           ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                   '%d' % int(height),
                   ha='center', va='bottom')

   autolabel(rects1)
   autolabel(rects2)

   plt.show()
```


+ 对于`ax.legend()`的设置，也可以直接在`ax.bar`创建是赋以参数`label`,然后调用`ax.legend()`即可，不用再次传入参数：

``` python
   rects1 = ax1.bar(index, yoursdata, bar_width,
                 alpha=opacity,
                 color='b',
                 label=u'您')
   ax1.legend()
```

+ `matplotlib`默认不支持在`label`等参数中传入中文，[这里](http://www.yeolar.com/note/2011/04/28/matplotlib-tips/)有三种解决办法，笔者直接尝试了第三种方法，成功解决问题
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20170226181042.png)

### 生成简单的饼形图(同理，比较简单，不赘述。)
参考文档内容：[pie_demo_features.py](http://matplotlib.org/examples/pie_and_polar_charts/pie_demo_features.html)




### 两张图合并成一张
参考文档内容：[subplots_demo.py](http://matplotlib.org/examples/pylab_examples/subplots_demo.html)

只需要创建两个`subplot`，分别绘制`bar`和`pie`即可，以下三种创建`subplot`的写法效果一致。到这里，基本上已经完成了整个思路，最后可能需要通过`plt.figure()`对象的一些参数调节整个图的呈现效果，细节不详述。

``` python
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

plt.close('all')

# Two subplots, the axes array is 1-d
f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(x, y)
axarr[0].set_title('Sharing X axis')
axarr[1].scatter(x, y)

# Two subplots, unpack the axes array immediately
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True) # 两行一列
ax1.plot(x, y)
ax1.set_title('Sharing X axis')
ax2.scatter(x, y)

# Two subplots, unpack the axes array immediately
fig = plt.figure()
ax1 = fig.add_subplot(211) # 两行一列第一个
ax2 = fig.add_subplot(212) # 两行一列第二个
ax1.plot(x, y)
ax1.set_title('Sharing X axis')
ax2.scatter(x, y)

plt.show()
```

### 保存图片

`plt.show()`只展示绘图界面，无法实现保存，保存命令需要用到`fig.savefig()`和`fig.close()`,在循环中调用时，如果不使用`fig.close()`，其效果是在上一张图的基础上继续作图。


最后，读取数据文件，循环生成图片即可，这里我使用json格式存储数据，结构如下：

``` json
{
"role_id2":
{"selfget_top5":{"way1":10,"way2":14,"way3":12,"way4":7,"way5":3},
"cha_self_top5":{"wayA":15,"wayB":13,"wayC":12,"wayD":7,"wayE":6},
"cha_target_top5":{"wayA":19,"wayB":17,"wayC":14,"wayD":8,"wayE":7}},

"role_id1":
{"selfget_top5":{"way1":15,"way2":13,"way3":12,"way4":7,"way5":3},
"cha_self_top5":{"wayA":15,"wayB":13,"wayC":12,"wayD":7,"wayE":7},
"cha_target_top5":{"wayA":19,"wayB":17,"wayC":14,"wayD":8,"wayE":7}}
}

```

最后，未经优化，基本满足需求的脚本：

``` python
# -*- coding:utf-8 -*-
"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""

import numpy as np
import json
import codecs
import matplotlib.pyplot as plt

def get_explode(selfdata):
    explode = [0, 0, 0, 0, 0]
    a = selfdata.index(max(selfdata))
    explode.pop(a)
    explode.insert(a, 0.1)
    return explode

def autolabel(rects, ax):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')


def jinbiduibitu(filename, selfdata, selftujing, yoursdata, targetdata, tujinglist, explode):

    N = 5
    labels = selftujing
    sizes = selfdata
    men_std = (2, 3, 4, 1, 2)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    opacity = 0.4      # 不透明度
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    rects1 = ax1.bar(ind, yoursdata, width,
                    color='b',
                    alpha=opacity,
                    yerr=men_std)

    women_std = (2, 3, 4, 1, 2)
    rects2 = ax1.bar(ind + width, targetdata, width,
                    color='r',
                    alpha=opacity,
                    yerr=women_std)

    # add some text for labels, title and axes ticks
    ax1.set_ylabel(u'数量(单位：万)')
    ax1.set_title(u'金币周获得量对比图')
    ax1.set_xticks(ind + width)
    ax1.set_xticklabels(tujinglist)
    autolabel(rects1, ax1)
    autolabel(rects2, ax1)
    ax1.legend((rects1[0], rects2[0]), (u'您', u'对比群体'))


    piecs = ['red', 'yellow', 'Maroon', 'blue', 'Orange']
    ax2.pie(sizes, colors=piecs, explode=explode, labels=labels, autopct='%1.2f%%',
                 shadow=True, startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title(u'个人金币周获得量渠道占比图', x=0.5,y=1.1)
    fn = './barchart_demo_output/' + filename + '.png'
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4) # 调整图间距
    #plt.show()
    plt.savefig(fn)
    plt.close()




if __name__ == '__main__':

    with codecs.open('barchart_demo_input.txt', 'r', encoding = 'utf-8', errors = 'ignore') as f:
        d = json.load(f)
    print len(d)
    for i in d.keys():
        filename = i
        tujinglist = d[i]['cha_self_top5'].keys()
        selfdata = []
        selftujing = d[i]['selfget_top5'].keys()
        for k in selftujing:
            sg = d[i]['selfget_top5'][k]
            selfdata.append(sg)
        yoursdata = []
        targetdata = []
        for j in tujinglist:
            yd = d[i]['cha_self_top5'][j]
            td = d[i]['cha_target_top5'][j]
            yoursdata.append(yd)
            targetdata.append(td)
        explode = get_explode(selfdata)

        jinbiduibitu(filename,selfdata, selftujing, yoursdata, targetdata, tujinglist, explode)



```

