#coding:utf-8  

import matplotlib 
import matplotlib.pyplot as plt 
%matplotlib inline
import seaborn as sns
import numpy as np
import pandas as pd
from __future__ import division #精确除法

matplotlib.rcParams['axes.unicode_minus']=False; #解决负号'-'显示为方块的问题

#Copy sulian

df = pd.read_csv('zhihu_data_v1.0.csv');
df = df.drop(['favourite', 'education'], axis=1);

#Basic statistics
#total users
user_num = df.sex.value_counts().sum();
#total questuons
ques_num = df.question.sum();
#total answers
ans_num = df.answer.sum();
#total articles
arc_num = df.article.sum();
#total votes
vote_num = df.vote.sum();
#total followers
fe_num = df.follower.sum();
#summary
dict1 = {'Users':user_num, 'Questions':ques_num, 'Answers':ans_num, 'Articles':arc_num, 'Votes':vote_num, 'Followers':fe_num};
s = pd.Series(dict1);
s.to_csv('basic statistics.csv');

#回答、赞成、关注分布情况
a1 = df.sex[(df.answer==0) & (df.follower==0)].value_counts().sum();
a2 = df.sex[(df.answer==0) & (df.follower!=0)].value_counts().sum();
a3 = df.sex[(df.answer!=0) & (df.vote==0) & (df.follower==0)].value_counts().sum();
a4 = df.sex[(df.answer!=0) & (df.vote==0) & (df.follower!=0)].value_counts().sum();
a5 = df.sex[(df.answer!=0) & (df.vote!=0) & (df.follower==0)].value_counts().sum();
a6 = df.sex[(df.answer!=0) & (df.vote!=0) & (df.follower!=0)].value_counts().sum();
#summary
array1 = np.array([a1, a2, a3, a4, a5, a6]);
array2 = array1/user_num;
array2 = np.array(['{:.2%}'.format(x) for x in array2]); #小数转换为百分数
dict2 = {'Users':array1, 'Percentage':array2};
indx = ['No answers & No followers', 'No answers & Has followers', 'Has answers & No votes & No followers', 'Has answers & Has votes & No followers', 'Has answers & No votes & Has followers', 'Has answers & Has votes & Has followers'];
d1 = pd.DataFrame(dict2, index=indx);
d1.to_csv('ans_vote_fe.csv');
#plot
sizes = dict2['Users'];
labels = indx;
colors = [sns.xkcd_rgb["pale red"], sns.xkcd_rgb["amber"], sns.xkcd_rgb["greyish"], sns.xkcd_rgb["windows blue"], sns.xkcd_rgb["faded green"], sns.xkcd_rgb["dusty purple"]];
#labels = [unicode(x, 'utf-8') for x in indx]; #utf-8转换为unicode
explode = (0, 0, 0, 0, 0, 0.1);
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90);
plt.axis('equal');

#得赞数分布情况
b1 = df.token[df.vote==0].value_counts().sum();  #0
b2 = df.token[(df.vote>0) & (df.vote<100)].value_counts().sum();  #1-99
b3 = df.token[(df.vote>=100) & (df.vote<1000)].value_counts().sum(); #100-999
b4 = df.token[(df.vote>=1000) & (df.vote<10000)].value_counts().sum(); #1000-9999
b5 = df.token[(df.vote>=10000) & (df.vote<100000)].value_counts().sum(); #10000-99999
b6 = df.token[df.vote>99999].value_counts().sum(); #100000+
#summary
array3 = np.array([b1, b2, b3, b4, b5, b6]);
array4 = array3/user_num;
array4 = np.array(['{:.2%}'.format(x) for x in array4]);
dict3  = {'Users':array3, 'percentage':array4};
indx = ['0', '1-99', '100-999', '1000-9999', '10000-99999', '100000+'];
d2 = pd.DataFrame(dict3, index=indx);
d2.to_csv('ans_num.csv');
#plot
sizes = dict3['Users'];
labels = indx;
colors = [sns.xkcd_rgb["red"], sns.xkcd_rgb["orangered"], sns.xkcd_rgb["orange"], sns.xkcd_rgb["sunflower"], sns.xkcd_rgb["dandelion"], sns.xkcd_rgb["sunny yellow"]];
explode = (0.1, 0, 0, 0, 0, 0);
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90);
plt.axis('equal');

#被关注数分布
c1 = df.sex[df.follower==0].value_counts().sum();
c2 = df.sex[(df.follower>0) & (df.follower<100)].value_counts().sum();
c3 = df.sex[(df.follower>=100) & (df.follower<1000)].value_counts().sum();
c4 = df.sex[(df.follower>=1000) & (df.follower<10000)].value_counts().sum();
c5 = df.sex[(df.follower>=10000) & (df.follower<100000)].value_counts().sum();
c6 = df.sex[(df.follower>99999)].value_counts().sum();
#summary
array5 = np.array([c1, c2, c3, c4, c5, c6]);
array6 = array5/user_num;
array6 = np.array(['{:.2%}'.format(x) for x in array6]);
dict4  = {'Users':array5, 'Percentage':array6};
indx = ['0', '1-99', '100-999', '1000-9999', '10000-99999', '100000+'];
d3 = pd.DataFrame(dict4, index=indx);
d3.to_csv('follower_num.csv');
#plot
sizes = dict4['Users'];
labals = ['0', '1-99', '100-999', '1000-9999', '10000-99999\n', '100000+\n'];
colors = [sns.xkcd_rgb["navy blue"], sns.xkcd_rgb["royal blue"], sns.xkcd_rgb["bright blue"], sns.xkcd_rgb["azure"], sns.xkcd_rgb["dark sky blue"], sns.xkcd_rgb["light aqua"]];
explode = (0, 0.07, 0, 0, 0, 0);
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90);
plt.axis('equal');

#性别统计
sns.set_style(style='darkgrid');
g1 = sns.countplot(x='sex', data=df, palette='Greens_d'); #一个Axes实例
g1.set_xticklabels(['Uknown', 'Female', 'Male']);
g1.set_title('Number of users by gender');
g1.set_xlabel('gender');

#变量的关联性探索
#回答数与得赞数
g2 = sns.regplot(x='answer', y='vote', data=df);
g2.set_yscale('log');
g2.set_xlim(0, 20000);
g2.set_ylim(1,10000000);
g3 = sns.lmplot(x='answer', y='vote', hue='sex', data=df);
g3.fig.get_axes()[0].set_yscale('log');
g3.fig.get_axes()[0].set_xlim(0, 20000);
g3.fig.get_axes()[0].set_ylim(1,10000000);
g4 = sns.lmplot(x='sex', y='vote', data=df);

#得赞数与被关注数
g5 = sns.regplot(x='vote', y='follower', data=df);
g5.set_yscale('log');
g5.set_xlim(0, 20000);
g5.set_ylim(1,10000000);
g6 = sns.lmplot(x='vote', y='follower', hue='sex', data=df);
g6.fig.get_axes()[0].set_yscale('log');
g6.fig.get_axes()[0].set_xlim(0, 20000);
g6.fig.get_axes()[0].set_ylim(1,10000000);
g7 = sns.lmplot(x='sex', y='follower', data=df);

#得赞数直方图
g8 = sns.distplot(df.vote, bins=100, kde=False);
g8.set_yscale('log');
#被关注数直方图
g9 = sns.distplot(df.follower, bins=100, kde=False);
g9.set_yscale('log');

#特殊点处理
sp1 = df.loc[df['vote'].idxmax()];
sp2 = df.loc[df['follower'].idxmax()];
sp3 = df.loc[(df['question'] / df['answer']).idxmax()];
sp4 = df.loc[(df['answer'] / df['question']).idxmax()];
sp5 = df.loc[(df['follower'] / df['following']).idxmax()];
sp6 = df.loc[(df['following'] / df['follower']).idxmax()];

