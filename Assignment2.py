#This codes displays a list of cars you are capable of buying with your money
import numpy as np
car=int(input('Please enter the amount you wish to spend on a car from our store: $'))

print()

if car > 1000000:
    print('You are eligible to purchase a Koenisegg Regara')
elif 900000 <= car < 1000000:
    print('You are eligible to purchase a Pagani Zonda')
elif 800000 <= car < 900000:
    print('You are eligible to purchase a Bugatti Tyron')
elif 700000 <= car < 800000:
    print('You are eligible to purchase a Lamborghini Gallardo')
elif 600000 <= car < 700000:
    print('You are eligible to purchase a Ferrari LaFerrari')
elif 500000 <= car < 600000:
    print('You are eligible to purchase a Rolls Royce')
elif 400000 <= car < 500000:
    print('You are eligible to purchase a Bently Continental GT')
elif 300000 <= car < 400000:
    print('You are eligible to purchase a Lexus CT')
elif 200000 <= car < 300000:
    print('You are eligible to purchase an Audi R8')
elif 150000 <= car < 200000:
    print('You are eligible to purchase a Mercedes Benz S-Class')
elif 100000 <= car < 150000:
    print('You are eligible to purchase a Porsche 911 Turbo')
elif 95000 <= car < 100000:
    print('You are eligible to purchase a BMW A9')
elif 90000 <= car < 95000:
    print('You are eligible to purchase a Chervolet Camaro')
elif 85000 <= car < 90000:
    print('You are eligible to purchase a Land Rover')
elif 80000 <= car < 85000:
    print('You are eligible to purchase a Jaguar E2A')
elif 75000 <= car < 80000:
    print('You are eligible to purchase a Volkswagen Golf 4')
elif 70000 <= car < 75000:
    print('You are eligible to purchase a Honda CR-V')
elif 65000 <= car < 70000:
    print('You are eligible to purchase a Hyundai Veloster')
elif 60000 <= car < 65000:
    print('You are eligible to purchase a Volvo XC60')
elif 55000 <= car < 60000:
    print('You are eligible to purchase a Tesla Cybertruck')
elif 50000 <= car < 55000:
    print('You are eligible to purchase a Toyota Camry')
elif 45000 <= car < 50000:
    print('You are eligible to purchase an Alpha Romeo')
elif 40000 <= car < 45000:
    print('You are eligible to purchase a Subaru Jinx')
elif 35000 <= car < 40000:
    print('You are eligible to purchase a Peugot')
elif 30000 <= car < 35000:
    print('You are eligible to purchase a Mazda')
elif 25000 <= car < 30000:
    print('You are eligible to purchase a Citreon')
elif 20000 <= car < 25000:
    print('You are eligible to purchase a Kantanka')
elif 15000 <= car < 20000:
    print('You are eligible to purchase a Saturn')
elif 15000 <= car < 20000:
    print('You are eligible to purchase a GMC')
elif 15000 <= car < 20000:
    print('You are eligible to purchase a Matiz II')
elif 15000 <= car < 20000:
    print('You are eligible to purchase a Fiat')
else:    print('We are sorry but you cannot afford any car from our store but we sell other car accessories if you are interested')

