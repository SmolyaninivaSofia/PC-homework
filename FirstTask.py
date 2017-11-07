import pandas as pd
import cmath

data_file='D:\\data.csv'
context_file='D:\\context.csv'
curr_user=36 #мой номер пользователя нумеруются с 0
sim = {}     #похожесть
res={}       #результат
users=pd.read_csv(data_file,encoding='latin1',index_col='Users') #таблица
user32=users.iloc[curr_user]
k=5

def metrics(user1, user2): #метрика схожести
    uv = 0
    u = 0
    v = 0
    for i in range(0, len(user1)):
        if user1[i]!=-1 and user2[i]!=-1:
            uv += user1[i] * user2[i]
            u += pow(user1[i],2)
            v += pow(user2[i],2)
    return uv / (cmath.sqrt(u) * cmath.sqrt(v))

def avg_value(user): #средняя оценка пользователя
    sum=0
    cnt=0
    for i in range(0, len(user)):
        if user[i]!=-1:
            sum += user[i]
            cnt+=1
    return sum/cnt

def stars(f): #предполагаемая оценка
    res=0
    ru=avg_value(user32)
    simsum=0
    top_users =sim.keys()
    for key in top_users:
        rvi=(users.iloc[key])[f]
        if rvi!=-1:
            rv=avg_value(users.iloc[key])
            res+=sim[key]*(rvi-rv)
            simsum+=abs(sim[key])
    return (ru+res/simsum).real #подсчет оценки

for u in range(0,len(users)):
    if u!=curr_user:
        sim[u]=metrics(users.iloc[u], user32)
sim=dict(sorted(sim.items(), key=lambda x: x[1], reverse=True)[:k]) # 5 похожих
for i in range(0,len(user32)):
    if user32[i]==-1:
        res[i+1]=stars(i)
for h in res:
    print('Movie',h,':',round(res[h],3))
