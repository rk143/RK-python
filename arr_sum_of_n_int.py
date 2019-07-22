r,k=map(int,input().split())
p=k
a=0
pd=[]
pd=list(map(int,input().strip().split()))[:r]
for i in range(0,p):
  a=a + pd[i]
print(a)
