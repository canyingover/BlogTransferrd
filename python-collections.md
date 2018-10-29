---
title: python collections
date: 2017-01-08 13:18:20
categories: Python
---
  具体实现方法参考文档：[https://docs.python.org/3/library/collections.html](https://docs.python.org/3/library/collections.html)

| container datetypes        | abstract           | Cool  |
| ------------- |:-------------:| -----:|
| deque      | 双端序列 | 有得必有失 |
| Counter      | 统计hashable objects      |   类似sql中的sum(A)...group by id |
| OrderedDict | 顺序存取的字典      |    None |
| defaultdict | key不存在时，赋予value默认值      |    实时统计玩家参与某副本的次数 |
| namedtuple() | 使tuple内的元素有自己的名称      |    坐标（x，y） |

<!-- more --> 
还有一些其他的类如*ChainMap*，暂时未归纳

#### defaultdict这个类想到的一些东西
+ 在实时获取玩家参与某个玩家的次数时，由于玩家id唯一，一般作为key，使用dict比较方便，还可以应用*json* （听说有另外一个ujson更好用，慢慢看吧）格式进行交互，但是一开始没有进入统计范围的玩家，获取key时会报错，使用*defaultdict*可以解决这个问题

```python
# 普通字典

In [7]: d = {}

In [8]: d['a']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-8-169a40407b7f> in <module>()
----> 1 d['a']

KeyError: 'a'
```
---------------------------------------------------------------------------

```python
# defaultdict
In [4]: from collections import defaultdict

In [5]: d = defaultdict(int)

In [6]: d['a']
Out[6]: 0
```

+ 实现hive中collect_all() 函数的函数,本来想在sqlite3上实现一下，但貌似不支持这个方法。

| color | count | 
| ------------- |:-------------:| 
| yellow	| 1	| 
| blue	 | 2	|   
| yellow | 3	|  
| blue | 4	|  
| red | 1 	|  


##### hive sql：
```
select color, collect_list(count) from test group by color

```

##### difaultdict：
```python
In [19]: s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

In [20]: d = defaultdict(list)

In [21]: for k, v in s:
    ...:     d[k].append(v)
    ...:

In [22]: d
Out[22]: defaultdict(list, {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]})
```



图床抽风用不了截图，就凑合着，中午没吃饭，又困又饿...
