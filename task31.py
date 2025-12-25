input_list = [3, 5, 3, 2, 5, 5, 1]
max_count = 0
eng_kop_takrorlangan = input_list[0]

for x in input_list:
    if input_list.count(x) > max_count:
        max_count = input_list.count(x)
        eng_kop_takrorlangan = x

print("Eng ko'p takrorlangan:", eng_kop_takrorlangan)