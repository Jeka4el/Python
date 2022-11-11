import sys
from urllib import request, parse # POST

myurl = "https://www.google.com/search?"
value = {'q=': 'Odessa'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'

try:
    mydata = parse.urlencode(value) # Превращаю mydata в другой формат
    myurl = myurl + mydata
    req = request.Request(myurl, headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)

except Exception:
    print("Error occurred during web request!!!")
    print(sys.exc_info()[1]) # выводим ошибку
