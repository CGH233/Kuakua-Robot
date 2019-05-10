# _*_ coding: utf-8 _*_

import re
import time
import json

titles = {}
result = []

with open('douban_kuakua_topic.txt', 'r') as t:
    for topic in t.readlines():
        comments = []
        cut = re.search('<######>', topic)
        if cut is None:
            continue
        cut = cut.span()
        title = topic[:cut[0]]
        if title is None:
            continue
        if re.search('~', title):
            continue
        topic = topic[cut[1]:]
        while len(topic) > 0:
            cut = re.search('<', topic)
            if cut == None:
                break
            cut = cut.span()
            comment = topic[:cut[0]] 
            if re.search('~', comment) is None:
                comments.append(comment)    
            topic = topic[cut[1]+7:]
        if comments:
            titles[title] = comments

result.append(titles)

name = str(time.strftime("%Y-%m-%d-%H-%M", time.localtime())) + '.json'

with open(name, 'w') as k:
    json.dump(result, k)

print("----------over!!!!-------------")
