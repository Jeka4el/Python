import re

mytext = "I have a great desire to work and develop as a DevOps. In my opinion the IT field allows a person to\
develop unlimitedly and move humanity forward. This is my third experience of starting a career from\
scratch. Previously I was successful in my work and reached the limits beyond which I could not develop. I \
have a great deal of basic skills necessary for effective work. In everyday life I’m keen on martial arts and I’m\
interested in extreme sports. 111 32323 , jeka4el@gmail.com"

""""
\d - Any Digit 0-9 , любая цифра
\D - Any non Digit
\w - Any Alphabet symbol [A-Z a-z]
\W - Any non Alphabet symbol
\s - space , пробел
\S - Non space
[0-9]{4} - ищу любые цифры от 0 до 9 , четыре подряд 
[A-Z][a-z]+ - ищу слова где первая букава большая [A-Z] , вторая маленькая [a-z] и маленьких может быть сколько угодно +
"""

textloolfor = r"person" # What am i searching - person
allresults = re.findall(textloolfor, mytext) # findall is searching text (textloolfor) in mytext
print(allresults)

print("---NEXT---")

textloolfor = r"\d\d\d" # Ищет любые три цифры подряд.
allresults = re.findall(textloolfor, mytext)
print(allresults)

print("---NEXT---")

textloolfor = r"[0-9]{4}" # Ищет любые три цифры подряд.
allresults = re.findall(textloolfor, mytext)
print(allresults)

print("---NEXT---")

textloolfor = r"\w{6}" # ищу все слова состоязие из 6 символов.
allresults = re.findall(textloolfor, mytext)
print(allresults)

print("---NEXT---")

textloolfor = r"\w{6}" # ищу все слова состоязие из 6 символов.
allresults = re.findall(textloolfor, mytext)
print(allresults)

print("---NEXT---")

textloolfor = r"[A-Z][a-z]+"
allresults = re.findall(textloolfor, mytext)
print(allresults)

print("---NEXT---")
textloolfor = r"\w+@\w+\.\w+" # найду все эмайлы
allresults = re.findall(textloolfor, mytext)
print(allresults)
#########################################

input_filename = "./dumpfile.txt"
result_filename = "./results.txt"
input_file = open(input_filename, mode='r', encoding='Latin-1')
result_file = open(result_filename, mode='w', encoding='Latin-1')

lookfor = r"[\w._-]+@[\w._-]+\.[\w.]+" # r"[\w._-]+@(?!hotmail\.couk)[\w._-]+\.[\w.]+" исключаем hotmail.couk

mytext = input_file.read()

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    result_file.write(item + "\n")


print("Total :" + str(len(results)))

