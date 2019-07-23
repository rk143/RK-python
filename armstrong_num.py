num=int(input())  
s=0  
r=num
while r>0:  
       d=r%10  
       s+=d**3  
       r//=10        
if num==s:
  print("yes")  
else:  
  print("no")
