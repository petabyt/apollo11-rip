import re, os

fp = open("images11.html", "rb")
c = fp.read()

c = str(c)

find = re.findall(r"AS11-([0-9]+)-([0-9]+)HR\.jpg", c)
for img in find:
    url = (
        "https://www.hq.nasa.gov/alsj/a11/" + 
        "AS11-" + img[0] + "-" + img[1] + "HR.jpg")
    os.system("cd images; wget  " + url)
