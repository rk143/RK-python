r,k=map(int,input().split())  
for n in range(r,k):
   s=0
   a=n
   while a>0:
       d= a%10
       s+=d**3
       a//=10
 
   if n==s:
       print(n,"",end="")
