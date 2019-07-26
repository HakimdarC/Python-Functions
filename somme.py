def somme(n):
    somme=0
    for i in range(0,n+1):
        somme+=i
    return somme
d=input("donner la val de n: ")
print("la somme de 0 a {} est {}:".format(int(d),somme(int(d))))
