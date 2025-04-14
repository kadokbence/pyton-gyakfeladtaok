
import random
def otos():
    nysz = []
    for i in range(1,8):
        szam = random.randint(1,91)
        if not nysz.__contains__(szam):
            nysz.append(szam)
    print(nysz)
    
#Lotto sorsolás kérjuk meg a felhasználot hogy melyik lottot szeretne jatszani?
#5os 6os skandináv
#szabályok:
#5os : 90böl 5ot
#6os : 45böl 6ot
#skandi : 35böl 7et (2x húzzák ki a nyereményt)
nyeremeny =[]
tipus = input("melyikel szeretnél játszani?\n ötös lottó \n 6-os lottó \n skandi\n")
match tipus:
    case '5' :
        otos()
    case '6':
        hatos()
    case 'S':
        skandi()    