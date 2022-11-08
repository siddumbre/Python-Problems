cost=list(map(int,input().split(' ')))
Max_a=list(map(int,input().split(' ')))
H=list(map(int,input().split(' ')))
C=list(map(int,input().split(' ')))
Aq=list(map(int,input().split(' ')))
Total=int(input())
M=max(cost)
a=[]
ele=[]
temp=[]
Mi=min(cost)
a.append(H[0]*H[1])
a.append(C[0]*C[1])
a.append(Aq[0]*Aq[1])
temp=[-1,-1,-1]
for i in range(len(cost)):
    if cost[i]==M and Mi!=M:
        arr=a[i]
        temp[i]=i
        ele.append(arr*cost[temp[i]])
    if cost[i]==Mi and Mi!=M:
        arp=Max_a[i]
        temp[i]=i
        ele.append(arp*cost[temp[i]])
for j in range(3):
    if j not in temp:
        arz=Total-arr
        arz-=arp
        print("aa",arp,arr,Total,Total-arr-arp)
        temp[j]=j
        ele.append(arz*cost[temp[j]])
        print(arz,j)
print(ele)
