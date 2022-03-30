# 
"""
2/1+3/2+4/3+5/4+6/5+7/6+8/7+....加滿20項求和

2~21
----        
1~20

"""
count=0
for i in range(1,21):
    x=(i+1)/i
    count+=x
print(count)
    