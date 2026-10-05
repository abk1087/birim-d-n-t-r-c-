def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_to_mile(km):
    if km < 0:
        raise ValueError("Mesafe negatif bir değer olamaz.")
    return km * 0.621371

def mile_to_km(mile):
    if mile < 0:
        raise ValueError("Mesafe negatif bir değer olamaz.")
    return mile / 0.621371

def birim_donusturucu():
    while True:
        print("\n--- BİRİM DÖNÜŞTÜRÜCÜ ---")
        print("1. Celsius -> Fahrenheit")
        print("2. Fahrenheit -> Celsius")
        print("3. Kilometre -> Mil")
        print("4. Mil -> Kilometre")
        print("5. Çıkış")
        
        secim = input("Lütfen bir işlem seçin (1-5): ").strip()
        
        if secim == "5":
            print("Program kapatılıyor...")
            break
            
        if secim not in ["1", "2", "3", "4"]:
            print("⚠️ Hata: Geçersiz menü seçimi! Lütfen 1-5 arasında bir sayı girin.")
            continue
            
        try:
            # Kullanıcıdan sayısal değer alma
            girdi = input("Dönüştürülecek değeri girin: ")
            miktar = float(girdi)
            
            # Seçime göre hesaplama
            if secim == "1":
                sonuc = celsius_to_fahrenheit(miktar)
                print(f"✅ {miktar}°C = {sonuc:.2f}°F")
            elif secim == "2":
                sonuc = fahrenheit_to_celsius(miktar)
                print(f"✅ {miktar}°F = {sonuc:.2f}°C")
            elif secim == "3":
                sonuc = km_to_mile(miktar)
                print(f"✅ {miktar} km = {sonuc:.2f} mil")
            elif secim == "4":
                sonuc = mile_to_km(miktar)
                print(f"✅ {miktar} mil = {sonuc:.2f} km")

        except ValueError as e:
            # Metin girilmesi veya özel olarak fırlatılan negatif değer hatası
            if "Mesafe negatif" in str(e):
                print(f"⚠️ Mantık Hatası: {e}")
            else:
                print("⚠️ Tip Hatası: Lütfen harf veya sembol yerine geçerli bir sayı girin (Örn: 25 veya 12.5).")
        except Exception as e:
            # Öngörülemeyen diğer hatalar için güvenlik ağı
            print(f"⚠️ Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    birim_donusturucu()