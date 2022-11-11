cities = ['New york', 'Odessa', 'Kyiv', 'Toronto']
print(cities)
print(len(cities)) # len посчитает сколько объектов в листе cities - 4
print(cities[1])   # Распечатает Odessa , считает с 0
print(cities[-1])  # Распечатает Toronto , последний Toronto.
print(cities[0].title()) # Распечатает первый New york с большой буквы New York

cities[3] = 'Alikante'
print(cities)

cities.append('Nikolaev') # добавил в лист, в конец Nikolaev
print(cities)

cities.insert(2, 'Poltava') # добавил в лист, в конец Poltava 3м
print(cities)

del cities[-1]
print(cities) # Удалил последний - Nikolaev

cities.remove('Kyiv') # Удалил один объект по названию Kyiv.
print(cities)

deleted_city = cities.pop() #удалит по дефолиту послений.
print("Deleted city is: " + deleted_city)
print(cities)

cities.sort()  # По дефолиту сортирует по алфавиту
print(cities)

cities.sort(reverse=True)  # По дефолиту сортирует по наоборот алфавита.
print(cities)

cars = ['bmw', 'WV', 'seat','acura','nissan', 'toyota']

for car in cars:
    print(car.upper()) # upper - big letters

for x in range(1,6):
    print(x)

mynumber_list = list(range(0,10))
print(mynumber_list)

for x in mynumber_list:
    x = x * 2
    print(x)

print("Max number is: " + str(max(mynumber_list))) # выводит максимальную цифру.
print("Min number is: " + str(min(mynumber_list))) # выводит минимальную цифру.
print("Sum of list: " + str(sum(mynumber_list)))   # выводит сумму.

# cars = ['bmw', 'WV', 'seat','acura','nissan', 'toyota']

mycars = cars[1:4]   # Добавит с 1 по 4 позицию с листа cars ['WV', 'seat', 'acura']
print(mycars)

mycars = cars[:4]    # Добавит с начала (:) по 4 позицию с листа cars ['bmw', 'WV', 'seat', 'acura']
print(mycars)

mycars = cars[-3:]    # Добавит с -3 по последнюю (:)  позицию с листа cars ['acura', 'nissan', 'toyota']
print(mycars)

mysupercars=cars[:]   # [:] создаст копию листа, это два разные листа , без [:] соединяем, они будут равны.