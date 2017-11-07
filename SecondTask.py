import pandas as pd
import cmath

data_file='D:\\data.csv'
context_file='D:\\context.csv'
curr_user=31 #мой номер пользователя -1
sim = {}     #похожесть
res = {}     #результат
films=[]     #фильмы для рекомендаций
users=pd.read_csv(data_file,encoding='latin1',index_col='Users') #таблица
context=pd.read_csv(context_file,encoding='latin1',index_col='Users')
user32=users.iloc[curr_user]

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
    r=(ru+res/simsum).real
    return r

for fil in range (0,30): # фильмы для рекомендации
    if user32[fil]==-1:
        films.append(fil)

for u in range(0,len(users)): # Заполнение данных для будних дней
    for f in range (0,30):
        cont_f= (context.iloc[u])[f]
        if (cont_f==' Sun' or cont_f==' Sut'):
            (users.iloc[u])[f]=-1

for u in range(0,len(users)): # расчет схожести пользователей в будний день
    if u!=curr_user:
        sim[u]=metrics(users.iloc[u], user32).real
sim=dict(sorted(sim.items(), key=lambda x: x[1], reverse=True)[:5]) # 5 похожих

for i in films: # расчет оценок и выбор лучшего фильма
    res[i+1]=stars(i)
res=dict(sorted(res.items(), key=lambda x: x[1], reverse=True)[:1])
for h in res:
    print('Movie',h,':',round(res[h],3))