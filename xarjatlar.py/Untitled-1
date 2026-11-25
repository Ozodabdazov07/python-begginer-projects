xarajatlar = []

while True:
    print("\n1. Xarajat qo'shish")
    print("2. Ro'yxatni ko'rish")
    print("3. Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        nomi = input("Nima uchun? ")
        summa = float(input("Summa: "))
        xarajatlar.append((nomi, summa))
        print("Qo'shildi!")

    elif tanlov == "2":
        jami = 0
        for nomi, summa in xarajatlar:
            print(f"{nomi}: {summa}")
            jami += summa
        print(f"Jami: {jami}")

    elif tanlov == "3":
        break

    else:
        print("Noto'g'ri tanlov")
        