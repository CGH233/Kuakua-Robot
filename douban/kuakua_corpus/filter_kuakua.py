from filter import DFAFilter

gfw = DFAFilter()
gfw.parse('keywords')

write_file = open('clean_kuakua.txt', 'a')

topics = []

with open('douban_kuakua_topic.txt', 'r') as t:
    for topic in t.readlines():
        topic = gfw.filter(topic, "~")
        topics.append((topic).encode('utf-8'))
write_file.writelines(topics)


