---
title: 异常值(outlier)检测
date: 2018-04-22 09:55:16
categories: Machine Learning
---


*------不专业，但想做专业的事情。*


#### 正态分布
也可以成为高斯分布，通过已知分布的`期望`和`方差`估计新样本的概率，再与某经验定值进行比较，例如，在正态分布的假设下，区域 \mu\pm 3\sigma 包含了99.7% 的数据，如果某个值距离分布的均值 \mu 超过了 3\sigma，那么这个值就可以被简单的标记为一个异常点（outlier）。


#### 箱线图
直接计算箱线图的分位数：最小估计值：Q1-k(Q3-Q1)；最大估计值：Q3+k(Q3-Q1)。超过该范围的值可简单定义为异常值。


<!-- more -->
#### Local Outlier Factor(LOF) 局部异常因子算法
基本原理：[https://zhuanlan.zhihu.com/p/28178476](https://zhuanlan.zhihu.com/p/28178476)

**K-邻近距离(k-distance)：**p为关注点，第 k 个最近 p 的点与 p 之间的距离称为k-distance(p)
**可达距离(rechability distance)：**数据点 p 到 数据点 o 的可达距离 reach-dist（p, o）为数据点 o 的K-邻近距离(情况一：p 到 o 的距离要比 p 的第 k 近点近) 和 数据点 p 与点 o 之间的直接距离的最大值(情况二：p 到 o 的距离要比 p 的第 k 近点远)。
**局部可达密度(local rechability density)：**对于数据点 p，那些跟点 p 的距离小于等于 k-distance（p）的数据点称为它的 k-nearest-neighbor，记为 $N_k(p)$，数据点 p 的局部可达密度为它与邻近的数据点的平均可达距离的倒数。一个数据点跟其他点比较疏远的话，那么显然它的局部可达密度就小。
**局部异常因子(local outlier factor)：**数据点 p 的局部相对密度（局部异常因子）为点p的邻居们的平均局部可达密度跟数据点p的局部可达密度的比值。LOF分数小于1则p处于一个相对密集的区域；LOF分数大于1则p跟其他点比较疏远。

![](http://okqlmzer2.bkt.clouddn.com/v2-b1527f2cdc286e2e60aea59c7f4f0514_hd.jpg)


``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors.lof import LocalOutlierFactor 

np.random.seed(42)
# Generate train data
X = 0.3 * np.random.randn(90, 3)

# Generate some abnormal novel observations
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 3))

X = np.r_[X + 2, X - 2, X_outliers]

# fit the model
clf = LocalOutlierFactor(n_neighbors=20, algorithm="auto", leaf_size=30, metric="minkowski", p=2, contamination=0.1, n_jobs=1)
y_pred = clf.fit_predict(X)

pd1 = pd.DataFrame(data=X,columns=["f1", "f2", "f3"])
pd1["result"] = y_pred
print pd1.loc[pd1["result"] == -1]

```


#### IsolationForest example 孤立森林

基本原理：每次用一个随机超平面切割数据空间，如此往复，指导每子空间只有一个数据为止，直观上，密度越低，越早被分割出来。

``` python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

rng = np.random.RandomState(42)

# Generate train data
X = 0.3 * rng.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Generate some regular novel observations
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# Generate some abnormal novel observations
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))

# fit the model
clf = IsolationForest(max_samples=100, random_state=rng)
clf.fit(X_train)
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)

```

#### 参考
+ [http://scikit-learn.org/stable/modules/outlier_detection.html](http://scikit-learn.org/stable/modules/outlier_detection.html)