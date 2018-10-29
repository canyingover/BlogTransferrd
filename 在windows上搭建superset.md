---
title: 在windows上搭建superset
date: 2017-10-15 23:29:21
categories: BigData
---

*------三尺青锋怀天下，一骑白马开吴疆。*


安装文档：[http://superset.apache.org/installation.html](http://superset.apache.org/installation.html)
#### 创建虚拟环境
`pip install superset`

#### 激活虚拟环境
`superset\Scripts\activate superset`
<!-- more --> 
#### 初始化的事情基本与文档一致，只是需要切换到envs\superset\Scripts下，将所有`superset`替换成`python superset`
``` python
# Install superset
pip install superset

# Create an admin user (you will be prompted to set username, first and last name before setting a password)
fabmanager create-admin --app superset

# Initialize the database
python superset db upgrade

# Load some data to play with
python superset load_examples

# Create default roles and permissions
python superset init

# Start the web server on port 8088, use -p to bind to another port
python superset runserver

# To start a development web server, use the -d switch
# python superset runserver -d

```

#### 连接数据库进行可视化
打开[http://localhost:8088](http://localhost:8088)，输入原先设置好的账号密码即可登陆。登陆后打开sources-databases，新建一个数据库连接，如下图修改相关信息即可，之后就可以使用sql提取数据并进行可视化了。
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20171022212044.png)
![](http://okqlmzer2.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20171022212440.png)

#### 相关问题

+ sasl.h找不到：
下载合适版本的whl文件手动安装[http://www.lfd.uci.edu/~gohlke/pythonlibs/#sasl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#sasl)。
+ "module" object has no attribute ‘SIGALRM‘错误：
windows下依赖包不兼容，把signal所在行都注释，下面再加一个pass就好了，文件在superset/utils.py。
+ localhost:8088无法打开：
可能是所处环境设置了代理，使用火狐浏览器设置无代理模式或者使用内网ip进行访问。
+ 由于 gunicorn 不支持 Windows，所以只能运行开发环境。



