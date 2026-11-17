#!/usr/bin/env python3
# Sonsuz Çay Demleme Deneyi
# Bu program gerçekten çay demler. Dijital olarak. Sonsuza kadar.
# Uyarı: Çalıştırırsanız gerçek çay içme ihtiyacınız artabilir.

import time
import random
import sys

def demle_cay(sicaklik=85, seker_sayisi=2, sure=float('inf')):
    """
    Dünyanın en bilimsel çay demleme fonksiyonu.
    Asla bitmez. Asla.
    """
    baslangic = time.time()
    tur = 0
    sikayetler = [
        "Su çok sıcak, çay yaprakları ağlıyor.",
        "Şeker erimedi, belki de şeker greve gitti.",
        "Demlenme süresi yetersiz, bilim böyle diyor.",
        "Bardak çok küçük, evren çayı içine sığdıramıyor.",
        "Çay poşeti kendini üstün görüyor, bizi aşağılıyor.",
        "Su çok sert, belki yumuşatmak lazım (psikolojik olarak).",
        "Demlik kapağı kapalı değil, çay kaçıyor evrenden.",
        "Bu çay demlenirken dünya dönmeye devam ediyor, adaletsizlik."
    ]
    
    print("🍵 Sonsuz Çay Demleme Deneyi Başlatıldı...")
    print("Bilimsel parametreler: Sıcaklık=", sicaklik, "°C, Şeker=", seker_sayisi, "adet")
    print("Durdurmak için Ctrl+C'ye basın. (Ama basmayın, çay küsülür.)")
    print("-" * 50)
    
    try:
        while True:
            tur += 1
            gecen = time.time() - baslangic
            print(f"Tur {tur}: Demlenme devam ediyor... ({gecen:.1f} saniye)")
            
            # Rastgele şikayet
            if random.random() > 0.6:
                print("  ⚠️ ", random.choice(sikayetler))
            
            # Gizli kontrol (sadece çok dikkatli olanlar fark eder)
            if tur == 42 and random.random() > 0.99:  # neredeyse hiç çıkmaz
                print("  [gizli not: her şey yolunda, merak etme]")
            
            # Simüle edilmiş bekleme (gerçek demleme gibi yavaş)
            time.sleep(random.uniform(1.5, 4.0))
            
            # Ara sıra "başarı" mesajı
            if tur % 7 == 0:
                print("  ✅ Çay bir adım daha demlendi. Tebrikler, hiçbir şey değişmedi.")
                
    except KeyboardInterrupt:
        print("\n🚫 Deney durduruldu. Çay küsüldü ve bir daha demlenmeyecek.")
        print("Toplam tur:", tur)
        print("Not: Gerçek çay içmeyi unutmayın. Bu program sadece simülasyon.")
        sys.exit(0)

if __name__ == "__main__":
    demle_cay()
