# -*- coding: gbk -*-
import time,datetime,os
ftime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
reducepath = "%sn7746gmwgcmd_reduce_item.txt"%ftime
mailpath = "%sn7746gmwgcmd_sendtxt.txt"%ftime
lockpath = "%sn7746gmwgcmd_lock_avatar.txt"%ftime
otherpath = "%sn7746gmwgcmd_other.txt"%ftime
weixipath = "%sn7746wg_vipάϵ.txt"%ftime
wanfalockpath = "%sn7746gmwgcmd_lock_wanfa.txt"%ftime
a = 1

while True:
    if os.path.exists(reducepath):
        reducepath = "%sn7746gmwgcmd_reduce_item-%s.txt"%(ftime,str(a))
        a +=1
    else:
        break
a = 1
while True:
    if os.path.exists(mailpath):
        mailpath = "%sn7746gmwgcmd_sendtxt-%s.txt"%(ftime,str(a))
        a +=1
    else:
        break
a = 1
while True:
    if os.path.exists(lockpath):
        lockpath = "%sn7746gmwgcmd_lock_avatar-%s.txt"%(ftime,str(a))
        a +=1
    else:
        break

a = 1
while True:
    if os.path.exists(otherpath):
        otherpath = "%sn7746gmwgcmd_other-%s.txt"%(ftime,str(a))
        a +=1
    else:
        break

a = 1
while True:
    if os.path.exists(wanfalockpath):
        wanfalockpath = "%sn7746gmwgcmd_lock_wanfa-%s.txt"%(ftime,str(a))
        a +=1
    else:
        break


a = 1
while True:
    if os.path.exists(weixipath):
        weixipath = "%sn7746gmwg_vipάϵ-%s.txt"%(ftime,str(a))
        a +=1
    else:
        break
    
raw_input('��ȷ���Ƿ��ѹ��˴�����ʷ��Ȼ�����ɴ�����ʽ')

url = "http://www.16163.com/zt/yys/shensushuoming/"
link_title = "�ύ����"
#reducebeizhu = "���:��ʼ�Ż��գ��״�������������̳"
sender = "��ʹ��"
title = "���Թ�ʹ�ڵ���"
docmd = open(reducepath,'a')
mail = open(mailpath,'a')
lockavatar = open(lockpath,'a')
other = open(otherpath,'a')
weixi = open(weixipath,'a')
wanfa = open(wanfalockpath,'a')
intxt = open('in.txt','r')
#try:
for i in intxt:
    #print i
    if i.strip() == '':continue

    if '����' not in i:
        lines = i.strip().split('\t')
        server,role_id,dj,xf,rq,wgcs,kctl,kcjb,gz= lines
        if role_id == '57fbc0bba4bcaf43dfb03692':
            print '�������˺�57fbc0bba4bcaf43dfb03692����'
            continue
        if role_id == '57fc72d578d9600dcbfca0ce':
            print '�������˺�57fc72d578d9600dcbfca0ce����'
            continue
        if role_id == '5c361593904cb55246b80fe8':
            print '����������˺�����'
            continue
        if role_id == '57e9513f8dda761ebc8ade09':
            print '����������˺�����'
            continue
        if role_id == '584550130a5b565de19f33d5':
            print '����������˺�����'
            continue
        if role_id == '581f04d913f2c15b413df80d':
            print '����������˺�����'
            continue
        if role_id == '5ad5fb8b67c29a3d305328bf':
            print '����������˺�����'
            continue
        if role_id == '5854af8cb807da46d81e47ca':
            print '����������˺�����'
            continue
        if role_id == '581b28557bbb5a0509d8c519':
            print '����������˺�����'
            continue
        if role_id == '580d6156d533f62687f83f5b':
            print '����������˺�����'
            continue
        if role_id == '57d2f9d8c28c9f7f339ad53f':
            print '����������˺�����'
            continue
        if role_id == '5886d6eee47c576aa284ebba':
            print '����������˺�����'
            continue
        if role_id == '5bad97e327004f7c5e681da1':
            print '����������˺�����'
            continue
        #������,role_id,�ȼ�,����,Υ������,Υ�����,�۳���������,�۳��������,������
        #kctl=1600
        #kcjb=5000000
        if int(kctl)<35000:
            reduceitem = "[[900003,%s]]"%kctl
            reduceitem2= "[[900001,%s]]"%kcjb
            #gz=cfbz.split('(')[1].split(')')[0]
            #kcbeizhu = "���Υ��۳��������״�������������̳"
            #gz='����'
            #gz='xwjc'
            locktime=10080
            if int(xf)>10000:
                locktime=4320
            #cfbz2='�̶�:B|��Ұ�����Υ��(%s)-�����淨%s����|Υ������:%s'%(gz,locktime,rq)
            cfbz2='{"ischufa":"1","account_id":"","urs":"","level":"B","type":"2_D_4","reason":"��Ұ�����Υ��(%s)-�����淨%s����|Υ������:%s"}'%(gz,locktime,rq)
            #cfbz3='�̶�:B|��Ұ�����Υ��(%s)-�۳�����%s|Υ������:%s'%(gz,kctl,rq)
            cfbz3='{"ischufa":"1","account_id":"","urs":"","level":"B","type":"2_L_4","reason":"��Ұ�����Υ��(%s)-�۳�����%s|Υ������:%s"}'%(gz,kctl,rq)
            #cfbz4='�̶�:B|��Ұ�����Υ��(%s)-���ս��%s|Υ������:%s'%(gz,kcjb,rq)
            cfbz4='{"ischufa":"1","account_id":"","urs":"","level":"B","type":"2_L_4","reason":"��Ұ�����Υ��(%s)-���ս��%s|Υ������:%s"}'%(gz,kcjb,rq)
            #content='''����ʦ���ã��������Ľ�ɫ������ʹ�ø�������򹤾���Ϊ(����ʹ��Сֽ�˹��ܲ����ܵ���Ӱ��)����������ƽ������������ֶ������ʺŽ�ɫ���н�ֹ���벿���淨%s���ӡ��۳�����%s�����ս��%s�Ĵ���������ؼ�ʱֹͣʹ���쳣��������򹤾ߣ������������븨������������ļ������ٴα����Υ�潫��ȡ��һ�������ʩ����������������ʱ��ֹ��½/�����淨���������㡢������ֵ�����÷�ͣ�ȣ���ϣ������֮�����Ϸ���������򣬹�ͬά����ɫ��ƽ����Ϸ������'''%(locktime,kctl,kcjb)
            #content=('�װ�������ʦ����:                                                             '\�������Ľ�ɫ������ʹ�ø�������򹤾���Ϊ(����ʹ��Сֽ�˹��ܲ����ܵ���Ӱ��)����������ƽ������������ֶ������ʺŽ�ɫ���н�ֹ���벿���淨%s���ӡ��۳�����%s�����ս��%s�Ĵ���������ؼ�ʱֹͣʹ���쳣��������򹤾ߣ������������븨������������ļ������ٴα����Υ�潫��ȡ��һ�������ʩ����������������ʱ��ֹ��½/�����淨���������㡢������ֵ�����÷�ͣ�ȣ���ϣ������֮�����Ϸ���������򣬹�ͬά����ɫ��ƽ����Ϸ������''')%(locktime,kctl,kcjb)
            #content='%s%s%s'%(locktime,kctl,kcjb)
            content = ('�װ�������ʦ����:                                                             '\
            '�������Ľ�ɫ������ʹ�ø�������򹤾���Ϊ(����ʹ��Сֽ�˹��ܲ����ܵ���Ӱ��)����������ƽ������������ֶ������ʺŽ�ɫ���н�ֹ���벿���淨%s���ӡ��۳�����%s�����ս��%s�Ĵ���������ؼ�ʱֹͣʹ���쳣��������򹤾ߣ������������븨������������ļ������ٴα����Υ�潫��ȡ��һ�������ʩ����������������ʱ��ֹ��½/�����淨���������㡢������ֵ�����÷�ͣ�ȣ���ϣ������֮�����Ϸ���������򣬹�ͬά����ɫ��ƽ����Ϸ������''')%(locktime,kctl,kcjb)
            mail.write(("%s\t%s\t\t%s\t%s\t%s\t%s\t%s\t\t%s\n"%(server,role_id,sender,title,content,url,link_title,cfbz2)).decode('gbk').encode('utf8'))
            wanfa.write(("%s\t%s\t%s\t%s\n"%(server,role_id,locktime,cfbz2)).decode('gbk').encode('utf8'))
            docmd.write(("%s\t%s\t\t%s\t\t\t\t\t%s\n"%(server,role_id,reduceitem,cfbz3)).decode('gbk').encode('utf8'))#����
            docmd.write(("%s\t%s\t\t%s\t\t\t\t\t%s\n"%(server,role_id,reduceitem2,cfbz4)).decode('gbk').encode('utf8'))#���
            if int(xf)>9999:
                #cfbz5='�����淨%s����+�۳�����%s+���ս��%s|Υ������:%s'%(locktime,kctl,kcjb,rq)
                cfbz5='{"ischufa":"1","account_id":"","urs":"","level":"B","type":"2_L_4","reason":"�����淨%s����+�۳�����%s+���ս��%s|Υ������:%s"}'%(locktime,kctl,kcjb,rq)
                weixi.write(("%s\t"*11%('�����ศ��',rq,server,role_id,'','aid_weizhi','nc_weizhi',xf,dj,cfbz5,'1')+'\n').decode('gbk').encode('utf8'))#άϵ
        else:
            print 'error,��ע�����������Ƿ���ȷ'
        
        




print '������'


docmd.close()
mail.close()
intxt.close()
lockavatar.close()
other.close()
weixi.close()
wanfa.close()
raw_input('over')
