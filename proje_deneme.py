from kütüphane import *

print("""
      
**************************************      
      
Kütüphane Programına Hoşgeldiniz..  

İşlemler:

1- Kitapları Göster
2- Kitap Sorgulama
3- Kitap Ekle
4- Kitap Sil
5- Baskı Yükselt

Çıkmak için q'ya basın.
      
***************************************""")

kütüphane = Kütüphane()

while True:
    
    işlem = input("Yapacağınız işlem: ")
    
    if(işlem == "q"):
        
        print("Program sonlandırılıyor..")
        time.sleep(2)
        print("Yine bekleriz....\n\n")
        break
    
    elif(işlem == "1"):
        
        kütüphane.kitapları_göster()
        
    elif(işlem == "2"):
        
        isim = input("Hangi kitabı istiyorsunuz: ")
        print("Kitap sorgulanıyor..\n\n")
        time.sleep(2)
        
        kütüphane.kitap_sorgula(isim)
        
    elif(işlem == "3"):
        
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))
        
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        
        print("\nKitap ekleniyor..")
        time.sleep(2)
        
        kütüphane.kitap_ekle(yeni_kitap)
        
        print("Kitap eklendi.\n\n")
        
    elif(işlem == "4"):
        
        isim = input("Hangi kitabı silmek istiyorsunuz: ")
        cevap = input("Emin misiniz (E/H): ")
        
        if(cevap == "E"):
            
            print("Kitap siliniyor..")
            time.sleep(2)
            
            kütüphane.kitap_sil(isim)
            
            print("Kitap silindi.\n\n")
        
    elif(işlem == "5"):
        
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz: ")
        
        print("Baskı yükseltiliyor..")
        time.sleep(2)
        
        kütüphane.baskı_yükselt(isim)
        
        print("Baskı yükseltildi.\n\n")
    
    else:
        
        print("Geçersiz işlem !! Lütfen geçerli bir işlem seçiniz.\n\n")