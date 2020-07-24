# -*- coding: utf-8 -*-
# @Author: n4663
# @Date:   2017-05-16 10:06:24
# @Last Modified by:   n4663
# @Last Modified time: 2018-09-22 14:07:19

from matplotlib import pyplot as plt
import datetime
import codecs
import os
import json
def mkdir(path):
    # 引入模块
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
    #     return True
    # else:
    #     # 如果目录存在则不创建，并提示目录已存在
    #     return False




def get_coordinate(filename):
    x_list = []
    y_list = []
    countline = 0
    with codecs.open(filename, 'r', encoding='utf-8') as f:

        for line in f:
            line_out = line.strip()
            #print line_out

            if u'mgdc_logtime' in line_out:
                continue

           # print line_out.split('\t')[12][:-2].split('"recordStr":"')[1].replace('\\','')

            #if json.loads(line_out.split('\t')[12].split('"}')[0].split('"recordStr":"')[1].replace('\\',''))['click_type'] == '2' :
            dataSet = json.loads(line_out.split('\t')[12][:-2].split('"recordStr":"')[1].replace('\\',''))['check_msg'][1:-1]

            # else:
            #dataSet = line_out.split('\\"check_msg\\": \\"{')[1].split('}\\", \\"click_type')[0]
            if len(dataSet) == 0:
                continue
            elif countline < 10:
                countline += 1
                rolename = line_out.split('\t')[11]
                if countline % 2==1:
                    xy_before = list(dataSet.split(','))
                    x2 = []
                    y2 = []
                    for xyb in xy_before:

                        x2.append(int(xyb.split(':')[0]))
                        y2.append(int(xyb.split(':')[1]))
                    x_list.append(x2)
                    y_list.append(y2)

                if countline % 2==0:
                    xy_after = list(dataSet.split(','))
                    x2 = []
                    y2 = []
                    for xya in xy_after:
                        x2.append(int(xya.split(':')[0]))
                        y2.append(int(xya.split(':')[1]))
                    x_list.append(x2)
                    y_list.append(y2)
    return rolename, countline/2, x_list, y_list


def match_scartter(sizes, rolename, xset_coordinate, yset_coordinate):

    nrows = sizes[0]
    ncols = sizes[1]

    fig, ax = plt.subplots(nrows, ncols, sharex=True, sharey=True, figsize=(15,15))
    i = 0
    for row in ax:
        if nrows == 1:
            x = xset_coordinate[i]
            y = yset_coordinate[i]
            ax.set_title(str(len(x)) + 'points')
            row.scatter(x, y, c='r', s=400, marker='.')

        else:
            for col in row:
                # col.plot(x, y)
                if i < sizes[0]*sizes[1] and i < 10:
                    x = xset_coordinate[i]
                    y = yset_coordinate[i]
                    col.set_title(str(len(x)) + 'points')
                    col.scatter(x, y, c='r', s=300, marker='.',edgecolors='red')
                    i += 1
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    mkpath = './' + now_time
    mkdir(mkpath)
    storge_path = './' + now_time + '/' + rolename + now_time + '.png'
    fig.savefig(storge_path, dpi=200)
    #plt.show()


if __name__ == '__main__':

    Rolename, CountLine, X_list, Y_list = get_coordinate(u'test.txt')
    sizes = [CountLine, 2]
    match_scartter(sizes, Rolename, X_list, Y_list)
