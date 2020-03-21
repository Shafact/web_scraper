import requests
import csv

url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=cbb266c5cf58b8713f0456cae25169e6'

headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) " \
               "Chrome/80.0.3987.132 Safari/537.36',
    'Cookie': '_zap=fc92f9f2-c834-44d0-8250-6725c185979d; _xsrf=0fa23a1e-28d5-4fdd-a806-4f80f2d12623; '
              '_ga=GA1.2.1183325924.1583983531; d_c0="AKCZjVRF8xCPTh4o0c5HjcSUsoXkrSu4uXA=|1583983535"; capsion_ticket="2|1:0|10:1583983539|14:capsion_ticket|44:NDEwMzU4ZWU1ZmE4NGJlZmE5MzY3ZTM3YjczN2ExZjM=|100461388ce9f981f9526f9a7d2752f1720b7356e474c57401f3ea2ce28a8980"; z_c0="2|1:0|10:1583983554|4:z_c0|92:Mi4xekFvSUFBQUFBQUFBb0ptTlZFWHpFQ1lBQUFCZ0FsVk53dmxXWHdDT0RRZWlfVTM5Y3lZRGJqZHVwRHcyc1ZUM0Z3|8cb49ceb2172bb4d7e1502a02d8474d8c5979c98ca246115b3065bc92dbd41ac"; tst=r; _gid=GA1.2.288283951.1584826824; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1583983532,1584826825,1584826844; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1584826844; KLBRSID=d1f07ca9b929274b65d830a00cbd719a|1584828568|1584826823',
}

res = requests.get(url,headers=headers)

data = res.json().get('data')
targets = []
answers = []
articles = []

# 把target的内容提取出来
for element in data:
    targets.append(element.get('target'))

#separate article and answers type
for element in targets:
    if element.get('type') == 'answer':
        answers.append(element)
    else:
        articles.append(element)

#因为answers的字典里的keys 和articles的keys不一样，所以我们分别处理，建立两个csv files
try:
    answers_header=list(answers[0].keys())
    print("answers' keys: ", answers_header, type(answers_header))
    with open('zhihu_feed_answers.csv','w') as f:
        #建立dict_writer 对象，匹配要写的file 和header
        dict_writer = csv.DictWriter(f,answers_header)
        #写下headers
        dict_writer.writeheader()
        #写下list里每一个dict元素，每一个占一行
        dict_writer.writerows(answers)
except:
    print("No answer type, all!")

try:
    articles_header=list(articles[0].keys())
    print("articles' keys: ", articles_header, type(articles_header))
    with open('zhihu_feed_articles.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, articles_header)
        dict_writer.writeheader()
        dict_writer.writerows(articles)
except:
    print("No article type!")





