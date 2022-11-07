name = input("Please ented your name: ")
print (name)

num1 = input("Enter X: ")
num2 = input("Enter Y: ")
summa = int(num1) + int(num2)
print(summa)

message = ""
while True:
    message = input("Enter Password : ")
    if message == 'pas':
        break
    print("Password not correct")


mylist = []
msg = ""
while msg != 'stop'.upper():
    msg = input("Enter new item, end STOP to finish ")
    mylist.append(msg)
print(mylist)