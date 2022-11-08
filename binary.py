def decimalToBinary(n):  
    return bin(n).replace("0b", "") 
n=int(input())
num=list(map(int,input().split(' ')))
na=max(num)
zeros=[]
ones=[]
oppo=0
count=0
for nom in num:
    no=decimalToBinary(nom)
    #print(no)
    l=list(no)
    if len(l)>oppo:
        oppa=len(l)
    #print(l)
    z=0
    one=0
    for i in range(len(l)):
        if l[i]=='1':
            one+=1
        z=len(l)-one     
    if one==z:
        count+=1
    zeros.append(z)
    ones.append(one)
tempo=0
tempz=0
for i in range(len(ones)-1):
    if ones[i]+ones[i+1]==zeros[i]+zeros[i+1]:
        tempz=zeros[i]+zeros[i+1]
        tempo=ones[i]+ones[i+1]
        count+=1
    if ones[i]+tempo==zeros[i]+tempz and tempo>0:
        count+=1
print(count)