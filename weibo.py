import requests
try:
    url = 'https://www.weibo.com/a/hot/realtime'

    headers = {
        'cookie': 'Ugrow-G0=5c7144e56a57a456abed1d1511ad79e8; login_sid_t=29d2562ebb4d24e7f9e1a8e3a51c50c2; '
                  'cross_origin_proto=SSL; TC-V5-G0=eb26629f4af10d42f0485dca5a8e5e20; WBStorage=42212210b087ca50|undefined; _s_tentry=-; Apache=4573686274203.705.1584309093358; SINAGLOBAL=4573686274203.705.1584309093358; ULV=1584309094378:1:1:1:4573686274203.705.1584309093358:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whey1pXyv_B.EsML_6KlVfj5JpX5K2hUgL.Foz4S02cSoe41KM2dJLoI7_-IGiaUfSXdc4LM7tt; SSOLoginState=1584309199; ALF=1615845223; SCF=AoXQ7FOjouufQLbeFbcw8ZyLDvEWP7wxYUnlB2Z7lzTBMGU1h-Sj7jEzundQvYJQ-JABrT4sQcMFmQH-bnutWiU.; SUB=_2A25zatO5DeRhGeRH7FMX9i3FwjuIHXVQHkJxrDV8PUNbmtAfLVeskW9NTYdG60nYSpQhQZYkQ1ID2U9hJBhwhQZz; SUHB=079jQ42Sc4_5TU; wb_view_log=1680*10502; un=15683653792; wvr=6',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36',

    }
    res = requests.get(url, headers=headers)
except Exception as e:
    print('Error:', e)
else:
    print('Successfully accessed weibo!')
    
try:
    with open('weibo.html','wb') as f:
       f.write(res.content)
except Exception as e:
    print('Error:', e)
else:
    print('weibo.html saved!')
