import re
f = open("C:\\Users\\OlePedch\\Desktop\\okk\\zakon.txt", "r")
txt = f.read()
x = re.findall("zakon[a-ząęśżźćń0-9]* [a-ząęśżźćńA-ZĘĄŚŻŹĆŃ0-9]* [a-ząęśżźćńA-ZĘĄŚŻŹĆŃ0-9]* |rycerzy[a-ząęśżźćń0-9]* [a-ząęśżźćńA-ZĘĄŚŻŹĆŃ0-9]* [a-ząęśżźćńA-ZĘĄŚŻŹĆŃ0-9]*", txt)
print(x)
k = "Konstantynopol"
y = re.findall("[qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNMŚŻŹĆŃśżźćń]", k)
print(y)