from urllib import request
import sys

myurl = "http://jeka4el.od.ua/img/x1080.jpg" # file to download
myfile = "/home/jeka/Python/foto.jpg"                 # location and name in my PC

try:
    print("Start download file " + myurl)
    request.urlretrieve(myurl, myfile)

except Exception:
    print("Some error")
    print(sys.exc_info())
    exit

print("file downloaded and saved in " + myfile)
