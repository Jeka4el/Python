print("********")

for x in range(0,10 +1):
    print("********")
    print("________")
    print(x)

for x in range(0,10, 2): # 2 это шаг выведет только четные
    print(x)

for x in range(1,20):
    print("Number x =" + str(x)) # если строка и число, число нуцжно превратить с строку str.

for x in range(0, 20):
    print("nunmber x= " + str(x))
    if x ==15:
        break

while True:
    print(x)
    x = x+1
    if x == 100:
        break