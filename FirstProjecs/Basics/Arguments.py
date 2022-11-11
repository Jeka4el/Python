import sys # запускаю файл через терминал, аргументы передаються sys.argv
import os
# print("Hello")
#
# print (sys.argv[1:])   # Первый аргумент (0) это название файла. Поэтому я начинаю со второго (1).
# print (sys.argv[1])
# print (sys.argv[2])
# print (sys.argv[3])
#
# for i in sys.argv:
#     print (i)

x = len(sys.argv)
if x > 1:
    print("Arguments entereded: " + str(sys.argv[1:]))
else:
    print("Arguments no provided")

os.system("ls")
sys.exit()
