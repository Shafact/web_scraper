import requests
import csv
import re

#DOUBAN'S API can't be accessed oversea. So we changed it to http://www.tvmaze.com/api
#Q1: Use http://www.tvmaze.com/api 接口，获得电视剧"Person of Interest" 的海报地址，下载海报到本地；
#02：Use http://api.tvmaze.com/shows?page=1 接口，批量获取Show的名字，genres，评分等数据，保存数据到本地CSV
#03：Use 上述的thing接口，获取每一部海报的url，批量下载电影海报到本地


#Q1: <PERSON OF INTEREST> API IS http://api.tvmaze.com/shows/2

while True:
    try:
        url = 'http://api.tvmaze.com/shows/2'

        res = requests.get(url)
        #获得的数据是json格式，用json方法转化为字典
        res = res.json()

        #获取海报url： key 为image, 选择"original"
        poster_url = res['image']['original']
    except:
        print("Can't access show's url")
        break

    try:
        poster_res = requests.get(poster_url)
    #把海报存在当前文件夹的子文件夹-douban images 的子文件夹（POI),命名为poster
    except:
        print("Can't access poster url")
        break

    try:
        with open('./douban_images/POI/poster.jpg', 'wb') as f:
            f.write(poster_res.content)
    except Exception as e:
        print('Error:', e)
    break
    #print(res, type(rep))
    # print("content type:", type(res.content))


#02: http://api.tvmaze.com/shows?page=1

try:
    url = 'http://api.tvmaze.com/shows?page=1'

    res = requests.get(url)
    res = res.json()

    #创造一个空list来储存每部电影需要的信息
    show_list = []

    #遍历每一个电影，把主要信息存在show_list里
    for i in range(len(res)):
        showDic = res[i]
        cleanr = re.compile('<.*?>') #用正则把html的tag去掉
        show = {'name':'','rating': 0.00, 'genres':[], 'summary':'', 'image':''}
        show['name'] = showDic['name']
        show['rating'] = showDic['rating']['average']
        show['genres'] = showDic['genres']
        show['summary'] = re.sub(cleanr, '', showDic['summary'])
        show['image'] = showDic['image']['medium']
        show_list.append(show)

    #准备CSV的header
    headers = list(show_list[0].keys())

    #print(show_list)
    #将show_list写到csv里
    with open('show_list.csv','w') as f:
        #运用csv的DictWriter方法，先写下header，再写show_list
        dict_writer = csv.DictWriter(f, headers)
        dict_writer.writeheader()
        dict_writer.writerows(show_list)
except Exception as e:
    print('Error:', e)


#03 存下每张图片，每张图片命名为show的名字，位置在


def save_poster(url,name):
    path = './douban_images/' + name + '.jpg'
    poster_res = requests.get(url)
    with open(path, 'wb') as f:
            f.write(poster_res.content)

try:
    for element in show_list:
        save_poster(element['image'],element['name'])
except Exception as e:
    print('Error:', e)

