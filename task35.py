sozlar = ["u", "bu", "ana", "mana", "qanday", "kompyuter", "python"]

savat1 = []
savat2 = []
savat3 = []

for s in sozlar:
    uzunlik = len(s)
    if uzunlik <= 3:
        savat1.append(s)
    elif 4 <= uzunlik <= 6:
        savat2.append(s)
    else:
        savat3.append(s)

print("1-savat:", savat1)
print("2-savat:", savat2)
print("3-savat:", savat3)