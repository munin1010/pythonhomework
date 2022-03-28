# 作業一 用第4個檔案+串列做
"""
由使用者輸入上面其中一個地區,程式要印出該區的所有站名sarea(中文場站區域)可借sbi(可借車位數),可停bemp(可還空位數)的資料
"""
import requests #上網用的
import json   #解析Json用的
url="https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=700"

bike=requests.get(url).text
data=json.loads(bike)
#area=list() 串列版2

area={} #把字典的資料用串列增加     
for row in data:
     if not row["sarea"] in area:
        area[row["sarea"]]=[] 
        #     key        空串列       
     area[row["sarea"]].append(row["sarea"]) 
     if not row["sbi"] in area[row["sarea"]]:  
         area[row["sarea"]].append(row["sbi"]) 
     if not row["bemp"] in area[row["sarea"]]:  
         area[row["sarea"]].append(row["bemp"])     
           
   
print(area.keys())  #把所有的key列出來   
name=input("請輸入查詢區域:") 
if name in area:
    print(area[name])










