import requests
import math


url = requests.get("https://drand.cloudflare.com/public/latest")
htmltext = url.text
htmltext = htmltext.replace("\"", "")
my_list = htmltext.split(",")
my_hex = my_list[1]
my_hex = my_hex[11:]
print(my_hex)
ent = 0.0
for i in my_hex:
    z = 10
    if i == "0":
        z = 1
    elif i == "1":
        z = 1
    elif i == "2":
        z = 2
    elif i == "3":
        z = 3
    elif i == "4":
        z = 4
    elif i == "5":
        z = 5
    elif i == "6":
        z = 6
    elif i == "7":
        z = 7
    elif i == "8":
        z = 8
    elif i == "9":
        z = 9
    elif i == "a":
        z = 10
    elif i == "b":
        z = 11
    elif i == "c":
        z = 12
    elif i == "d":
        z = 13
    elif i == "e":
        z = 14
    elif i == "f":
        z = 15
    else:
        print("There is a problem!Sorry!")
        break
    ent = ent + z*math.log(z, 10)
print(ent)