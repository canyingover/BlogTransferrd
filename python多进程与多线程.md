---
title: python多进程与多线程
date: 2017-02-12 10:39:50
categories: Python
---

*------五花马,千金裘,呼儿将出换美酒,与尔同销万古愁。*

越来越觉得自己对这些东西一知半解...
折腾了好久，今天整理一下我一知半解的 `python多进程与多线程` 毕竟每周还是应该多少有点什么值得记下来...

<!-- more --> 

首先理解：进程>线程（不知道可不可以这样讲），进程里至少有一个线程，线程之间共享内存空间，有其他进程占用内存空间时，需要等待内存闲置。
一篇文章：关于进程和线程区别的类比：
[http://www.ruanyifeng.com/blog/2013/04/processes_and_threads.html](http://www.ruanyifeng.com/blog/2013/04/processes_and_threads.html)

## 多进程

1.创建多进程的：使用`multiprocessing`模块的`Process`类


```python
from multiprocessing import Process
import os

def test(name):

    # os模块的getpid()方法可以获取当前进程的进程id
    print 'Run process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':

    print 'Main process %s.' % os.getpid()
    # 创建一个进程
    p = Process(target=test, args=('process1',))
    p.start()  # 调用start()方法，开始执行子进程
    p.join()  # 调用进程的join()方法，来阻塞除当前进程以外的所有进程,相当于是上锁的操作
    print 'test finished!'

```

2.依次创建进程进行一次计算并测试效率

```python
from multiprocessing import Process
import time


def test(num):
    sum = 0
    for i in range(0, num):
        sum += i
    return sum



if __name__ == '__main__':
    start_time = time.time()
    test(10000000)
    test(10000000)
    test(10000000)
    last_time = time.time() - start_time
    print last_time
	
	# 常规写法，耗时2.85500001907s

    p1 = Process(target=test, args=(10000000,))
    p2 = Process(target=test, args=(10000000,))
    p3 = Process(target=test, args=(10000000,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    # 多进程写法，耗时1.36999988556s


```
这里开启进程时要注意一点：先把所有`.start()`写完，再写`.join()`,这样发生进程阻塞的情况要少，这样就能充分发挥利用cpu，提高执行效率。

3.使用进程池的方式创建进程

```python
from multiprocessing import Pool
import time


def test(num):
    sum = 0
    for i in range(0, num):
        sum += i
    return sum


def test_test(num):
    a = test(num)
    b = test(num)
    c = test(num)
    return a+b+c

if __name__ == '__main__':
    start_time = time.time()
    pool = Pool(processes=3)
    result = pool.apply_async(test_test, args=(10000000,))
    pool.close()
    pool.join()
    print result.get() # 如果不获取结果，效率会高很多
    last_time = time.time() - start_time
    print last_time

# 耗时：3.21100020409s

```
注意两点：
+ 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool。
+ `apply`和`apply_async`的区别：`apply`主进程会阻塞于函数，主进程的执行流程同单进程一样；`apply_async`是非阻塞的且支持结果返回后进行回调，主进程循环运行过程中不等待`apply_async`的返回结果，在主进程结束后，即使子进程还未返回整个程序也会退出。虽然`apply_async`是非阻塞的，但其返回结果的get方法却是阻塞的，如使用result.get()会阻塞主进程。对返回结果不感兴趣， 那么可以在主进程中使用`pool.close`与`pool.join`来防止主进程退出。注意join方法一定要在close或terminate之后调用。

Pool相关函数：[https://docs.python.org/2/library/multiprocessing.html#module-multiprocessing.pool](https://docs.python.org/2/library/multiprocessing.html#module-multiprocessing.pool)



4.使用Pool的map方法，进行多进程（cpu密集型任务）操作伪代码

```python
from multiprocessing import Pool

def method1():
	return 被处理元素列表

def method2():
	进行处理的方法

if __name__ == '__mian__':
	
	pool = Pool()
	pool.map(method2, method1的结果)
	pool.close()
	pool.join()

```


## 多线程

多线程适用于io密集型的任务，暂时只记使用`multiprocessing.dummy`这一种实现方法

```python
import urllib2 
from multiprocessing.dummy import Pool as ThreadPool 

urls = [
    'http://www.python.org', 
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc.. 
    ]

# Make the Pool of workers
pool = ThreadPool(4) 
# Open the urls in their own threads
# and return the results
results = pool.map(urllib2.urlopen, urls)
#close the pool and wait for the work to finish 
pool.close() 
pool.join() 

```


## 总结几句：
+ IO 密集型任务选择`multiprocessing.dummy`，CPU 密集型任务选择`multiprocessing` 
+ 关于IO 密集型和CPU 密集型：
所谓IO密集型任务，是指磁盘IO、网络IO占主要的任务，计算量很小。比如请求网页、读写文件等。
所谓计算密集型任务，是指CPU计算占主要的任务，CPU一直处于满负荷状态。比如在一个很大的列表中查找元素，复杂的加减乘除等。


## 文章参考：
+ [一行 Python 实现并行化 -- 日常多线程操作的新思路](https://segmentfault.com/a/1190000000414339)
+ [python 中多进程以及多线程编程的总结](https://gold.xitu.io/entry/58218787da2f60005d11f2b5)


------写的过程中还看到了进程之间的通信与同时操作一个文件的进程锁的相关内容，只能慢慢来咯...