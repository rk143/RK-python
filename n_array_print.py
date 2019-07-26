r=int(input())
p =list(map(int,input().strip().split()))[:r] 
for i in range(len(p)): 
    print (p[i],end = " ") 
    print (i)
