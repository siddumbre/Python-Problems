n=int(input())
Br=list(map(int,input().split(' ')))
B=Br[0]
H=Br[1]
L=list(map(int,input().split(' ')))
l=[]
for i in range(n):
    for j in range(i+1,n+1):
        Len=min(L[i:j])
        Lens=Len*(j-i)
        l.append(Lens)
fin=max(l)
final=fin*B*H
total=sum(L)*H*B
print(total-final)
        