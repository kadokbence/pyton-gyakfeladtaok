#feladat 1
def Koszones():
    #pass
    print("Hello szia szeva")
#Fügveény definicio
def Összead(a,b):
    Összeg=a+b
    return Összeg
#1. tétel összegzés(sorozatszámitás) tételét
#Hivás:
print("Itt koszonok: ")
Koszones()
oszz = Összead(3,5)
print(oszz)
print(Összead(4,8),Összead(6,9),Összead(12,65)/2)
Koszones()
#100 elemű lista 1000 és 5000 közti számokat teszünk
import random
lista=[]
for i in range(100):
    lista.append(random.randint(1000,5001))

print(lista)

#számitsuk ki a sorozat elemeinek átlagát
def osssegzes(A):
    N=len(A)
    szum=0
    for i in range(1,N,1):
        szum+=A[i]
    return szum
print(f"A lista elemeiknek átlaga: {osssegzes(lista)/len(lista)}")

#2. Tétel Maximum tételét
def Maxkiválsztása(A):
    N=len(A)
    maxi = 0
    for i in range(0,N,1):
        if A[maxi]<A[i]:
            maxi = 1 
    return maxi


maxindex = Maxkiválsztása(list)
print(f"A sorozat legnagyobb eleme: {lista[maxindex]}, amely a {maxindex}. helyen van,")