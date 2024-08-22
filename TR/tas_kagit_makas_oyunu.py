import random

def bilgisayar_secimi():
    oyun_listesi = ["taş", "kağıt", "makas"]
    return random.choice(oyun_listesi)

def oyuncu_secimi():
    while True:
        oyuncu_secimi = input("Lütfen (taş, kağıt, makas) birini seçiniz: ").lower().strip()

        if oyuncu_secimi in ["taş", "kağıt", "makas"]:
            return oyuncu_secimi
        
        else:
            print("Geçersiz seçim. Lütfen 'taş', 'kağıt' veya 'makas' yazınız.")

def result(oyuncu_secimi, bilgisayar_secimi):
    if oyuncu_secimi == bilgisayar_secimi:
        return "Berabere!"
    
    elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
        (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
        (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
        return "Roundu Kazandınız!"
    
    else:
        return "Roundu Kaybettiniz!"
    
def main():
    print("Taş - Kağıt - Makas Oyununa Hoşgeldiniz!")
    oyuncu_skor = 0
    bilgisayar_skor = 0

    while True:
        oyuncu = oyuncu_secimi()
        bilgisayar = bilgisayar_secimi()

        print(f"Sizin seçiminiz: {oyuncu} - Bilgisayarın seçimi: {bilgisayar}")

        oyun_sonucu = result(oyuncu, bilgisayar)

        print(oyun_sonucu)

        # her bir round için
        if oyun_sonucu == "Roundu Kazandınız!":
            oyuncu_skor += 1
            print(f"Skorunuz: {oyuncu_skor} | Bilgisayarın Skoru: {bilgisayar_skor}")
        
        elif oyun_sonucu == "Roundu Kaybettiniz!":
            bilgisayar_skor += 1
            print(f"Skorunuz: {oyuncu_skor} | Bilgisayarın Skoru: {bilgisayar_skor}")

        else:
            bilgisayar_skor = bilgisayar_skor
            oyuncu_skor = oyuncu_skor
            print(f"Skorunuz: {oyuncu_skor} | Bilgisayarın Skoru: {bilgisayar_skor}")

        # genel sonuç için
        if oyuncu_skor == 3 and oyuncu_skor > bilgisayar_skor:
            print("Tebrikler! Oyunu kazandınız!")
            tekrar_oyna = input("Eğer tekrar oynamak isterseniz 'evet' yazınız. Oyundan çıkmak isterseniz ise klavyeden herhangi bir tuşa basınız:").lower().strip()

            if tekrar_oyna != "evet":
                print("Oyundan çıkılıyor...")
                print("Oyundan çıkıldı.")
                break
            else:
                bilgisayar_skor = 0
                oyuncu_skor = 0

        elif bilgisayar_skor == 3 and bilgisayar_skor > oyuncu_skor:
            print("Oyunu kaybettiniz!")
            tekrar_oyna = input("Eğer tekrar oynamak isterseniz 'evet' yazınız. Oyundan çıkmak isterseniz ise klavyeden herhangi bir tuşa basınız:").lower().strip()

            if tekrar_oyna != "evet":
                print("Oyundan çıkılıyor...")
                print("Oyundan çıkıldı.")
                break
            else:
                bilgisayar_skor = 0
                oyuncu_skor = 0

if __name__ == "__main__":
    main()