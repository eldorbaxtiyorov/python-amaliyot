# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:07:03 2021

#09-dars

@author: Eldor


#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar=['Asal',"Go'zal",'Sora',"Nora",'Leyla']

for ism in ismlar:
    print('Salom',ism)
    
#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print("Kod",len(ismlar),'marta takrorlandi') 

#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
sonlar=list(range(10,100))

for son in sonlar:
    print(f"{son} ning kubi {son**3} ga teng")
   
kinolar=[]
print('5 ta sevimli kinolaringizni kiriting:')

for n in range(5):
    kinolar.append(input(f"{n+1}-kino nomini kiriting: "))
print(kinolar)

odamlar=[]
n=int(input('Bugun nechta odam bilan uchrashdingiz?\n>>>'))
for n in range(n):
    odamlar.append(input(f"{n+1}-suhbatdosh  nomini kiriting: "))
print(odamlar)
"""

