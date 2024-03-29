def temp ():
    t=int(input("entrer le temps a convertir:"))
    h=t//3600
    secondes_restant=h %3600
    m=secondes_restant //60
    s=secondes_restant %60
    print("T="+str(h)+":"+str(m)+":"+str(s))
temp()