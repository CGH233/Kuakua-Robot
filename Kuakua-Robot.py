# -*- coding:utf-8 -*- 

import itchat, re
from itchat.content import *
import random
import json


REPLY = {'夸我': ['你真是太优秀！',
		'啥也不说了，夸！',
		'每天看到你心情好呢！',
		'你真是一位可爱的小天使啊！',
		'一看你就是美丽与善良的化身 夸！',			  
		'你上辈子一定拯救了银河系吧，优秀！',
		'德才兼备说的就是你这样的社会主义接班人！',
		'以后你就是夸夸群里的元老，就是夸夸之父，简称夸父！',
		'这句话完美的表达了你想被夸的坚定信念，你一定是一个执着追求自己理想的人！',
        '不知道有用没用还是进来求夸，说明是个勇于探索敢于进取的人！夸！',
        '人生总是有点**的，感谢你坚持下来，我们得幸又与你共度一天',
        '如出水芙蓉，天然雕饰，天哪！这世间怎么会有这么好看的人！',
        '名字好听！',
        '每一帧都是如此动人，夸！',
        '沉着冷静，说话之前深思熟虑，夸夸！'],
         'default': ['太棒了！',
		     '真不错！',
             '厉害！',
		     '好开心！',
             '你真好看',
             '干得好！！！',
             '加油哦',
             '加油！你是最棒的！放平心态！',
             '你是最棒哒！！！加油哇！！！！',
             '你已经做得很好了',
             '你们太好了呜呜呜呜呜',
		     '嗯哪！',
             '看到群友们的发言，真是好风采！',
             '大家好！群友们一看都非凡卓越！',
             '一切都会好起来的!',
		     '没什么好说的了，我送你一道彩虹屁吧！']}


         
@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
    if msg['User']['NickName'] == '哈哈哈哈':
        print('Message from: %s' % msg['User']['NickName'])
        username = msg['ActualNickName']
        print('Who sent it: %s' % username)

        normal_match = re.search('夸我|求夸|夸一下|夸|鼓励|来', msg['Text'])

        match = normal_match

        if match:
            if normal_match:
                print('-+-+' * 5)
                print('Message content:%s' % msg['Content'])
                print('夸我 is: %s' % (normal_match is not None))
                randomIdx = random.randint(0, len(REPLY['夸我']) - 1)
                itchat.send('@' + '%s\n%s' % (username, REPLY['夸我'][randomIdx]), msg['FromUserName'])
            
        print('isAt is:%s' % msg['isAt'])

        if not match:
            randomIdx = random.randint(0, len(REPLY['default']) - 1)
            itchat.send('@' + '%s\n%s' % (username, REPLY['default'][randomIdx]), msg['FromUserName'])
            print('-+-+'*5)

itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()

