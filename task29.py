sonlar = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]
noyoblar = []

for s in sonlar:
    if sonlar.count(s) == 1:
        noyoblar.append(s)

print("Noyob elementlar:", noyoblar)