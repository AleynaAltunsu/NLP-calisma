import gensim.downloader as api
import numpy as np
import random

# Gensim'in gömülü FastText modelini indirin (örneğin Wiki News dataset'i üzerinde eğitilmiş)
# fasttext_model = api.load("fasttext-wiki-news-subwords-300")

# Pythagorean mesafesini hesaplayan fonksiyon
def pythagorean_distance(vec1, vec2):
    return np.sqrt(np.sum((vec1 - vec2) ** 2))

# Mesafeyi modeldeki kelime sayısına eşit olacak şekilde ayarlayan fonksiyon
def scale_distance(distance, max_scale):
    # Mesafeyi max_scale ile sınırlamak için bir ölçek katsayısı uygula
    max_distance = 10  # varsayılan olarak çok büyük bir mesafe belirleyebiliriz
    scaled_distance = (distance / max_distance) * max_scale
    return min(scaled_distance, max_scale)  # max_scale'i geçmeyecek şekilde sınırla

# Modeldeki kelimelerden rastgele birini seç
w1 = random.choice(list(fasttext_model.key_to_index.keys()))

# Kelime modelindeki tüm kelimeleri listeleyelim
kelime_listesi = list(fasttext_model.key_to_index.keys())

# Kelime listesindeki toplam kelime sayısını yazdır
total_words = len(kelime_listesi)
print(f"Modeldeki toplam kelime sayısı: {total_words}")
print(f"Seçilen gizli kelime: {w1}")

while True:
    w3 = input("Bir şeyler yazın (çıkmak için 'çıkış' yazın): ")

    if w3.lower() == "çıkış":
        print("Oyunu bıraktınız.")
        print(f"Seçilen kelime: {w1}")
        break

    w2 = input("Lütfen bir kelime giriniz: ")

    if w2 not in fasttext_model:
        print("Girdiğiniz kelime modelde bulunamadı.")
        continue

    # Seçilen kelime ve girilen kelimenin vektörlerini alalım
    vec1 = fasttext_model[w1]
    vec2 = fasttext_model[w2]

    # Vektörel uzaklık hesaplama
    distance = pythagorean_distance(vec1, vec2)

    # Mesafeyi modeldeki kelime sayısına sınırlandırma
    scaled_distance = scale_distance(distance, total_words)
    print(f"Seçilen kelime ile girilen kelime ARASINDAKİ KELİME SAYISI: {scaled_distance}")

    if distance <= 0.5:
        print("Tebrikler! Doğru tahmin!")
        break
