# -*- coding: utf-8 -*-

# Süpermarket içindeki ürünler üzerinden bir tane Süpermarket Projesi
import sqlite3

import time

class Supermarket():
    
    def __init__(self,ürün_adı, ürün_grubu, son_kullanma_tarihi, fiyatı):
        
        self.ürün_adı = ürün_adı
        self.ürün_grubu = ürün_grubu
        self.son_kullanma_tarihi = son_kullanma_tarihi
        self.fiyatı = fiyatı
        
    def __str__(self):
        
        return "Ürün Adı: {}\nÜrün Grubu: {}\nSon Kullanma Tarihi: {}\nFiyatı: {}\n".format(self.ürün_adı, self.ürün_grubu ,self.son_kullanma_tarihi,self.fiyatı)
    
    

class Ürün():
    
    def __init__(self):
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("market.db")
        
        self.cursor = self.baglanti.cursor()
        
        sorgu = "CREATE TABLE IF NOT EXISTS ürünler (ürün_adı TEXT, ürün_grubu TEXT,son_kullanma_tarihi TEXT,fiyatı FLOAT)"
        
        self.cursor.execute(sorgu)
        
        self.baglanti.commit()
        
    def baglantiyi_kes(self):
        
        self.baglanti.close()
    
    def urunleri_goster(self):
        
        sorgu = "Select * From ürünler"
        
        self.cursor.execute(sorgu)
        
        ürünler = self.cursor.fetchall()
        
        if (len(ürünler) == 0):
            print("Markette ürün yok...")
        
        else:
            for i in ürünler:
                ürün = Supermarket(i[0], i[1], i[2], i[3])
                
                print(ürün)
    
    def urun_sorgula(self,ürün_adı):
        
        sorgu = "Select * From ürünler where ürün_adı = ?"
        
        self.cursor.execute(sorgu , (ürün_adı,))
        
        ürünler = self.cursor.fetchall()
        
        if (len(ürünler) == 0):
            print("Böyle bir ürün bulunmuyor.")
        else:
            ürün = Supermarket(ürünler[0][0],ürünler[0][1],ürünler[0][2],ürünler[0][3])
            
            print(ürün)
            
    def urun_ekle(self,ürün):
        
        sorgu = "Insert into ürünler Values(?,?,?,?)"
        
        self.cursor.execute(sorgu,(ürün.ürün_adı,ürün.ürün_grubu,ürün.son_kullanma_tarihi,ürün.fiyatı))
        
        self.baglanti.commit()
        
    def urun_sil(self,ürün_adı):
        
        sorgu = "Select * From ürünler where ürün_adı = ?"
        
        self.cursor.execute(sorgu , (ürün_adı,))
        
        ürünler = self.cursor.fetchall()
        
        if (len(ürünler) == 0):
            print("Böyle bir ürün bulunmuyor.")
        else:
            print("Ürün siliniyor...")
            time.sleep(2)
                    
            sorgu2 = "Delete From ürünler where ürün_adı = ?"
            
            print("Ürün silindi...")
            
            self.cursor.execute(sorgu2 , (ürün_adı,))

            self.baglanti.commit()
    def urun_guncelle(self,eski_fiyat,yeni_fiyat):
        
        sorgu = "Update ürünler set fiyatı = ? where fiyatı = ?"
        
        self.cursor.execute(sorgu , (yeni_fiyat,eski_fiyat,))
        
        print("Ürün Fiyatı Güncellendi...")
        
        self.baglanti.commit()
    
    def skt_ogrenme(self,ürün_adı):
        
        sorgu = "Select * From ürünler where ürün_adı = ?"
        
        self.cursor.execute(sorgu ,(ürün_adı,))
        
        ürünler = self.cursor.fetchall()
        
        if (len(ürünler) == 0):
            print("Böyle bir ürün bulunmuyor.")
        else:
            for i in ürünler:
                print("{} son kullanma tarihi {}".format(i[0], i[2]))
            

print("""******************************
      
Süpermarket Programına Hoşgeldiniz.

İşlemler;

1. Ürünleri Göster

2. Ürün Sorgula

3. Ürün Ekle

4. Ürün Sil

5. Fiyat Güncelle

6. Son Kullanma Tarihi Öğrenme

Çıkmak için 'q' ya basın.
******************************

""")
ürün = Ürün()
    


while True:
    işlem = input("Yapacağınız İşlem:")
    
    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        print("Yine Bekleriz...")
        break
    elif (işlem == "1"):
        ürün.urunleri_goster()
    elif (işlem == "2"):
        ürün_adı = input("Hangi ürünü arıyorunuz ? ")
        print("Ürün Sorgulanıyor...")
        time.sleep(2)
        ürün.urun_sorgula(ürün_adı)

    elif (işlem == "3"):
        ürün_adı = input("Ürün Adı: ")
        ürün_grubu = input("Ürün Grubu: ")
        son_kullanma_tarihi = input("Son Kullanma Tarihi: ")
        fiyatı = int(input("Ürün Fiyatı: "))
        yeni_ürün = Supermarket(ürün_adı,ürün_grubu,son_kullanma_tarihi,fiyatı)
        
        print("Ürün Ekleniyor...")
        time.sleep(2)
        ürün.urun_ekle(yeni_ürün)
        print("Ürün Eklendi...")
        
    elif (işlem == "4"):
        ürün_adı = input("Hangi Ürünü Silmek İstiyorsunuz ? ")
        
        cevap = input("Emin misiniz? (E/H)")
        
        if (cevap == "E" or "e"):
            
            ürün.urun_sil(ürün_adı)
        
    elif (işlem == "5"):
        ürün_adı = input("Hangi Ürünü Güncellemek İstiyorsunuz ? ")
        if (ürün.urun_sorgula(ürün_adı) != "Böyle bir ürün bulunmuyor."):
            eski_fiyat = float(input("Ürün Eski Fiyatı: "))
            yeni_fiyat = float(input("Ürün Yeni Fiyatı: "))
            ürün.urun_guncelle(eski_fiyat,yeni_fiyat)
    
    elif (işlem == "6"):
        ürün_adı = input("Hangi Ürünü Güncellemek İstiyorsunuz ? ")
        ürün.skt_ogrenme(ürün_adı)
        
    else:
        print("Geçersiz işlem...")
    
    
    
    
    
    
    
    
    