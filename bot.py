import requests 
import re 
import threading    
q=[0 for i in range(30)]    
res1=[] 
gg=list()
def ssilki(pot,url):        
    headers={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
    }
    global q    
    global res1     
    r=requests.get(url,headers=headers).text    
    while len(res1)<100:
        res2=re.findall(r'({"webCommandMetadata":{"url":"/.{,500}"webPageType":"WEB_PAGE_TYPE_WATCH"}})',r)   
        res2=[re.findall(r'/watch.{1,300}",',res2[i]) for i in range(len(res2))]    
        res1+=[res2[i][0][:-2] for i in range(len(res2))]   
        r=requests.get('https://www.youtube.com'+res1[len(res1)-pot-1],headers=headers).text   
    del q[len(q)-1] 
t=[[] for i in range(30)]
g=0

def prn():
    global gg
    a=open('C:\\Users\\В\\Desktop\\worck\\Ворона\\baza.txt','w',encoding="utf-8")
    for i in gg:
        a.write(i+'\n')
    a.close()

def sort():
    for i in res1:
        if 'https://www.youtube.com'+i not in gg:
            gg.append('https://www.youtube.com'+i)

def Main():
    global q  
    url=input("Введите начальную ссылку: ")  
    for i in range(30): 
        threading.Thread(target=ssilki,args=(i,url)).start()    
    d=True  
    while d:   
        if len(q)<1:  
            sort()
            prn()
            d=False

Main()