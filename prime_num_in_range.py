r,k=map(int,input().split())  
for s in range(r+1,k):  
   if s>1:  
       for i in range(2,s):  
           if (s%i) == 0:  
               break  
       else:  
          print (s,"",end="")
