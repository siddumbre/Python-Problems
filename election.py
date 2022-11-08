n=int(input())
que=input()
q=list(que)
n=len(q)
la=[]
lb=[]
l=[]
a=0
b=0
if q[0]=='-' and q[1]=='A':
    q[0]='A'
if q[len(q)-1]=='-' and q[len(q)-2]=='B':
    q[len(q)-1]='B'
for i in range(n):
    if q[i]=='-':
        l.append(i)
for i in range(n):
    for j in range(1,n-1):
        if j in l:
            if q[j+1]=='A':
                q[j]='A'
            if q[j-1]=='B':
                q[j]='B'
            if q[j+1]=='A' and q[j-1]=='B':
                q[j]='-'
if q[0]=='-' and q[1]=='A':
    q[0]='A'
if q[len(q)-1]=='-' and q[len(q)-2]=='B':
    q[len(q)-1]='B'
for el in q:
    if el=='A':
        a+=1
    if el=='B':
        b+=1
print(q)
if a>b:
    print('A')
if a<b:
    print("B")
if a==b:
    print("Coalition government")
        
        