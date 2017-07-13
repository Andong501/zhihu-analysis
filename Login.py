#!/urs/bin/evn python
# -*- coding:utf-8 -*-

from random import choice
import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
           'Proxy-Authorization': 'Basic SE83MTA2UzAxODFOMTJLRDpBN0VCQzIxRjlGMkNBQ0RG'
    }

def see_captcha(data):
    with open('captcha.png','wb') as f:
        f.write(data)
    return raw_input('captcha:')

def login_e(account,password,oncaptcha):
    session = requests.session()
    session.headers.update(headers) #add ua
    _xsrf = BeautifulSoup(session.get('https://www.zhihu.com/#signin').content,'lxml').find('input', attrs={'name': '_xsrf'})['value']
    captcha_content = session.get('https://www.zhihu.com/captcha.gif?r=%d&type=login' %(time.time()*1000)).content
    data ={
        '_xsrf':_xsrf,
        'email':account,
        'password':password,
        'captcha':oncaptcha(captcha_content)
    }
    resp = session.post('https://www.zhihu.com/login/email',data=data).content
    print resp
    assert '\u767b\u5f55\u6210\u529f' in resp
    return session

def login_p(account,password,oncaptcha):
    session = requests.session()
    session.headers.update(headers) #add ua
    _xsrf = BeautifulSoup(session.get('https://www.zhihu.com/#signin').content,'lxml').find('input', attrs={'name': '_xsrf'})['value']
    captcha_content = session.get('https://www.zhihu.com/captcha.gif?r=%d&type=login' %(time.time()*1000)).content
    data ={
        '_xsrf':_xsrf,
        'phone_num':account,
        'password':password,
        'captcha':oncaptcha(captcha_content)
    }
    resp = session.post('https://www.zhihu.com/login/phone_num',data=data).content
    print resp
    assert '\u767b\u5f55\u6210\u529f' in resp
    return session
