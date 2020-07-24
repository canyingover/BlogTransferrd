# -*- coding: gbk -*-
import time,datetime,os
ftime = time.strftime("%Y-%m-%d",time.localtime(time.time()))
reducepath = "%sn7746gmwgcmd_reduce_item.txt"%ftime
mailpath = "%sn7746gmwgcmd_sendtxt.txt"%ftime
lockpath = "%sn7746gmwgcmd_lock_avatar.txt"%ftime
otherpath = "%sn7746gmwgcmd_other.txt"%ftime
weixipath = "%sn7746wg_vip维系.txt"%ftime
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
        weixipath = "%sn7746gmwg_vip维系-%s.txt"%(ftime,str(a))
        a +=1
    else:
        break
    
raw_input('请确认是否已过滤处罚历史，然后生成处罚格式')

url = "http://www.16163.com/zt/yys/shensushuoming/"
link_title = "提交申诉"
#reducebeizhu = "外挂:初始号回收，首次来单引导至论坛"
sender = "鬼使黑"
title = "来自鬼使黑的信"
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

    if '消费' not in i:
        lines = i.strip().split('\t')
        server,role_id,dj,xf,rq,wgcs,kctl,kcjb,gz= lines
        if role_id == '57fbc0bba4bcaf43dfb03692':
            print '白名单账号57fbc0bba4bcaf43dfb03692跳过'
            continue
        if role_id == '57fc72d578d9600dcbfca0ce':
            print '白名单账号57fc72d578d9600dcbfca0ce跳过'
            continue
        if role_id == '5c361593904cb55246b80fe8':
            print '法务白名单账号跳过'
            continue
        if role_id == '57e9513f8dda761ebc8ade09':
            print '法务白名单账号跳过'
            continue
        if role_id == '584550130a5b565de19f33d5':
            print '法务白名单账号跳过'
            continue
        if role_id == '581f04d913f2c15b413df80d':
            print '法务白名单账号跳过'
            continue
        if role_id == '5ad5fb8b67c29a3d305328bf':
            print '法务白名单账号跳过'
            continue
        if role_id == '5854af8cb807da46d81e47ca':
            print '法务白名单账号跳过'
            continue
        if role_id == '581b28557bbb5a0509d8c519':
            print '法务白名单账号跳过'
            continue
        if role_id == '580d6156d533f62687f83f5b':
            print '法务白名单账号跳过'
            continue
        if role_id == '57d2f9d8c28c9f7f339ad53f':
            print '法务白名单账号跳过'
            continue
        if role_id == '5886d6eee47c576aa284ebba':
            print '法务白名单账号跳过'
            continue
        if role_id == '5bad97e327004f7c5e681da1':
            print '法务白名单账号跳过'
            continue
        #服务器,role_id,等级,消费,违规日期,违规次数,扣除体力数量,扣除金币数量,检测规则
        #kctl=1600
        #kcjb=5000000
        if int(kctl)<35000:
            reduceitem = "[[900003,%s]]"%kctl
            reduceitem2= "[[900001,%s]]"%kcjb
            #gz=cfbz.split('(')[1].split(')')[0]
            #kcbeizhu = "外挂违规扣除御札，首次来单引导到论坛"
            #gz='加速'
            #gz='xwjc'
            locktime=10080
            if int(xf)>10000:
                locktime=4320
            #cfbz2='程度:B|外挂按键类违规(%s)-冻结玩法%s分钟|违规日期:%s'%(gz,locktime,rq)
            cfbz2='{"ischufa":"1","account_id":"","urs":"","level":"B","type":"2_D_4","reason":"外挂按键类违规(%s)-冻结玩法%s分钟|违规日期:%s"}'%(gz,locktime,rq)
            #cfbz3='程度:B|外挂按键类违规(%s)-扣除体力%s|违规日期:%s'%(gz,kctl,rq)
            cfbz3='{"ischufa":"1","account_id":"","urs":"","level":"B","type":"2_L_4","reason":"外挂按键类违规(%s)-扣除体力%s|违规日期:%s"}'%(gz,kctl,rq)
            #cfbz4='程度:B|外挂按键类违规(%s)-回收金币%s|违规日期:%s'%(gz,kcjb,rq)
            cfbz4='{"ischufa":"1","account_id":"","urs":"","level":"B","type":"2_L_4","reason":"外挂按键类违规(%s)-回收金币%s|违规日期:%s"}'%(gz,kcjb,rq)
            #content='''阴阳师您好，由于您的角色近期有使用辅助程序或工具行为(正常使用小纸人功能不会受到此影响)，严重扰乱平安世界的秩序，现对您的帐号角色进行禁止参与部分玩法%s分钟、扣除体力%s及回收金币%s的处理。请您务必及时停止使用异常辅助程序或工具，并彻底清理与辅助程序关联的文件，如再次被检测违规将采取进一步处理措施（包括但不限于暂时禁止登陆/冻结玩法、体力清零、倒扣数值、永久封停等），希望您在之后的游戏中遵守秩序，共同维护绿色公平的游戏环境！'''%(locktime,kctl,kcjb)
            #content=('亲爱的阴阳师大人:                                                             '\由于您的角色近期有使用辅助程序或工具行为(正常使用小纸人功能不会受到此影响)，严重扰乱平安世界的秩序，现对您的帐号角色进行禁止参与部分玩法%s分钟、扣除体力%s及回收金币%s的处理。请您务必及时停止使用异常辅助程序或工具，并彻底清理与辅助程序关联的文件，如再次被检测违规将采取进一步处理措施（包括但不限于暂时禁止登陆/冻结玩法、体力清零、倒扣数值、永久封停等），希望您在之后的游戏中遵守秩序，共同维护绿色公平的游戏环境！''')%(locktime,kctl,kcjb)
            #content='%s%s%s'%(locktime,kctl,kcjb)
            content = ('亲爱的阴阳师大人:                                                             '\
            '由于您的角色近期有使用辅助程序或工具行为(正常使用小纸人功能不会受到此影响)，严重扰乱平安世界的秩序，现对您的帐号角色进行禁止参与部分玩法%s分钟、扣除体力%s及回收金币%s的处理。请您务必及时停止使用异常辅助程序或工具，并彻底清理与辅助程序关联的文件，如再次被检测违规将采取进一步处理措施（包括但不限于暂时禁止登陆/冻结玩法、体力清零、倒扣数值、永久封停等），希望您在之后的游戏中遵守秩序，共同维护绿色公平的游戏环境！''')%(locktime,kctl,kcjb)
            mail.write(("%s\t%s\t\t%s\t%s\t%s\t%s\t%s\t\t%s\n"%(server,role_id,sender,title,content,url,link_title,cfbz2)).decode('gbk').encode('utf8'))
            wanfa.write(("%s\t%s\t%s\t%s\n"%(server,role_id,locktime,cfbz2)).decode('gbk').encode('utf8'))
            docmd.write(("%s\t%s\t\t%s\t\t\t\t\t%s\n"%(server,role_id,reduceitem,cfbz3)).decode('gbk').encode('utf8'))#体力
            docmd.write(("%s\t%s\t\t%s\t\t\t\t\t%s\n"%(server,role_id,reduceitem2,cfbz4)).decode('gbk').encode('utf8'))#金币
            if int(xf)>9999:
                #cfbz5='冻结玩法%s分钟+扣除体力%s+回收金币%s|违规日期:%s'%(locktime,kctl,kcjb,rq)
                cfbz5='{"ischufa":"1","account_id":"","urs":"","level":"B","type":"2_L_4","reason":"冻结玩法%s分钟+扣除体力%s+回收金币%s|违规日期:%s"}'%(locktime,kctl,kcjb,rq)
                weixi.write(("%s\t"*11%('按键类辅助',rq,server,role_id,'','aid_weizhi','nc_weizhi',xf,dj,cfbz5,'1')+'\n').decode('gbk').encode('utf8'))#维系
        else:
            print 'error,请注意体力数量是否正确'
        
        




print '输出完毕'


docmd.close()
mail.close()
intxt.close()
lockavatar.close()
other.close()
weixi.close()
wanfa.close()
raw_input('over')
