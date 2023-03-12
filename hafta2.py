ogrenciler = []

def ogrenci_ekle(ad, soyad):
    ogrenciler.append({"ad": ad, "soyad": soyad})

def ogrenci_sil(ad, soyad):
    for ogrenci in ogrenciler:
        if ogrenci["ad"] == ad and ogrenci["soyad"] == soyad:
            ogrenciler.remove(ogrenci)

def ogrenci_listele():
    for index, ogrenci in enumerate(ogrenciler):
        print(f"{index}: {ogrenci['ad']} {ogrenci['soyad']}")

def ogrenci_numarasi(ad, soyad):
    for index, ogrenci in enumerate(ogrenciler):
        if ogrenci["ad"] == ad and ogrenci["soyad"] == soyad:
            return index

def ogrencileri_sil():
    i = 0
    while i < len(ogrenciler):
        ogrenciler.remove(ogrenciler[i])
ogrenci_ekle("Ali", "Demir")
ogrenci_ekle("Ayşe", "Yılmaz")
ogrenci_ekle("Mehmet", "Ak")

ogrenci_listele() 

print("Numarası:", ogrenci_numarasi("Ayşe", "Yılmaz")) 
ogrenci_sil("Ali", "Demir")
ogrenci_listele() 

ogrencileri_sil()
ogrenci_listele() 