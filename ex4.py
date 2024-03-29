
def impot():
    a = int(input("Entrer votre age: "))
    s = input("Entrer votre sexe: ")

    if a > 20 and s == "h":
        print("Paient impot")
    elif a >= 18 and a <= 35 and s == "f":
        print("Paient impot")
    else:
        print("Ne pas payer")

impot() 