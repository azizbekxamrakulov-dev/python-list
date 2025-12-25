list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
kesishma = []

for x in list1:
    if x in list2 and x not in kesishma:
        kesishma.append(x)

print("Umumiy elementlar:", kesishma)