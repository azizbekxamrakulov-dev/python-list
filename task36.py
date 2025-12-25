sozlar = ["olma", "anor", "shaftoli", "banan"]
eng_uzun = sozlar[0]

for s in sozlar:
    if len(s) > len(eng_uzun):
        eng_uzun = s

print("Eng uzun so'z:", eng_uzun)