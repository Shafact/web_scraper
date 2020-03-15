import requests
import re
import bs4

url = 'https://www.ebay.com/itm/CHANEL-Coco-Cocoon-Small-Tote-Leather-Black-A47108-Free-Shipping-/133298438568?hash=item1f0934c1a8'

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, features="lxml")

#eBay图片地址都存在这个division id为"PicturePanel"里
div = soup.find_all('div', id="PicturePanel")

#返回一个resultset，这个set其实是一个list，list中的每个元素都是一个BeautifulSoup的tag元素（可想象成dict）直接用["参数"]获得参数值，img标签的alt参数值其实正好是url里，item的名字
name_pattern = re.compile('itm/(.*?)-/')
item_name = re.findall(name_pattern,url)[0]
print(item_name, type(item_name))
img = soup.find_all('img',alt=re.compile(item_name))

#单独取出img里的source url组成一个list
img_list=[]
for i in img:
    img_list.append(i['src'])
# print(img_list)

#修改每一个网址，把最后的地址把s-l64.jpg改成s-l600.jpg就可以得到相对的大图了
pattern = re.compile('s-l[0-9]*.jpg')

for i in range(len(img_list)):
    img_list[i] = re.sub(pattern, 's-l600.jpg', img_list[i])
#print(img_list)

#去除img_list里的重复元素
clean_list = []

for element in img_list:
    if element in clean_list:
        pass
    else:
        clean_list.append(element)
clean_list.remove('') #去除空元素
print(clean_list)

#定义一个存照片的方法
def save_img(url,name):
    with open('/Users/sharonzhou/Documents/GitHub/web_scraper/ebay_images/test_items_image/'+ name,'wb') as f:
        f.write(requests.get(url).content)

#遍历每一个图片的url，然后将图片存下来，命名为item_name + 数字 + '.jpg'
count = 1
for element in clean_list:
    name = item_name + '-' + str(count) + '.jpg'
    save_img(element,name)
    count += 1
