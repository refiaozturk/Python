calisanlar = []

def calisan_ekle():
    ad = input("Çalışanın adını giriniz: ").title()
    maas = input("Maaşını giriniz: ")

    if maas.isdigit():
        calisanlar.append({"ad": ad, "maaş": int(maas)})
        print(f"{ad} adlı çalışan eklendi.")

    else:
        print("Geçersiz maaş girdiniz. Lütfen tekrar deneyin.")


def calisanlari_listele():
    if not calisanlar:
        print("Henüz çalışan eklenmedi.")

    else:
        for calisan in calisanlar:
            print(f"Çalışan: {calisan['ad']}, Maaş: {calisan['maaş']}")


def maasa_gore_calisan_filtreleme(min_maas):
    filtrelenmis = list(filter(lambda calisan: calisan['maaş'] > min_maas, calisanlar))

    if not filtrelenmis:
        print(f"{min_maas} maaşından yüksek maaşta çalışan yok.")
    
    else:
        for calisan in filtrelenmis:
            print(f"Çalışan: {calisan['ad']}, Maaş: {calisan['maaş']}")


def main():
    while True:
        print("""
              Çalışan Maaş Yönetim Sistemi
              ----------------------------
              1. Çalışan Ekle
              2. Çalışanları Listele
              3. Belirli Maaştan Yüksek Olan Çalışanları Filtrele
              4. Çıkış
              """)
        
        secim = input("Lütfen size belirtilen listeden seçiminizi yapınız (1-4): ")

        if secim == "1":
            calisan_ekle()
        
        elif secim == "2":
            calisanlari_listele()

        elif secim == "3":
            min_maas = input("Minimum maaş değerini giriniz: ")

            if min_maas.isdigit():
                maasa_gore_calisan_filtreleme(int(min_maas))

            else:
                print("Geçersiz maaş girdiniz. Lütfen tekrar deneyiniz.")

        elif secim == "4":
            print("Programdan çıkılıyor...")
            print("Programdan çıkıldı.")
            break

        else:
            print("Geçersiz seçim yaptınız. Lütfen tekrar deneyiniz.")

if __name__ == "__main__":
    main()