# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:28:45 2021

10-dars if else

@author: Eldor


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
for car in cars:
    if car=='gm':
        print(car.upper())
    else:
        print(car.title())
print('==========')
for car in cars:
    if car!='gm':
        print(car.title())
    else:
        print(car.upper())
        
login=input('Login kiriting:')
if login.lower()=='admin':
    print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz {login.title()}!")
    
    
son1=int(input('1-sonni kiriting:'))
son2=int(input('2-sonni kiriting:'))

if son1==son2 :
    print('Sonlar  teng ekan')


son=int(input('Sonni kiriting:'))
if son<0:
    print('Manfiy son')
else:
    print('Musbat son')
    

son=int(input('Sonni kiriting:'))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')
"""