x = 25
if x == 25:
    print("YES you are Right ")
else:
    print("NO you are wrong")


age = 36

if age <=4 :
    print("You are baby")
elif age > 4 and age < 12 :
    print("You are Kid")
elif age > 12 and age < 70:
    print("It's best age")
else:
    print("You are old")


all_cars = ['BMW', 'WV', 'seat','Acura','nissan', 'toyota', 'KIA', 'lexus', 'audi']
if "BMW" in all_cars:
    print("Yes")
else:
    print("NO")


all_cars = ['BMW', 'WV', 'seat','Acura','nissan', 'toyota', 'KIA', 'lexus', 'audi']
german_cars = ['BMW', 'WV','audi']
for xxx in all_cars:
    if xxx in german_cars:
        print(xxx + " Yes")
    else:
        print(xxx + " NO")




