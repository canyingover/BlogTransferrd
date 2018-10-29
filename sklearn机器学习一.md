---
title: sklearn机器学习一
date: 2017-10-22 21:50:54
categories: Machine Learning
---
*------世间草木都美，人不是；中药很苦，你也是。*


#### KNN(k-NearestNeighbor),k-近邻算法
计算测试样本和所有训练样本的距离，选择最近的k个训练样本，统计k个训练样本的分类。

<!-- more -->
``` python
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

# 加载数据集
fruits_df = pd.read_csv('fruit_data_with_colors.txt', sep='\t', encoding='utf-8')
fruits_df.head()

# 划分数据集
X = fruits_df[['mass', 'width', 'height', 'color_score']]
y = fruits_df['fruit_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/4, random_state=0)

# 查看数据集 
sns.pairplot(data=fruits_df, hue='fruit_name', vars=['mass', 'width', 'height', 'color_score'])

# 选择模型 
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)

# 训练模型
knn.fit(X_train, y_train)

# 预测模型
y_pred = knn.predict(X_test)
print(y_pred)

# 效果
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_pred)

```

#### 线性回归
给定样本，通过加权求和该样本的特征值计算其结果并预测
求参方法：最小二乘法，即选择参数，使预测值和观测值（真实值）的平方和最小，该值称为残差平方和（residual sum of squares,RSS）

``` python
from sklearn.datasets import make_regression
X_R1, y_R1 = make_regression(n_samples = 100, n_features=1,
                            n_informative=1, bias = 150.0,
                            noise = 30, random_state=0)
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                  random_state = 0)
# 调用线型回归模型
linreg = LinearRegression()

# 训练模型
linreg.fit(X_train, y_train)

# 输出结果
print('线型模型的系数(w): {}'.format(linreg.coef_))
print('线型模型的常数项(b): {:.3f}'.format(linreg.intercept_))
print('训练集中R-squared得分: {:.3f}'.format(linreg.score(X_train, y_train)))
print('测试集中R-squared得分: {:.3f}'.format(linreg.score(X_test, y_test)))
```

#### 逻辑回归
将线性回归函数取对数，引入正则项，使回归结果可以用概率解释。
在sklearn中，logsitic regression的参数C使正则项系数的倒数，C=1/ λ，C小， λ大，正则化越弱，尽可能拟合训练样本数据，容易过拟合。
``` python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# 加载数据集
fruits_df = pd.read_table('fruit_data_with_colors.txt')

X = fruits_df[['width', 'height']]
y = fruits_df['fruit_label'].copy()

# 将不是apple的标签设为0
y[y != 1] = 0
# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/4, random_state=0)

# 不同的C值
c_values = [0.1, 1, 100]

for c_value in c_values:
    # 建立模型
    lr_model = LogisticRegression(C=c_value)

    # 训练模型
    lr_model.fit(X_train, y_train)

    # 验证模型
    y_pred = lr_model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print('C={}，准确率：{:.3f}'.format(c_value, acc))
    
```
#### 线性SVM
当线性分类器有多种选择时，在样本中能够达到最大间隔的线性分类器称为线性SVM（Linear Support Vector Machine）
在sklearn中，logsitic regression的参数C和论文的lambda一致，C大，正则化弱，容易过拟合。
`from sklearn.svm import SVC`

#### 决策树
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20171028094949.png)
pruing:[http://www.saedsayad.com/decision_tree_overfitting.htm](http://www.saedsayad.com/decision_tree_overfitting.htm)

sklearn决策树重要参数：
+ max_depth：树的最大深度（分割点个数）
+ min_samples_leaf：（每个叶子拥有的最少样本个数）
+ max_leaf_modes：叶子最大个数

``` python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

max_depth_values = [2, 3, 4]

for max_depth_val in max_depth_values:
    dt_model = DecisionTreeClassifier(max_depth=max_depth_val)
    dt_model.fit(X_train, y_train)
  
    print('max_depth=', max_depth_val)
    print('训练集上的准确率: {:.3f}'.format(dt_model.score(X_train, y_train)))
    print('测试集的准确率: {:.3f}'.format(dt_model.score(X_test, y_test)))

# 特征的贡献值
print (iris.feature_names)
print (dt_model.feature_importances_)
```



