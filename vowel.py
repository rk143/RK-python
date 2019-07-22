l= input()
if (l=='A' or l=='a' or l=='E' or l=='e' or l=='I'
 or l=='i' or l=='O' or l=='o' or l=='U' or l=='u'):
    print("Vowel") 
elif ((l>='a' and l<='z') or (l>='A' and l<='Z')):
     print("Consonant")
else:
    print("invalid")
