import requests
import re
from bs4 import BeautifulSoup
import json

group = 'kuakua'
url = 'https://www.douban.com/group/' + group + '/'
titles = {}
result = []

def get_full_list(url):
  html = requests.get(url).text
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup.find_all('td', class_='title')
  for tag in tags:
      try:
          title = tag.a['title']
          detal_url = tag.a['href']
          comments = get_comment(detal_url)
          if comments:
            titles[title] = comments
      except:
          pass

def get_comment(url):
    comments = []
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('p', class_='reply-content')
    for tag in tags:
        try:
            comment = tag.contents[0]
            comment = re.sub("[a-zA-Z0-9\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：]+", ""    , comment)
            comments.append(comment)
        except:
            pass
    return comments

num = int(input("请输入想爬取的页数："))
for page in range(1, num+1):
  print("正在爬取第{}页".format(page))
  urls = url + 'discussion?start=' + str(page*25)
  get_full_list(urls)

result.append(titles)

with open('kuakua.json', 'w') as k:
    json.dump(result, k)
