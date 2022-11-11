mystring = "one two three"

name = "BabuWka Miwa"

print(name)
print(name.title()) # .title() делает занлавные буквы.
print(name.upper()) # .upper() преобразует все буквы в большие
print(name.lower()) #  преобразует все буквы в маленькие

print("Messages:\n\tMwssage1\n\tMwssage2\n\tMessage3\nEND") # \n - новая строка \t - таб.
print("Lower name: " + name.lower())

a = "   ,Ded Mazay..   "
print(a)
print(a.rstrip()) # Сотрет все пробелы справа.
print(a.lstrip()) # Сотрет все пробелы слева.
print(a.strip())  # Сотрет все пробелы с двух сторон.

b = ".....hi....."
print(b.strip(".")) # обрежет точки