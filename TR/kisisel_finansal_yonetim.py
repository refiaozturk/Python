import os

def gelir_ekle(gelir_listesi):
    gelir = float(input("Eklemek istediğiniz gelir miktarını giriniz: "))
    gelir_listesi.append(gelir)

def gider_ekle(gider_listesi):
    gider = float(input("Eklemek istediğiniz gider miktarını giriniz: "))
    gider_listesi.append(gider)

def gelir_goster(gelir_listesi):
    print("Gelir Listesi: ")
    for gelir in gelir_listesi:
        print(f"- {gelir}")

def gider_goster(gider_listesi):
    print("Gider Listesi: ")
    for gider in gider_listesi:
        print(f"- {gider}")

def butce_hesapla(gelir_listesi, gider_listesi):
    toplam_gelir = sum(gelir_listesi)
    toplam_gider = sum(gider_listesi)
    butce = toplam_gelir - toplam_gider
    return butce

def dosyaya_kaydet(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(f"{item}\n")

def read_from_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [float(line.strip()) for line in file.readlines()]
    
def main():
    gelir_listesi = read_from_file("gelirler.txt")
    gider_listesi = read_from_file("giderler.txt")

    while True:
        print("""
              Kişisel Finans Yönetim Uygulaması
              ---------------------------------
              1. Gelir Ekle
              2. Gider Ekle
              3. Gelirleri Göster
              4. Giderleri Göster
              5. Aylık Bütçeyi Hesapla
              6. Çık ve Verileri Kaydet
              """)
        
        secim = input("Bir seçenek seçiniz (1-6): ")

        if secim == "1":
            gelir_ekle(gelir_listesi)
        
        elif secim == "2":
            gider_ekle(gider_listesi)
        
        elif secim == "3":
            gelir_goster(gelir_listesi)

        elif secim == "4":
            gider_goster(gider_listesi)

        elif secim == "5":
            butce = butce_hesapla(gelir_listesi, gider_listesi)
            print(f"Aylık bütçeniz: {butce}")
        
        elif secim == "6":
            dosyaya_kaydet("gelirler.txt", gelir_listesi)
            dosyaya_kaydet("giderler.txt", gider_listesi)
            print("Veriler kaydedildi. Çıkış yapılıyor...")
            break
        
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyiniz.")

if __name__ == "__main__":
    main()