#-*- encoding: utf-8 -*-
'''
Created on 2014年11月7日

@author: liang
'''
from builtins import len

#89861114000203962776
#cardNO_1_org=[8,9,8,6,1,1,1,4,0,0,0,2,0,3,9,6,2,7,7]
cardNO_1_org="439225080413324"

def f(cardNO_1,num):
    print("尝试数：",num,)
    cardNO_1=list(cardNO_1)
    cardNO_1.append(num)
    cardNO_1.reverse()
    print("尝试数：",num,cardNO_1)
    #resvCardNO = cardNO_1[::-1].append(num)
    #print(cardNO_1)
    jiweisum=0
    for i in range(len(cardNO_1)):
        if i%2==0:
            jiweisum+=int(cardNO_1[i])
            #print(cardNO_1[i],jiweisum)
        
    print("奇数和",jiweisum)

    oushsum=0
    for i in range(len(cardNO_1)):
        tmp=0
        if i%2==1:
            tmp=int(cardNO_1[i])*2
            if tmp>10:
                tmp=tmp-9
            
            oushsum+=tmp
    print("偶数和",oushsum)
            

    if (jiweisum+oushsum)%10==0 :
        print(num, "is the key")
        return "ok"
    else:
        print(num, "is not the key")
        cardNO_1.reverse()
        cardNO_1.pop()
        
    




for i in range(10):
    if f(cardNO_1_org,i)=="ok":
        break

    
    