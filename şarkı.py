# -*- coding: utf-8 -*-

import sqlite3

import time

class Şarkı():
    
    def __init__(self,isim,sanatçı,albüm,prodüksiyon,süre):
        
        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon = prodüksiyon
        self.süre = süre
        
    def __str__(self):
        
        return "Şarkı İsmi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirketi: {}\nŞarkı Süresi: {}\n".format(self.isim, self.sanatçı,self.albüm,self.prodüksiyon,self.süre)

class Liste():
    
    def __init__(self):
        
        self.baglanti_olustur()
        
    def baglanti_olustur(self):
        
        self.baglanti = sqlite3.connect("liste.db")
        
        self.cursor = self.baglanti.cursor()
        
        sorgu = "CREATE TABLE IF NOT EXISTS şarkılar (isim TEXT , sanatçı TEXT, albüm TEXT, prodüksiyon TEXT, süre INT)"
        
        self.cursor.execute(sorgu)
        
        self.baglanti.commit()
        
    def baglantiyi_kes(self):
        
        self.baglanti.close()

    def sarkilari_goster(self):
        
        sorgu = "Select * From şarkılar"
        
        self.cursor.execute(sorgu)
        
        şarkılar = self.cursor.fetchall()
        
        if (len(şarkılar) == 0):
            print("Listede şarkı yoktur...")
        
        else:
            for i in şarkılar:
                şarkı = Şarkı(i[0], i[1], i[2], i[3], i[4])
                
                print(şarkı)
        
        
    def sarki_sorgula(self,isim):
        
        sorgu = "Select * From şarkılar where isim = ?"
        
        self.cursor.execute(sorgu , (isim,))
        
        şarkılar = self.cursor.fetchall()
        
        if (len(şarkılar) == 0):
            print("Böyle bir şarkı bulunmuyor.")
        else:
            şarkı = Şarkı(şarkılar[0][0],şarkılar[0][1],şarkılar[0][2],şarkılar[0][3],şarkılar[0][4])
            
            print(şarkı)
            
    def sarki_ekle(self,şarkı):
        
        sorgu = "Insert into şarkılar Values(?,?,?,?,?)"
        
        self.cursor.execute(sorgu,(şarkı.isim,şarkı.sanatçı,şarkı.albüm,şarkı.prodüksiyon,şarkı.süre))
        
        self.baglanti.commit()
        
    def sarki_sil(self,isim):
        
        sorgu = "Select * From şarkılar where isim = ?"
        
        self.cursor.execute(sorgu , (isim,))
        
        şarkılar = self.cursor.fetchall()
        
        if (len(şarkılar) == 0):
            print("Böyle bir şarkı bulunmuyor.")
        else:
            print("Şarkı siliniyor...")
            time.sleep(2)
                    
            sorgu2 = "Delete From şarkılar where isim = ?"
            
            print("Şarkı silindi...")
            
            self.cursor.execute(sorgu2 , (isim,))

            self.baglanti.commit()
        
    def sure_hesapla(self):
        
        sorgu = "Select * From şarkılar"
        
        self.cursor.execute(sorgu)
        
        şarkılar = self.cursor.fetchall()
        
        if (len(şarkılar) == 0):
            print("Listede şarkı yoktur...")
        
        else:
            süre = 0
            for i in şarkılar:
                süre += i[4]
                
            print("Şarkıların Toplam Süresi {} saniyedir.".format(süre))

        
print("""******************************
      
Şarkı Programına Hoşgeldiniz.

İşlemler;

1. Şarkıları Göster

2. Şarkı Sorgula

3. Şarkı Ekle

4. Şarkı Sil

5. Şarkıların Toplam Süresini Hesapla

Çıkmak için 'q' ya basın.
******************************

""")

liste = Liste()

while True:
    işlem = input("Yapacağınız İşlem:")
    
    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        print("Yine Bekleriz...")
        break
    elif (işlem == "1"):
        liste.sarkilari_goster()
    elif (işlem == "2"):
        isim = input("Hangi şarkıyı istiyorsunuz ? ")
        print("Şarkı Sorgulanıyor...")
        time.sleep(2)
        liste.sarki_sorgula(isim)

    elif (işlem == "3"):
        isim = input("İsim: ")
        sanatçı = input("Sanatçı: ")
        albüm = input("Albüm: ")
        prodüksiyon = input("Prodüksiyon: ")
        süre = int(input("Süre: "))
        yeni_şarkı = Şarkı(isim,sanatçı,albüm,prodüksiyon,süre)
        
        print("Şarkı Ekleniyor...")
        time.sleep(2)
        liste.sarki_ekle(yeni_şarkı)
        print("Şarkı Eklendi...")
        
    elif (işlem == "4"):
        isim = input("Hangi Şarkıyı Silmek İstiyorsunuz ? ")
        
        cevap = input("Emin misiniz? (E/H)")
        
        if (cevap == "E"):
            
            liste.sarki_sil(isim)
        
    elif (işlem == "5"):
        liste.sure_hesapla()
    else:
        print("Geçersiz işlem...")
        
