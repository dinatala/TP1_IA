def trie():
    a=[1,2,3,4,7,6,5,8,9]
    s=0
    max=0
    for i in a:
        if i>=max:
            max=i
        else:
            s+=1  
    if s==0:
        print("le trie est croissante")
    else: 
        print("le trie n'est pas croissante")         
trie()        