par= 0
impar =0
positivo =0
negativo =0
for c in range (1,6):
    n=int(input(""))
    if n%2==0:
        par+=1
    elif n%2!=0:
        impar+=1
    elif n>0:
        positivo +=1
    elif n<0:
        negativo+=1
print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivo,"valor(es) positivos(s)")
print(negativo,"valor(es) negativos(s)")