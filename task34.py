sonlar = [1, 2, 3, 7, 8, 9]
juftliklar = []

for i in range(len(sonlar)):
    for j in range(i + 1, len(sonlar)):
        if sonlar[i] + sonlar[j] == 10:
            juftliklar.append((sonlar[i], sonlar[j]))

print("Yig'indisi 10 ga teng juftliklar:", juftliklar)