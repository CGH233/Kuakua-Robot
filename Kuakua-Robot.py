# -*- coding:utf-8 -*- ：

import itchat, re
from itchat.content import *
import random
import json
import jieba
import jieba.analyse

with open('./douban/kuakua_corpus/2019-05-09-20-16.json', 'r') as l:
    REPLY = json.load(l)[0]

titles = list(REPLY.keys())

reply = {'夸': ['你真是太优秀！',
		'啥也不说了，夸！',
		'每天看到你心情好呢！',
		'你真是一位可爱的小天使啊！',
		'一看你就是美丽与善良的化身 夸！',
		'你上辈子一定拯救了银河系吧，优秀！',
		'德才兼备说的就是你这样的社会主义接班人！',
		'以后你就是夸夸群里的元老，就是夸夸之父，简称夸父！',
		'你这句话完美的表达了你想被夸的坚定信念，你一定是一个执着追求自己理想的人！',
        '能在这里遇到你真好，你让我觉得世界都变美好了！', 
        '在我心里天山雪莲也不及您回眸一笑更加动人',
        '您的妙语连珠让人实在忍俊不禁，按耐不住好奇心，发现您在魔都。真的让我瞬间对着一片土地爱的升华了！我为了您！为了您的才华！我心甘情愿替您吸雾霾而绝不说一个“不”字儿！',
        '太棒了！',
        '这美丽的天气本来就是为你而存在的，能被你瞧见，就是它的荣耀!',
        '比今天的你更漂亮的，是明天的你。',
        '如果你的美是一氧化碳，那我现在可能要窒息而亡了',
        '你的确很漂亮，笑一笑更美！',
        '我要向你学习！',
        '厉害！',
        '好看',
        '你真棒=￣ω￣=',
        '飘飘兮若回风之流雪。',
        '写到水穷天杪，定非尘土间人。',
		'真羡慕你！',
        '太有文化了！',
        '天气因你而美丽！',
        '加油，想给你一个拥抱',
        '加油！都说苦尽甘来！不经历风雨怎么见彩虹',
        '加油＾０＾~',
        '奇怪！心脏怎么跳得这么快！',
        '真不错！',
        '你真是一个可爱美丽天真活泼大方优雅的人啊',
		'你美的天上有地下无，那可是活脱脱的七仙女儿啊！',
        '你长这么美貌还这么有爱，真是让人嫉妒！',
        '好开心！',
		'嗯哪！',
		'没什么好说的了， 我送你一道彩虹屁吧！']}

def words_list(text):
    jieba.analyse.set_stop_words('./stopwords/百度停用词表.txt')
    tags = jieba.analyse.extract_tags(text,20)
    if tags:
        return tags
    else:
        return jieba.cut(text, cut_all=True)

def choose_answer(title, match, username, msg):
    #print('-+-+' * 5)
    #print('Message content:%s' % msg['Content'])
    #print('match is: %s' % (match is not None))
    if len(REPLY[title]) <= 1:
        itchat.send('@' + '%s\n%s' % (username, REPLY[title][0]), msg['FromUserName'])
        return
    randomIdx = random.randint(0, len(REPLY[title]) - 1)
    itchat.send('@' + '%s\n%s' % (username, REPLY[title][randomIdx]), msg['FromUserName'])

def random_answer(username, msg):
    random_id = random.randint(0, len(REPLY) - 1)
    random_title = titles[random_id]
    while len(REPLY[random_title]) <= 1:
        random_id = random.randint(0, len(REPLY) - 1)
        random_title = titles[random_id]
    randomIdx = random.randint(0, len(REPLY[random_title]) - 1)
    itchat.send('@' + '%s\n%s' % (username, REPLY[random_title][randomIdx]), msg['FromUserName'])

@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
    if msg['User']['NickName'] == '数舆夸夸群':
        #print('Message from: %s' % msg['User']['NickName'])
        username = msg['ActualNickName']
        #print('Who sent it: %s' % username)        
        text = msg['Text']
        if len(text) <= 4 and re.search('夸', text):
            randomIdx = random.randint(0, len(reply['夸']) - 1)
            itchat.send('@' + '%s\n%s' % (username, reply['夸'][randomIdx]), msg['FromUserName'])
            return
        words = words_list(text)
        #print(words)
        match_title = []
        for word in words:
            for title in titles:
                match = re.search(word, title)
                if match:
                    match_title.append(title)
        if len(match_title) > 1:
            random_id = random.randint(0, len(match_title) - 1)
            title = match_title[random_id]
            choose_answer(title, match, username, msg)
            return
        elif len(match_title) == 1:
            choose_answer(match_title[0], match, username, msg)
            return
        random_answer(username, msg)
        #print('isAt is:%s' % msg['isAt'])
        #print('-+-+'*5)
'''
'''
itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()
