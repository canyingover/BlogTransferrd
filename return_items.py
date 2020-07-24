# -*- coding: utf-8 -*-
# @Author: n4663
# @Date:   2017-09-29 17:08:32
# @Last Modified by:   n4663
# @Last Modified time: 2018-08-23 11:34:32
import json
f = open(u'return_items.txt', 'r')
w = open(u'result.txt', 'w')

for line in f:
    if line == '\n':
        break
    else:
    #print len(line.strip().split('\t'))
        server = json.loads(line.strip().split('\t')[0])['hostnum']
        role_id = json.loads(line.strip().split('\t')[0])['role_id']

        items_name = eval(str(json.loads(line.strip().split('\t')[0])['items']))[0][0]
        items_num = eval(str(json.loads(line.strip().split('\t')[0])['items']))[0][1]

        beizhu = line.strip().split('\t')[1]
        chuliren = line.strip().split('\t')[2]
        if items_name == 900001:
            shang = items_num / 1000000
            yushu = items_num % 1000000
            while shang >= 10:
                jinbi_line = '[' + ('[900001,1000000],'*10)[0:-1] + ']'
                lin = '\t'.join([str(server),str(role_id),jinbi_line,str(beizhu),str(chuliren)]) + '\n'
                shang -= 10
                w.write(lin)
            if shang != 0:
                jinbi_line = '[' + ('[900001,1000000],'*shang)[0:-1] + ']'
                lin = '\t'.join([str(server),str(role_id),jinbi_line,str(beizhu),str(chuliren)]) + '\n'
                w.write(lin)

            if yushu != 0 :
                lin = '\t'.join([str(server),str(role_id),"[[900001,{}]]".format(str(yushu)),str(beizhu),str(chuliren)]) + '\n'
                w.write(lin)
        if items_name == 900003:
            shang = items_num / 500
            yushu = items_num % 500
            while shang >= 10:
                tili_line = '[' + ('[900003,500],'*10)[0:-1] + ']'
                lin = '\t'.join([str(server),str(role_id),tili_line,str(beizhu),str(chuliren)]) + '\n'
                shang -= 10
                w.write(lin)
            if shang != 0:
                tili_line = '[' + ('[900003,500],'*shang)[0:-1] + ']'
                lin = '\t'.join([str(server),str(role_id),tili_line,str(beizhu),str(chuliren)]) + '\n'
                w.write(lin)
            if yushu != 0 :
                lin = '\t'.join([str(server),str(role_id),"[[900003,{}]]".format(str(yushu)),str(beizhu),str(chuliren)]) + '\n'
                w.write(lin)


f.close()
w.close()
raw_input('ok')
