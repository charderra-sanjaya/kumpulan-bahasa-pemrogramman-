#variabel
a = "Charderra Eka Bagas Sanjaya"
def func():
    a = "any"
    print ("Selamat "+ a)
func()
print (a)

#definisi
def tambah():
    a = 5 
    b= 4 
    c= a+b
    print (c)

tambah()

#parameter
def data(nama,nim):
    print(f"Nama saya {nama} dan Nim : {nim}")
data ("Charderra Eka Bagas Sanjaya","20210801088")

#contoh
def total(sisi):
    return sisi*sisi

def segitiga(alas,tinggi):
    return 0.5*alas*tinggi