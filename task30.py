sozlar = ["alla", "kitob", "non", "olma", "kiyik"]
palindromlar = []

for s in sozlar:
    if s == s[::-1]:
        palindromlar.append(s)

print("Palindromlar:", palindromlar)