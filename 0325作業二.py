# 作業二
"""
data=[99,1,10,6,88,60]
請將data排序由 小到大 或 大到小
並印出排序後結果[1,6,10,60,88,99]、[99,88,60,10,6,1]
用迴圈解

"""
number=[]
LL=[]
data=[99,1,10,6,88,60]
for i in range(6):
    Count=0
    for x in range(6):
        if data[i] >= data[x]:
            Count+=1
    if Count==6:
        number.insert(0, data[i])
    elif Count==5:
        number.insert(1, data[i])
    elif Count==4:
        number.insert(2, data[i])
    elif Count==3:
        number.insert(3, data[i])
    elif Count==2:
        number.insert(4, data[i])
    elif Count==1:
        continue
else:
    number.append(data[1])

           
      
           
           
           
        
             
        

            
            
      
                        
