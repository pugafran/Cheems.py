import datetime, random

print(datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day).strftime("%a"))

print(datetime.datetime.now().hour == 14)

suma = 0

for i in range (100):
    print(str(random.randint(0,10)) + "\n")
    suma += random.randint(0,10)

print(suma)

