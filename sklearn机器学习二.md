---
title: sklearn机器学习二
date: 2017-10-29 16:36:17
categories: Machine Learning
---
*------子规夜半犹啼血，不信东风唤不回。*


#### 特征工程
+ 数值型：可直接使用，也可以进行归一化、标准化提高模型的性能
 `sklearn.preprocessing.MinMaxScaler()`
+ 有序型：转换成数值，A--1，B--2，C--3
+ 类别型：独热编码
 `sklearn.preprocessing.OneHotEncoder()`

<!-- more -->
``` python
# 随机生成有序型特征和类别特征作为例子
X_train = np.array([['male', 'low'],
                  ['female', 'low'],
                  ['female', 'middle'],
                  ['male', 'low'],
                  ['female', 'high'],
                  ['male', 'low'],
                  ['female', 'low'],
                  ['female', 'high'],
                  ['male', 'low'],
                  ['male', 'high']])

X_test = np.array([['male', 'low'],
                  ['male', 'low'],
                  ['female', 'middle'],
                  ['female', 'low'],
                  ['female', 'high']])
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 在训练集上进行编码操作
label_enc1 = LabelEncoder() # 首先将male, female用数字编码
one_hot_enc = OneHotEncoder() # 将数字编码转换为独热编码

label_enc2 = LabelEncoder() # 将low, middle, high用数字编码

tr_feat1_tmp = label_enc1.fit_transform(X_train[:, 0]).reshape(-1, 1) # reshape(-1, 1)保证为一维列向量
tr_feat1 = one_hot_enc.fit_transform(tr_feat1_tmp) 
tr_feat1 = tr_feat1.todense()

tr_feat2 = label_enc2.fit_transform(X_train[:, 1]).reshape(-1, 1)

X_train_enc = np.hstack((tr_feat1, tr_feat2))
print(X_train_enc)
```

#### 交叉验证
模型的参数有两种，`自身参数`样本学习得到，模型自动更新，如逻辑回归、神经网络中的权重及偏置的学习；`超参数`手动设置的参数，如kmeans的k，神经网络中的网络层数及每层的节点个数。交叉验证就是帮助快速找到合适的超参。k-fold cross-validation,将数据分成k份，不放回每次取其中一份为测试集，其他为训练集，每次模拟得到一个准确值，然后取k次的平均值评估模型，一般会做多次k-fold cross-validation。
+ 交叉验证：`sklearn.model_selection.cross_val_score()`
+ 网格搜索：`sklearn.model_selection.GridSearchCV()`

##### 单一参数
``` python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

k_range = [5, 10, 15, 20]
cv_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=3) #X,y应该为全部数据，不是被split的，cv=3表示3fold
    cv_score = np.mean(scores)
    print('k={}，验证集上的准确率={:.3f}'.format(k, cv_score))
    cv_scores.append(cv_score)
best_k = k_range[np.argmax(cv_scores)]
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train_scaled, y_train)
print('测试集准确率：', best_knn.score(X_test_scaled, y_test))

```

##### 多个参数

``` python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

parameters = {'max_depth':[3, 5, 7, 9], 'min_samples_leaf': [1, 2, 3, 4]}
clf = GridSearchCV(DecisionTreeClassifier(), parameters, cv=3, scoring='accuracy')
clf.fit(X, y)
print('最优参数：', clf.best_params_)
print('验证集最高得分：', clf.best_score_)
best_model = clf.best_estimator_
print('测试集上准确率：', best_model.score(X_test, y_test))
```

#### 评价指标
<table><tr><td></td><td></td><td colspan="2" align="center">Prediction</td></tr>
<tr><td></td><td></td><td  align="center">Positive</td><td  align="center">Negative</td></tr>
<tr><td rowspan="2" align="center">Ground Truth</td><td align="center">Positive</td><td align="center">TP</td><td align="center">FN</td></tr>
<tr><td align="center">Negative</td><td align="center">FP</td><td align="center">TN</td></tr></table>

TRP(Recakk,召回率)：TP/(TP+TN)
Precision(精确率)：TP/(TP+FP)
FPR：FP/(TN+FP)
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20171029184051.png)

sklearn.metrics包含常用的评价指标：accuracy_score、precision_score、recall_score、f1_score

##### PR曲线（Precision-Recall Curve）
最理想的点是右上角，precision=1.0,recall=1.0,AUC的值就是曲线下的面积
`sklearn.metrics.precision_recall_curve()`

![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20171029193422PR.png)

##### ROC曲线（Receiver Operating Chaaracteristic Curve）
最理想的点是左上角，FPR=0.0，TPR=1.0
`sklearn.metrics.roc_curve()`

![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20171029193440ROC.png)

##### 混淆矩阵（confusion matrix）
用于多分类模型的评价，给出的是每一类预测的准确情况
`sklearn.metrics.confusion_matrix()`

![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20171029193502CM.png)

上述主要为分类和预测的评价指标，回归模型中常用的指标有
+ sklearn.metrics.r2_score()
+ sklearn.metrics.mean_absolute_error()
+ sklearn.metrics.mean_squared_error()
+ sklearn.metrics.median_absolute_error()
更多：[http://scikit-learn.org/stable/modules/model_evaluation.html](http://scikit-learn.org/stable/modules/model_evaluation.html)

#### 朴素贝叶斯
是构建分类器的简单方法，不是训练分类器的单一算法，是一系列基于相同原理的算法，前提条件是_需要假定每个特征与其他特征不相关_。效率高，可用于高维数据，通常作为模型比较的baseline，但分类想过不一定好，没有超参。
`sklearn.naive_bayes`

sklearn中的三种朴素贝叶斯算法：
+ Bernoulli：二元特征，如一个特征有没有出现
+ Multinomial：离散型特征，如单词出现次数
+ Gaussian：连续型特征

#### 随机森林
多个学习器的集成学习（Ensenle Learning），不需要过多的特征归一化和标准化
+ Bagging:个体学习器不存在依赖关系，如随机森林
+ boosting:个体学习器存在依赖关系，GBDT
随机包括两部分：随机采样和随机特征，通常选取特征数为k=log2d,d为总特征数。
*解释* Bagging，基于自助采样法（bootsrap sampling）:有放回采样，样本在m次采样中不被采到的概率是(1-1/m)^m,取极限=1/e，约为0.368。
`sklearn.ensemble.RandomForestClassifier`

重要参数:
+ n_estimators:包含决策树的个数
+ max_features:默认即可，可调整
+ max_depth:每棵决策树的深度

#### GBDT(Gradient Boosted(-ing) Descision Tree)
传统boosting关注的是先前基学习器做错的训练样本，然后基于调整后的样本分布来训练下一个基学习器，直到基学习器的数目达到预设的T值，最终将这个T个基学习器进行加权结合；而Gradient Boost是框架，可以嵌入不同的模型，迭代的方式是为了减少上一次的残差，在减少残差的梯度方向上建立新的模型，也就是每次建立的新树是前面所有树的结论和残差。不适合文本和高维数据。
`sklearn.ensemble.GradientBoostingClassifier`

重要参数:
+ n_estimators:包含决策树的个数
+ learning_rate:学习率，控制从上一次迭代中纠错的强度
+ max_depth:大多数应用中设置为3-5












