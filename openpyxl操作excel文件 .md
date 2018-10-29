---
title: openpyxl操作excel文件 
date: 2016-12-31 10:46:29
categories: Excel
---


这个完全是为了熟悉hexo和markdown语法，上周末生日，来自一位朋友的工作需求

<!-- more --> 
### 需求描述
需要将目录中的每一行数据分别建立单独的工作表，应用工作表1的模板，并填入对于应的数据（红色框部分）

![图1](http://i1.piimg.com/567571/7b7b3f529bc43078.png)

![图2](http://i1.piimg.com/567571/c201f090d2a42726.png)

实现效果：
![图3](http://p1.bpimg.com/567571/ddb0b210b626cbd3.png)

### 实现过程
#### 第一步：批量生成指定名称的工作表，excel可直接操作
1. 选中“桥梁名称”列，先Alt+D，再Alt+P，插入数据透视表
2. 在数据透视表字段，将“桥梁名称”拖拽到筛选区域
3. 透视表“选项”，选择“显示报表筛选页”，确定

参考：[http://jingyan.baidu.com/article/6fb756ec8c6703241858fbba.html](http://jingyan.baidu.com/article/6fb756ec8c6703241858fbba.html)


#### 第二步：复制模板到各个工作表
这里只需要复制模板，全选模板内容，按住shift全选工作表，Ctrl+V复制即可


#### 第三步：填入数据
这应该是可以直接用excel完成的，比较菜，不会，选择了python *openpyxl* 模块操作excel的方式
参考{% raw %}openpyxl{% endraw %}文档：[http://openpyxl.readthedocs.io/en/default/usage.html](http://openpyxl.readthedocs.io/en/default/usage.html)

```python
# -*- coding:utf-8 -*-
from openpyxl import load_workbook
wb = load_workbook(filename = u"xxx.xlsx")

ws1 = wb.get_sheet_by_name(wb.get_sheet_names()[-2])
print ws1.title
hangshu = ws1.get_highest_row()

content = {}
def get_content():
	for i in range(2,217):
		if i < 11:
			key = '00' + str(i-1)
		elif i < 101:
			key = '0' + str(i-1)
		else:
			key =  str(i-1)
		name_index = 'C' + str(i)
		bianhao_index = 'B' + str(i)
		dengji_index = 'H' + str(i)
		xunhao_index = 'K' + str(i)
		name = ws1[name_index].value
		keyname = key + name
		bianhao = ws1[bianhao_index].value
		dengji = ws1[dengji_index].value
		xunhao = ws1[xunhao_index].value
		
		content[keyname] = [bianhao, dengji, xunhao, name]	
	return content

content = get_content()

ll = 0
for j in wb.get_sheet_names():
	print j
	print content[j][3]
	wb.get_sheet_by_name(j)['B3'] = content[j][3]
	wb.get_sheet_by_name(j)['D3'] = content[j][0]
	wb.get_sheet_by_name(j)['F3'] = content[j][1]
	wb.get_sheet_by_name(j)['F26'] = content[j][2]
	
	ll += 1
	if ll > 214:
		break 

wb.save(filename = 'aaa_test1.xlsx')
```




