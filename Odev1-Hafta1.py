#Sayılar: Python'da tamsayılar (integer), kayan noktalı sayılar (float) ve karmaşık sayılar (complex) gibi farklı sayı türleri bulunur
a = 42          # tamsayı (integer)
b = 3.14        # kayan noktalı sayı (float)
c = 2 + 3j      # karmaşık sayı (complex)
#Metin (string): Python'da metin verileri string olarak adlandırılır. Stringler tek tırnak veya çift tırnak içine alınır
isim = 'Ahmet'
mesaj = "Merhaba, dünya!"
#Boolean: True ve False olmak üzere iki değere sahip olan veri tipidir
x = True
y = False
#Liste: Python'da, birden fazla veri öğesini bir arada tutmak için liste kullanılabilir. Liste, eşsiz olmayan elemanlardan oluşan bir sıralı koleksiyondur
meyveler = ['elma', 'armut', 'çilek', 'muz']
#Tuple: Liste gibi elemanları saklamak için kullanılan bir başka veri tipidir. Ancak tuple'lar, değiştirilemez (immutable) olarak tanımlanırlar
renkler = ('kırmızı', 'yeşil', 'mavi')
#Sözlük (dictionary): Anahtar-değer çiftlerinden oluşan bir veri tipidir. Sözlükler, anahtarlarının değerlerine hızlı bir şekilde erişebilmenizi sağlar
telefonlar = {'Ahmet': '0555 555 55 55', 'Mehmet': '0533 333 33 33', 'Ayşe': '0544 444 44 44'}


#soru2
#  #Kurslarim, Tum Kurslar, Kariyer ve SSS ====> String
#Profil resmi ustune tiklandiginda cikan kisim ====> Liste
#Profil duzenledeki ad, soyad, sifre ====> String

#soru3
ChangePassword = True
NewPassword="12345"
ConfirmPassword="123456"
if(ChangePassword):
   if NewPassword == ConfirmPassword:
    print("İki string birbirine eşittir.")
   else:
    print("İki string birbirine eşit değildir.")
