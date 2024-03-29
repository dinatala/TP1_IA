import math
def polynome():
 n=int(input("entrer un entier:"))
 s=0
 i=0
 while i<n:
  s+=10**i  #same as:s+=pow(10,i)
  i+=1
 print("le resultat:",s) 
polynome()  