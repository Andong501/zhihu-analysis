#!/urs/bin/evn python
# -*- coding:utf-8 -*-

import threading
import Login
import DB
import Queue
import Myjson
from time import sleep
import random
from random import choice
from requests.exceptions import ConnectionError


def search(ss,tk,dp,q): #from tk to tks
    session = ss
    pg = 0
    is_end = False
    sec_url1 = 'https://www.zhihu.com/api/v4/members/'
    sec_url2 = '/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset='
    sec_url3 = '&limit=10'
    sec_url4 = 'https://www.zhihu.com/api/v4/members/'
    sec_url5 = '?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cmarked_answers_count%2Cmarked_answers_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_force_renamed%2Cis_bind_sina%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
    while is_end == False:
        try:
            json_url1 = sec_url1+tk+sec_url2+str(pg*10)+sec_url3
            getJson1 = session.get(json_url1).content
            getDict1 = Myjson.json_loads_byteified(getJson1)
            print getDict1.get('data')
            sleep(random.uniform(1,1.5))
            for d in getDict1.get('data'):
                try:
                    s = d['url_token']
                    if users.find_one({'token':s}) is None: #has this user already in db?
                        json_url2 = sec_url4+s+sec_url5
                        getJson2 = session.get(json_url2).content
                        getDict2 = Myjson.json_loads_byteified(getJson2)
                        nm,sx,ed,ct,fd,cp,jb,fe,fi,vu,tn,fv,an,ar,qs = DB.data_model(getDict2)
                        DB.save_data(users,dp,s,nm,sx,ed,ct,fd,cp,jb,fe,fi,vu,tn,fv,an,ar,qs)
                        q.put(s)
                    else:pass
                    sleep(random.uniform(1,1.5)) #slow down
                except ConnectionError:
                    continue
            is_end = getDict1.get('paging').get('is_end')
            pg += 1
        except ConnectionError:
            continue
    return q

def spider(ss,init_token,usr):
    depth = 0
    q = Queue.Queue()
    if users.find_one({'token':init_token}) is None:
        DB.save_data(users,depth,init_token,usr,sx=None,ed=None,ct=None,fd=None,cp=None,jb=None,fe=0,fi=0,vu=0,tn=0,fv=0,an=0,ar=0,qs=0)
        q.put(init_token)
    while not(depth==10):
        depth +=1
        list=[]
        len = q.qsize()
        for i in range(0,len):
            list.append(q.get())
        print list
        for token in list:
            q = search(ss,token,depth,q)
            sleep(random.uniform(0.5,1))
    return

if __name__ == '__main__':

    users = DB.start_db()

    act1 = raw_input('account:') #input your account
    pw1 = raw_input('password:') #input your passord
    usr1 = raw_input('username:') #input your username
    url_token1 = raw_input('url_token:') #input your zhihu token

    act2 = raw_input('account:') 
    pw2 = raw_input('password:') 
    usr2 = raw_input('username:') 
    url_token2 = raw_input('url_token:') 

    act3 = raw_input('account:') 
    pw3 = raw_input('password:') 
    usr3 = raw_input('username:') 
    url_token3 = raw_input('url_token:') 

    act4 = raw_input('account:') 
    pw4 = raw_input('password:') 
    usr4 = raw_input('username:') 
    url_token4 = raw_input('url_token:') 

    session1 = Login.login_e(act1,pw1,Login.see_captcha) #get a session with logining my initial account
    session2 = Login.login_e(act2,pw2,Login.see_captcha)
    session3 = Login.login_p(act3,pw3,Login.see_captcha)
    session4 = Login.login_e(act4,pw4,Login.see_captcha)
    
    t1 = threading.Thread(target=spider,args=(session1,url_token1,usr1)) #set 4 threads
    t2 = threading.Thread(target=spider,args=(session2,url_token2,usr2))
    t3 = threading.Thread(target=spider,args=(session3,url_token3,usr3))
    t4 = threading.Thread(target=spider,args=(session4,url_token4,usr4))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
