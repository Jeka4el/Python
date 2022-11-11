import json
filename = "user_settings.txt"
myfile = open(filename, mode="w", encoding="Latin-1")

player1 = {
    'PlayerName': "Herbert Garrison",
    'Score': 12,
    'awards': ["Best teacher", "Real men", "Good boy"]
}

player2 = {
    'PlayerName': "Conor McGregor",
    'Score':14,
    'awards': ["UFC Champion", "The best whiskey", "Plumber of the Year"]

}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)


# --- Save by JSON ---

json.dump(myplayers,myfile)
myfile.close()

# --- Load by JSON ---

myfile = open(filename, mode='r', encoding="Latin-1")
json_data = json.load(myfile)

for user in json_data:
    print("Player name is : " + str(user['PlayerName']))
    print("Player Score is :" + str(user['Score']))
    print("Player awsrds is : " + str(user['awards']))