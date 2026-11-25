#Hesap adında bir sınıf oluşturuyoruz
class Hesap:
    #Sınıfın başlangıç özelliklerini (ad soyad, hesap no, bakiye) tanımlıyoruz.
    def __init__(self, ad_soyad, hesap_no, bakiye=0):
        self.ad_soyad = ad_soyad 
        self.hesap_no = hesap_no
        self.bakiye = bakiye 
    #Hesaba para yatırma fonksiyonu tanımlıyoruz    
    def para_yatir(self , miktar):
        #Yatırılan miktar 0'dan büyükse bakiyeye ekliyoruz.
        if miktar >= 0:
            self.bakiye += miktar
            print("Yeni bakiyeniz: ",self.bakiye)
        #Negatif miktar girilirse uyarı veriyoruz.
        else:
            print("Geçersiz miktar!!!")
    # Hesaba para çekme fonksiyonu tanımlıyoruz.
    def para_cek(self, miktar):
        # miktar bakiyeden fazla ise uyarı veriyoruz
        if miktar > self.bakiye:
            print("Yetersiz bakiye!!!")
        # miktar bakyeye eşit veya daha azsa bakiyeden bu miktarı çıkartıyoruz.    
        else:
            self.bakiye -= miktar
            print("Yeni bakiyeniz:",self.bakiye)
    # Hesap bilgilerini ve güncel bakiyeyi ekrana yazdıran fonksiyonu tanımlıyoruz.        
    def bakiye_goruntule(self):
        print("Hesap sahibi:", self.ad_soyad)
        print("Hesap No: ", self.hesap_no)
        print("Güncel Bakiye: ", self.bakiye)
# Kullanıcıdan hesap bilgilerini alıyoruz
ad_soyad = input("Adınız ve soyadınız:")
hesap_no = input("Hesap numaranız: ")
bakiye = float(input("Başlangıç bakiyesi: "))
# Alınan bilgilerle Hesap sınıfından hesap adında bir nesne oluşturuyoruz.
hesap = Hesap(ad_soyad, hesap_no, bakiye)
# Kullanıcıdan yatırılacak tutarı alıp para yatırma işlemini yapıyoruz.
yatirilacak = float(input("Yatırma miktarı:"))
hesap.para_yatir(yatirilacak)
# Kullanıcıdan çekilecek tutarı alıp para çekme işlemini yapıyoruz.
cekilecek = float(input("Çekmek istediğiniz tutar:"))
hesap.para_cek(cekilecek)
# Hesap bilgilerini ve güncel bakiyeyi ekrana yazdırıyoruz.
hesap.bakiye_goruntule()