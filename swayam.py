if __name__=='__main__':
  n=int(input())
  b=input()
  l=b.split(' ')
  bro=l[0]
  gro=l[1]
  br=list(bro)
  gr=list(gro)
  o=0
  for i in range(len(br)+1):
    if len(br)>0:
      if br[0]==gr[0]:
        #print(br[0],'marries',gr[0])
        br.remove(br[0])
        gr.remove(gr[0])
        o+=1
      else:
        for k in gr:
          temp=gr[0]
          for j in range(len(gr)-1):
            gr[j]=gr[j+1]
          gr[len(gr)-1]=temp
          #print("After rotation:",gr)
          if br[0]==gr[0]:
            #print(br[0],"Marries",gr[0])
            br.remove(br[0])
            gr.remove(gr[0])
            o+=1
  print(n-o)