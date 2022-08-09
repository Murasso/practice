import MeCab
import datetime
import noun
import dice
import numpy as np
import pandas as pd
dt_now = datetime.datetime.now()
df = pd.read_csv('data.csv',index_col=['質問'])
# df2=pd.read_csv('data_csv')
QA = dict(zip(df.index, df['答え']))
# print(QA)
Q=input('質問は何ですか？')

# QA={"今日の天気は？":"晴れ",
#     "今の時間は？":dt_now,
#     "君の血液型は?":"B型",
#     "好きな食べ物は?":"カレー",
#     "出身地は":"愛媛"}
Qdict=noun.noundic(QA)
ques=noun.nounQ(Q)
value=[]
valdict={}
for i in Qdict:
    v=dice.dice_similarity_coefficient(ques,i)
    value.append(v)
    valdict[v]=i
df['dice']=value
df_s = df.sort_values('dice', ascending=False)
print(df_s[['答え']][:3])
# print(valdict)







# while node:
#     f=node.feature
#     p=f.split(',')[0]
#     if p=='名詞':
#         print(node.surface)
#     node=node.next