def tambah():
    a = input("angka 1 :")
    b = input("angka 2 :")
    c = a+b
    print(c)

def kurang():
    a = input("angka 1 :")
    b = input("angka 2 :")
    c = a-b
    print(c)

def kali():
    a = input("angka 1 :")
    b = input("angka 2 :")
    c = a*b
    print(c)

def pilihan():
    print("1. +")
    print("2. -")
    print("exit")

while True:
    pilihan()
    pil = int(input("pilihan :"))

    if pil == 1:
        tambah()
    elif pil == 2:
        kurang()
    elif pil == 3:
        kali()
    else:
        break