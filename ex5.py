def operation():
    oprt1=int(input("entrer operateur 1:"))
    oprt2=int(input("entrer operateur 2:"))     
    op=input("entrer l'operateur convenable +,-,*,/:")
    if op== "*":
        r=oprt1*oprt2
        print("le resultat est",r)
    elif op== "+":
        r=oprt1+oprt2
        print("le resultat est",r)
    elif op== "-":
        r=oprt1-oprt2
        print("le resultat est",r)
    else:
        r=oprt1/oprt2
        print("le resultat est",r)

operation()