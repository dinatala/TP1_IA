def div():
    np=int(input("entrer un entier positive:"))
    s=0
    for i in range(1,np):
        r=np%i
        if r==0:
           s+=i
    
    if s==np:
        print("le nombre est parfait")
    else:
        print("le nombre n'est pas parfait")    
div()       