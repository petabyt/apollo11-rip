import re

fp = open("images11.html", "rb")
c = fp.read()

c = str(c)

find = re.findall(r"AS11-([0-9]+)-([0-9]+)HR\.jpg", c)
for img in find:
    print(
        "https://www.hq.nasa.gov/alsj/a11/" + 
        "AS11-" + img[0] + "-" + img[1] + "HR.jpg")

print("Total", str(len(find)), "images")
