import requests
import re


#Example 1 find all title of movies
"""
url = "https://static1.scrape.cuiqingcai.com"

data = {
    'name': 'germey',
    'age': 25
}
r = requests.get(url, params=data)

#print(r.text, type(r.text))

pattern = re.compile(r"<h2.*?>(.*?)</h2>",re.S)

title = re.findall(pattern,r.text)

print(pattern,title)
"""

#Example 2 save images videos and audios (byte type)
"""
url = "https://github.com/favicon.ico"

r = requests.get(url)

with open('favicon.ico','wb') as f:
    f.write(r.content)
"""

#Example 3 adding headers
"""
url = "https://static1.scrape.cuiqingcai.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 '
                  'Safari/537.36',
}
r = requests.get(url, headers=headers)

#print(r.text, type(r.text))

pattern = re.compile(r"<h2.*?>(.*?)</h2>",re.S)

title = re.findall(pattern,r.text)

print(title)
"""


# Example 4 Post method
"""
url = "http://httpbin.org/post"

data = {
    'name': 'germey',
    'age': '25'
}

r = requests.post(url, data=data)

print(r.text, type(r.text))
"""

#Example 5 Response
"""
url = "https://static1.scrape.cuiqingcai.com"

r = requests.get(url)
print(type(r.status_code),r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
"""

#Example 6 Status code test
"""
url = "https://static1.scrape.cuiqingcai.com"

r = requests.get(url)

if not r.status_code == requests.codes.ok:
    exit()
else:
    print('Request Successfully')
"""

# Example 7 Upload files
"""
files = {'file': open('favicon.ico','rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
"""

#Example 8 Cookies
"""
url = "https://github.com/"

headers = {
   'Cookie': '_octo=GH1.1.766780395.1583973596; _ga=GA1.2.2009317487.1583975594; '
             'experiment:homepage_signup_flow=eyJ2ZXJzaW9uIjoiMSIsInJvbGxPdXRQbGFjZW1lbnQiOjc2LjY1ODcxOTM1MzUzMTIsInN1Ymdyb3VwIjpudWxsLCJjcmVhdGVkQXQiOiIyMDIwLTAzLTEyVDAxOjEzOjE0LjI4OVoiLCJ1cGRhdGVkQXQiOiIyMDIwLTAzLTEyVDAxOjEzOjE0LjI4OVoifQ==; _gat=1; tz=America%2FNew_York; _device_id=027e018320dc534858e369e138a2afcd; has_recent_activity=1; user_session=0-XmWvwiSoh_sRTK1UoZyniWmpMEuyF0EFcwndhyRZTf8kSW; __Host-user_session_same_site=0-XmWvwiSoh_sRTK1UoZyniWmpMEuyF0EFcwndhyRZTf8kSW; logged_in=yes; dotcom_user=Shafact; _gh_sess=Lq24kl6SA6Kr2Zk3Q7ur9sNobv9udY910B73WbRtQscq8Wam35r0sFM6riJFRWnwjQoCZ0Kit%2FZen9Fnaw3z1ty6eri5A91S5b8VQ%2Fh03lvi%2Bwa6JD9Y%2BgPjaJU3i6ehACeBxDlAJTuXAZsONAsVuzwniL7YJ9PhYOcGIVmu0ayOHQGCqBeMaT5HBv7eLfmprT7AekA%2BfiQ2J2SgD%2FUV06DegvJLZSaggXwBKWEkbXTB9nU2lIzoDBMMJ187DFuYscxil%2B9ghAJ%2BIRepr9uWDTjEKaTiEWUfxtJxIzMVYifagqlPwrosX5hbXR7cjm3k%2FkL2JAR8Uer%2BfOLLTqZe2pySVsA57AYTUIZLNaCYcVCeathWsp63L1X6d3OC0%2FLYzfzHWEBbvrxHOp3gD3%2Bx563y23hva0HHSB0fn2pKFONRLReGiBM1JCk32cY80J7ja0TvZcXuVQocXsdsKrce8zB3IWnPvOgZjZ6q%2FDGDLQFJ32DR8Ukwms%2Ba8IaROLOJNYRcW80VYFU3dUsU9K1YFVlF4IQ8q%2FAkvuuPcv%2Fe1PfyTsHe72aPv3V2ldrVEkkcew%2FoVIbL5ULJQoUU42P6DCiDin2a8jJxaoEVx2MgmrEnSeA5bKeTLoDmHxXUt2jZ%2BhBQCMGQkjdzViPPLGkVZMOW9sAf64Z2b%2FwzZKGDoJo5HGEIpzeRMvJXkrqO347NdC9FcEFLFrjfxL2mM1bZJsFmHmEOfgsRHc7OtkgIhmFkeX7dgx8%2F4O8%2Bg8Ikm4%2B8rWsQjLIv1N7QI1UwmNBaqSKB8x9TF7yrBOy80XElPEVZYvuEuu6UXTUBODs2t0Uqhz0DKR071bBLHTvmTcUqQPSITIsNsrJ1CKijaWmsiHvU5gGLCiKUBBYjfymqOVfDhWK6qGzsQvom3IT%2FXXklWm0jHapKMmCuV9OefxooeJx710snmlinOqP2TA3ONq%2F28o6yaai%2BdWt3OXm9rUIcIQJvzKTB8sJj9FsdTxZe9BfPVqyPAmMuKp0Tv%2BR45VDEc8xVdst39Ti3XVELJTqAemz%2BjyUOP0tlgrgK%2FWZvEkCg4WJ1MhGAKPqeW%2BASdmPrZPrTHwD8z8TVnTEXp90JMRaxalIT20g%2Fid0JQT1vW%2FJFWoCLiBiDyqsDHxyrp%2BliZWITZlXopg4UYiPO3qesOPglld2xR7Iip0dt22zXuT7TZYK6OhqrXp%2BxA8rzFyAib6dVsukbQJWbBvSQ7E%2BDT8gD0iwPT8etyxMZ2b4m%2FbY9ddX7QytJYo8w4GJfm5RMADxHSDukk3OXoqSeme%2F7SpWA8yE66E8lAGJpqaAF6e0b4n%2BLCVECA8WJNYy8%2BHjhFnNZd05Dz8oq3u3u5BKZyuj0hK267INay7NhzenUI6qWu4B4uCNFt05RmU4jL%2FqHNvS2C4pMF8QsGR%2BllVK2fjOy3DKBzQ3x41h9brypc8wBSflnhDJNe9PfT9LHGKG0ynwN3K6LRNYN%2FM38uHZcV7a0vBXvSf1okUyHQx3yscZr0K95PRzWoU60i7eXc1B7lTAQz5HlAVyTZbj1cPWU%2FtJo12VErnhWGJwCHg%3D%3D--Hd3gVYRjdq4a23qR--f238jGM%2B%2BoGQg%2FKBas%2Bf%2FQ%3D%3D',

   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

r = requests.get(url, headers=headers)

print(r.text)
"""

#Example 9 Set Cookie Jar
"""
url = 'https://github.com'

cookies = '_octo=GH1.1.766780395.1583973596; _ga=GA1.2.2009317487.1583975594; experiment:homepage_signup_flow=eyJ2ZXJzaW9uIjoiMSIsInJvbGxPdXRQbGFjZW1lbnQiOjc2LjY1ODcxOTM1MzUzMTIsInN1Ymdyb3VwIjpudWxsLCJjcmVhdGVkQXQiOiIyMDIwLTAzLTEyVDAxOjEzOjE0LjI4OVoiLCJ1cGRhdGVkQXQiOiIyMDIwLTAzLTEyVDAxOjEzOjE0LjI4OVoifQ==; _gat=1; tz=America%2FNew_York; _device_id=027e018320dc534858e369e138a2afcd; has_recent_activity=1; user_session=0-XmWvwiSoh_sRTK1UoZyniWmpMEuyF0EFcwndhyRZTf8kSW; __Host-user_session_same_site=0-XmWvwiSoh_sRTK1UoZyniWmpMEuyF0EFcwndhyRZTf8kSW; logged_in=yes; dotcom_user=Shafact; _gh_sess=Lq24kl6SA6Kr2Zk3Q7ur9sNobv9udY910B73WbRtQscq8Wam35r0sFM6riJFRWnwjQoCZ0Kit%2FZen9Fnaw3z1ty6eri5A91S5b8VQ%2Fh03lvi%2Bwa6JD9Y%2BgPjaJU3i6ehACeBxDlAJTuXAZsONAsVuzwniL7YJ9PhYOcGIVmu0ayOHQGCqBeMaT5HBv7eLfmprT7AekA%2BfiQ2J2SgD%2FUV06DegvJLZSaggXwBKWEkbXTB9nU2lIzoDBMMJ187DFuYscxil%2B9ghAJ%2BIRepr9uWDTjEKaTiEWUfxtJxIzMVYifagqlPwrosX5hbXR7cjm3k%2FkL2JAR8Uer%2BfOLLTqZe2pySVsA57AYTUIZLNaCYcVCeathWsp63L1X6d3OC0%2FLYzfzHWEBbvrxHOp3gD3%2Bx563y23hva0HHSB0fn2pKFONRLReGiBM1JCk32cY80J7ja0TvZcXuVQocXsdsKrce8zB3IWnPvOgZjZ6q%2FDGDLQFJ32DR8Ukwms%2Ba8IaROLOJNYRcW80VYFU3dUsU9K1YFVlF4IQ8q%2FAkvuuPcv%2Fe1PfyTsHe72aPv3V2ldrVEkkcew%2FoVIbL5ULJQoUU42P6DCiDin2a8jJxaoEVx2MgmrEnSeA5bKeTLoDmHxXUt2jZ%2BhBQCMGQkjdzViPPLGkVZMOW9sAf64Z2b%2FwzZKGDoJo5HGEIpzeRMvJXkrqO347NdC9FcEFLFrjfxL2mM1bZJsFmHmEOfgsRHc7OtkgIhmFkeX7dgx8%2F4O8%2Bg8Ikm4%2B8rWsQjLIv1N7QI1UwmNBaqSKB8x9TF7yrBOy80XElPEVZYvuEuu6UXTUBODs2t0Uqhz0DKR071bBLHTvmTcUqQPSITIsNsrJ1CKijaWmsiHvU5gGLCiKUBBYjfymqOVfDhWK6qGzsQvom3IT%2FXXklWm0jHapKMmCuV9OefxooeJx710snmlinOqP2TA3ONq%2F28o6yaai%2BdWt3OXm9rUIcIQJvzKTB8sJj9FsdTxZe9BfPVqyPAmMuKp0Tv%2BR45VDEc8xVdst39Ti3XVELJTqAemz%2BjyUOP0tlgrgK%2FWZvEkCg4WJ1MhGAKPqeW%2BASdmPrZPrTHwD8z8TVnTEXp90JMRaxalIT20g%2Fid0JQT1vW%2FJFWoCLiBiDyqsDHxyrp%2BliZWITZlXopg4UYiPO3qesOPglld2xR7Iip0dt22zXuT7TZYK6OhqrXp%2BxA8rzFyAib6dVsukbQJWbBvSQ7E%2BDT8gD0iwPT8etyxMZ2b4m%2FbY9ddX7QytJYo8w4GJfm5RMADxHSDukk3OXoqSeme%2F7SpWA8yE66E8lAGJpqaAF6e0b4n%2BLCVECA8WJNYy8%2BHjhFnNZd05Dz8oq3u3u5BKZyuj0hK267INay7NhzenUI6qWu4B4uCNFt05RmU4jL%2FqHNvS2C4pMF8QsGR%2BllVK2fjOy3DKBzQ3x41h9brypc8wBSflnhDJNe9PfT9LHGKG0ynwN3K6LRNYN%2FM38uHZcV7a0vBXvSf1okUyHQx3yscZr0K95PRzWoU60i7eXc1B7lTAQz5HlAVyTZbj1cPWU%2FtJo12VErnhWGJwCHg%3D%3D--Hd3gVYRjdq4a23qR--f238jGM%2B%2BoGQg%2FKBas%2Bf%2FQ%3D%3D'

jar = requests.cookies.RequestsCookieJar()

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

}

for cookie in cookies:
   key, value = cookies.split('=',1)
   print("key, value", (key,value))
   jar.set(key,value)
   print('jar:', jar)
r = requests.get(url, cookies=jar, headers=headers)
print(r.text)
"""

# Example 10 Session 维持
"""
url = 'http://httpbin.org/cookies'

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')

r = s.get(url)

print(r.text)
"""

# Example 11 证书验证 Verify 参数控制是否验证证书
"""
url = 'https://static2.scrape.cuiqingcai.com/'

response = requests.get(url, verify=False)
print(response.status_code) # 忽略了证书不过返回了一个警告，建议我们给它指定证书
"""

# Example 12 完全忽略证书验证 method 1 忽略警告的方法来忽略警告
"""
from requests.packages import urllib3

urllib3.disable_warnings()

url = 'https://static2.scrape.cuiqingcai.com/'

response = requests.get(url, verify=False)
print(response.status_code)
"""

# Example 12 完全忽略证书验证 method 2 捕获警告到日志的方式忽略警告
"""
import logging

logging.captureWarnings(True)

url = 'https://static2.scrape.cuiqingcai.com/'

response = requests.get(url, verify=False)
print(response.status_code)
"""

# Example 13 超时设置
"""
url = 'https://httpbin.org/get'

response1 = requests.get(url, timeout=1) #timeout 单位是秒，connect + read的总时间
response2 = requests.get(url, timeout=(5,5)) #分别指定connect的timeout秒数和read的timeout秒数
response3 = requests.get(url, timeout=None) #永久等待，设置参数为None 或者不加参数
print(response3.status_code)
"""

# Example 14 身份认证 Http Basic Access Authentication, 使用requests自带的身份认证功能，通过auth 参数即可设置
"""
from requests.auth import HTTPBasicAuth

url = "https://static3.scrape.cuiqingcai.com/"

r = requests.get(url, auth=HTTPBasicAuth('admin', 'admin'))
print(r.status_code)
"""

# Example 15 代理设置 某些网站在测试的时候请求几次，能正常获取内容。但是对于大规模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，更甚者可能会直接封禁客户端的IP，导致一定时间段内无法访问。为了防止这种情况发生，我们需要设置代理来解决这个问题，这就需要用到 proxies 参数。可以用这样的方式设置：
"""
url = 'https://httpbin.org/get'

proxies = {
   'http': 'http://10.10.10.10:1080',
   'https': 'http://10.10.10.10:1080',
}

r = requests.get(url, proxies=proxies)
print(r.status_code)
# 当然，直接运行这个实例或许行不通，因为这个代理可能是无效的，可以直接搜索寻找有效的代理并替换试验一下。若代理需要使用上文所述的身份认证，可以使用类似 http://user:password@host:port
# 这样的语法来设置代理，示例如下：
proxies2 = {
   'http': 'http://user:password@http://10.10.10.10:1080/',
}
r2 = requests.get(url,proxies=proxies2)

#Socks 协议的代理
proxies3 = {
   'http': 'socks5://user:password@host:port',
   'https': 'socks5://user:password@host:port'
}
r3 = requests.get(url,proxies=proxies3)
print(r3.text)
"""

# Example 16 Prepared Request 不用request方法，直接构造一个Prepared Request 对象
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
   'name': 'germey',
}
headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/80.0.3987.132 Safari/537.36',
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)

# 有了 Request 这个对象，就可以将请求当作独立的对象来看待，这样在一些场景中我们可以直接操作这个 Request 对象，更灵活地实现请求的调度和各种操作。
