#!/urs/bin/evn python
# -*- coding:utf-8 -*-

from pymongo import MongoClient

def start_db():
    client = MongoClient('localhost',27017) #connect to db
    db = client.zhihu #enter database zhihu
    users = db.users #enter collection users
    return users

def data_model(g):
    if g.has_key('name'):
        nm = g['name']
    else:
        nm = None

    if g.has_key('gender'):
        sx = g['gender']
    else:
        sx = -1

    if g.has_key('educations') and g['educations']:
        if g['educations'][0].has_key('school'):
            ed = g['educations'][0]['school']['name']
        else:
            ed = None
    else:
        ed = None

    if g.has_key('locations') and g['locations']:
        if g['locations'][0].has_key('name'):
            ct = g['locations'][0]['name']
        else:
            ct = None
    else:
        ct = None

    if g.has_key('business'):
        if g['business'].has_key('name'):
            fd = g['business']['name']
        else:
            fd = None
    else:
        fd = None

    if g.has_key('employments') and g['employments']:
        if g['employments'][0].has_key('company'):
            cp = g['employments'][0]['company']['name']
        else:
            cp = None
        if g['employments'][0].has_key('job'):
            jb = g['employments'][0]['job']['name']
        else:
            jb = None
    else:
        cp = None
        jb = None

    if g.has_key('follower_count'):
        fe = g['follower_count']
    else:
        fe = 0

    if g.has_key('following_count'):
        fi = g['following_count']
    else:
        fi = 0

    if g.has_key('voteup_count'):
        vu = g['voteup_count']
    else:
        vu = 0

    if g.has_key('thanked_count'):
        tn = g['thanked_count']
    else:
        tn = 0

    if g.has_key('favorited_count'):
        fv = g['favorited_count']
    else:
        fv = 0

    if g.has_key('answer_count'):
        an = g['answer_count']
    else:
        an = 0

    if g.has_key('articles_count'):
        ar = g['articles_count']
    else:
        ar = 0

    if g.has_key('question_count'):
        qs = g['question_count']
    else:
        qs = 0
    return nm,sx,ed,ct,fd,cp,jb,fe,fi,vu,tn,fv,an,ar,qs

def save_data(users,dp,tk,nm,sx,ed,ct,fd,cp,jb,fe,fi,vu,tn,fv,an,ar,qs):
    data ={
        'depth':dp,
        'token':tk,
        'name':nm,
        'sex':sx,
        'educations':ed,
        'city':ct,
        'field':fd,
        'company':cp,
        'job':jb,
        'follower':fe,
        'following':fi,
        'vote':vu,
        'thank':tn,
        'favorite':fv,
        'answer':an,
        'article':ar,
        'question':qs
    }
    users.insert(data) #put one record in db
    return
