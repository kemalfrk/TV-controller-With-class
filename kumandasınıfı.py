import random
import time

class Kumanda():

    def __init__(self,tv_durum="Kapali",tv_ses=0,kanal_listesi=["Trt","Kanald","NTV"],kanal="Trt"):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):

        if(self.tv_durum=="Acik"):
            print("Televizyon Zaten Acik..")
        
        else:
            print("Televizyon Aciliyorr...")
    
    def tv_kapat(self):
        if(self.tv_durum=="Kapali"):
            print("Televizyon Zaten Kapali..")
        
        else:
            print("Televizyon Kapaniyor...")
            self.tv_durum="Kapali"
    
    def ses_ayarlari(self):
        while True:

            cevap=input("Sesi Azalt:'<'\nSesi Artir: '>'\n Cikis:cikis ")

            if(cevap=="<"):
                if(self.tv_ses !=0):

                    self.tv_ses -=1
                    print("Ses:",self.tv_ses)
            
            elif (cevap==">"):
                if(self.tv_ses !=32):
                    self.tv_ses +=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)

                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor...")
        time.sleep(1) #bir saniye bekle diyoruz

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi....")
    
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Su anki Kanal:",self.kanal)
    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return "Tv Durumu: {}\nTv ses: {}\nKanal Listesi: {}\nSu anki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    
kumanda=Kumanda()

print("""

________Televizyon uygulamasi_________
-----------------------------------------------------

1.Tv Ac
2.Tv Kapat
3.Ses Ayarlari
4.Kanal Ekle
5.Kanal Sayisini Ögrenme
6.Rastgele Kanala Gecme
7.Televizyon Bilgileri

Cikmak icin "q" ya basiniz.
-------------------------------------------------------
""")

while True:
    islem=input("İslemi Seciniz:")

    if(islem=="q"):
        print("Program Sonlandiriliyor...")
        break
    elif(islem=="1"):
        kumanda.tv_ac()
    elif(islem=="2"):
        kumanda.tv_kapat()
    elif(islem=="3"):
        kumanda.ses_ayarlari()
    elif(islem=="4"):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayirarak giriniz:")
        kanal_listesi=kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif(islem=="5"):
        print("Kanal Sayisi:",len(kumanda))
    
    elif(islem=="6"):
        kumanda.rastgele_kanal()
    
    elif(islem=="7"):
        print(kumanda)
    
    else:
        print("Gecersiz İslem Girdiniz.Lütfen Tekrar Deneyiniz!")
