davlatlar = ["O'zbekiston", "Turkiya", "Yaponiya", "Germaniya", "AQSH", "Koreya"]
print("Mavjud davlatlar:", davlatlar)

start = int(input("Boshlanish indeksini kiriting: "))
end = int(input("Tugash indeksini kiriting: "))

kesma = davlatlar[start:end]
print(f"{start}-dan {end}-gacha bo'lgan elementlar:", kesma)