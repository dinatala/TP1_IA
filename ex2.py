import math
def equation(a,b,c):
    des=b*b-4*a*c
    if des>0 :
      x1=(-b-math.sqrt(des))/2*a
      x2=(-b+math.sqrt(des))/2*a
      print(x1,x2) 
    elif des==0:
        x=-b/2*a 
        print(x) 
    else:
        print("the function have no solution")
 
equation(6,4,2)