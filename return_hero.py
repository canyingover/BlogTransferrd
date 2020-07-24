# -*- coding: utf-8 -*-
# @Author: n4663
# @Date:   2017-09-29 17:08:32
# @Last Modified by:   n4663
# @Last Modified time: 2017-10-03 10:45:23
import json
f = open(u'return_hero.txt', 'r')
w = open(u'result.txt', 'w')

for line in f:
    if line == '\n':
        break
    else:
    #print len(line.strip().split('\t'))
        server = line.strip().split('\t')[18]
        role_id = line.strip().split('\t')[9]
        heroId = json.loads(line.strip().split('\t')[16])['heroId']
        star = json.loads(line.strip().split('\t')[16])['star']
        awake = json.loads(line.strip().split('\t')[16])['awake']
        level = json.loads(line.strip().split('\t')[16])['level']
        skinfo = str(json.loads(line.strip().split('\t')[16])['skinfo']).replace(' ','')

        lin = '\t'.join([str(server),str(role_id),str(heroId),str(star),str(level),str(awake),skinfo]) + '\n'
        w.write(lin)
f.close()
w.close()
