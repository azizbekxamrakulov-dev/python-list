fanlar = ["Matematika", "Fizika", "Tarix", "Biologiya"]
print("Fanlar:", fanlar)

index = int(input("O'zgartirmoqchi bo'lgan fan indeksini kiriting (0-3): "))
yangi_fan = input("Yangi fan nomini kiriting: ")

fanlar[index] = yangi_fan
print("Yangilangan ro'yxat:", fanlar)