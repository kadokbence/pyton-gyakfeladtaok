#feladat : Mennyi 2000 alati 3-al oszthato szam van a sorozatban?
#A[i] < 2000 and A[i] % 3 == 0
lista = [2,2,2,2,2,2,4,3,24,6,7,]
def KicsiharmadDarab(A):
    N = len(A)
    db = 0
    for i in range(0,N,1):
        if A[i] < 2000 and A[i]%3 == 0:
            db+=1
    return db
print(f"A sorozatban{KicsiharmadDarab(lista)}")
 