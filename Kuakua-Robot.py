# -*- coding:utf-8 -*- ：

import itchat, re
from itchat.content import *
import random
import json
import jieba
import jieba.analyse

with open('./douban/kuakua.json', 'r') as l:
    REPLY = json.load(l)[0]

titles = list(REPLY.keys())

def words_list(text):
    jieba.analyse.set_stop_words('./stopwords/百度停用词表.txt')
    tags = jieba.analyse.extract_tags(text,20)
    return tags

def choose_answer(title, match, username, msg):
    #print('-+-+' * 5)
    #print('Message content:%s' % msg['Content'])
    #print('match is: %s' % (match is not None))
    randomIdx = random.randint(0, len(REPLY[title]) - 1)
    itchat.send('@' + '%s\n%s' % (username, REPLY[title][randomIdx]), msg['FromUserName'])

def random_answer(username, msg):
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
        if not text:
            random_answer(username, msg)
            return 
        words = words_list(text)
        #print(words)
        for word in words:
            for title in titles:
                match = re.search(word, title)
                if match:
                    choose_answer(title, match, username, msg)
                    return
        random_answer(username, msg)
        #print('isAt is:%s' % msg['isAt'])
        #print('-+-+'*5)

itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()

