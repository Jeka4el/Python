enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Ded Mazay'
}

print(enemy)

print("Location x = " + str(enemy['loc_x']))
print("Lacation y = " +str(enemy['loc_y']))
print("Name is " + (enemy['name']))

enemy['rank']= 'Pornohero'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'
print(enemy)

print('=======================================')

enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Ded Mazay',
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

all_enemys = []

for x in range(0,10):
    all_enemys.append(enemy.copy())

for ene in all_enemys:
    print(ene)
print('=======================================')

all_enemys[5]['health'] = 30
all_enemys[8]['name'] = "Ded Makar"
all_enemys[2]['loc_x'] += 10
for ene in all_enemys:
    print(ene)

