#Bu kod büyük ve küçük harfleri aynı kabul etmektedir.
#Kullanıcıdan bir kelime veya metin girmesini istiyoruz.
metin=input("Lütfen bir kelime veya metin giriniz: ")
#len fonksiyonu ile metnin uzunluğunu hesaplıyoruz.
uzunluk=len(metin)
#büyük/küçük harfe duyarsız olması için tüm metni küçük harfe çeviriyoruz ve sonrasında kelimeleri birbirinden ayırıyoruz.
kelimeler=metin.lower().split()
kelime_sayisi=len(kelimeler)

en_uzun=0
tekrar={}
#for döngüsü ile kelimeleri tek tek kontrol ediyoruz.
#ilk if döngüsü ile en uzun kelimeyi bulmaya çalışıyoruz.
for kelime in kelimeler:
    if len(kelime)>en_uzun:
        en_uzun=len(kelime)
    #Kelime sözlükte varsa sayısını 1 artırıyoruz.
    if kelime in tekrar:
        tekrar[kelime]+=1
    #Kelime sözlükte yoksa 1 olarak ekliyoruz.
    else:
        tekrar[kelime]=1

#Hesaplanan tüm değerleri ekrana yazdırıyoruz.
print("Toplam kelime sayısı: ",kelime_sayisi)
print("Boşluklar dahil toplam karakter sayısı: ", uzunluk)
print("En uzun kelimenin karakter sayısı:  ", en_uzun)
print("Kelime tekrarları: ", tekrar)