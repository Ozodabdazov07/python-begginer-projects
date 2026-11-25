import json
import os

FAYL = "xarajatlar.json"


def yuklash():
    if os.path.exists(FAYL):
        with open(FAYL, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def saqlash(xarajatlar):
    with open(FAYL, "w", encoding="utf-8") as f:
        json.dump(xarajatlar, f, ensure_ascii=False, indent=2)


xarajatlar = yuklash()

while True:
    print("\n1. Xarajat qo'shish")
    print("2. Ro'yxatni ko'rish")
    print("3. Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        nomi = input("Nima uchun? ")
        try:
            summa = float(input("Summa: "))
        except ValueError:
            print("Summa raqam bo'lishi kerak!")
            continue
        xarajatlar.append({"nomi": nomi, "summa": summa})
        saqlash(xarajatlar)
        print("Qo'shildi va saqlandi!")

    elif tanlov == "2":
        jami = 0
        for x in xarajatlar:
            print(f"{x['nomi']}: {x['summa']}")
            jami += x["summa"]
        print(f"Jami: {jami}")

    elif tanlov == "3":
        break

    else:
        print("Noto'g'ri tanlov")