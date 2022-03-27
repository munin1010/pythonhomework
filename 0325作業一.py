# 作業一
"""
由系統自動產生6個不重複的數字 (1~100)  random
由使用者自行輸入6個號碼   list(input("請輸入號碼:"))
先列出系統的6個號碼，再列出使用者中了幾個  if的index和count
中2個獲得10個蘋果
中3個獲得20個蘋果
中4個獲得30個蘋果
中5個獲得40個蘋果
中6個獲得50個蘋果
"""
import random
number=[]
num=[]
Count=0
for x in range(6):
    n=random.randint(1,100) 
    number.append(n)
    guess=int(input("請輸入號碼:"))
    num.append(guess)
    if number[x]==num[x]:
        Count+=1
if Count ==2:
   print(number)
   print("中2個獲得10個蘋果")
elif Count ==3:
    print(number)
    print("中3個獲得20個蘋果")
elif Count ==4:
    print(number)
    print("中4個獲得30個蘋果")
elif Count ==5:
    print(number)
    print("中5個獲得40個蘋果")
elif Count ==6:
    print(number)
    print("中6個獲得50個蘋果")
else:
    print("請下次再來")
        
        
    
        
    
    
    
    
    
    
