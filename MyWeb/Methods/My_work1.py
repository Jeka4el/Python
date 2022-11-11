from urllib import request

myUrl = "http://jeka4el.od.ua"

otvet = request.urlopen(myUrl)
mytext1 = otvet.readlines()
mytext2 = otvet.read()

print(otvet)
print("====================")
print(mytext1)
print("====================")
for otv in mytext1:
    print(otv)
