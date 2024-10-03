
# README

## Proje Açıklaması
Bu proje, Gensim kütüphanesi kullanarak bir FastText kelime gömme modeli üzerinde basit bir kelime tahmin oyunu geliştirmektedir. Oyuncu, rastgele seçilen bir kelimeyi tahmin etmeye çalışırken, modeldeki kelimeler arasındaki vektörel mesafeyi kullanarak doğru tahmin yapmaya çalışır.

## Kullanılan Kütüphaneler
- `gensim`: Kelime gömme modellerini yüklemek ve kullanmak için kullanılır.
- `numpy`: Matematiksel hesaplamalar ve dizilerle çalışmak için kullanılır.
- `random`: Rastgele seçim yapabilmek için kullanılır.

## Kurulum
Bu projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Python ve gerekli kütüphanelerin yüklü olduğundan emin olun. Gensim ve NumPy kütüphanelerini yüklemek için aşağıdaki komutu kullanabilirsiniz:
   ```bash
   pip install gensim numpy
   ```

2. Gensim kütüphanesinden FastText modelini indirin (örneğin Wiki News dataset'i üzerinde eğitilmiş). Yorum satırındaki satırı etkinleştirerek model yükleyin:
   ```python
   fasttext_model = api.load("fasttext-wiki-news-subwords-300")
   ```

## Kodun Açıklaması

### 1. Kütüphanelerin İçe Aktarılması
```python
import gensim.downloader as api
import numpy as np
import random
```
- Gensim'in gömülü FastText modelini indirmek için `gensim.downloader` kullanılır.
- `numpy`, matematiksel hesaplamalar için kullanılır.
- `random`, rastgele kelime seçimi için kullanılır.

### 2. Mesafe Hesaplama Fonksiyonu
```python
def pythagorean_distance(vec1, vec2):
    return np.sqrt(np.sum((vec1 - vec2) ** 2))
```
- İki kelime arasındaki vektörel mesafeyi hesaplamak için Pisagor teoremini kullanır. `vec1` ve `vec2` vektörleri arasındaki farkların karelerinin toplamının karekökünü alarak mesafeyi döner.

### 3. Mesafeyi Ölçeklendirme Fonksiyonu
```python
def scale_distance(distance, max_scale):
    max_distance = 10  # varsayılan olarak çok büyük bir mesafe belirleyebiliriz
    scaled_distance = (distance / max_distance) * max_scale
    return min(scaled_distance, max_scale)  # max_scale'i geçmeyecek şekilde sınırla
```
- Verilen mesafeyi (distance), modeldeki toplam kelime sayısına (max_scale) göre ölçeklendirir.
- `max_distance` değeri, mesafeyi sınırlamak için kullanılacak maksimum değerdir.

### 4. Rastgele Bir Kelime Seçimi
```python
w1 = random.choice(list(fasttext_model.key_to_index.keys()))
```
- Modeldeki kelimelerden rastgele bir kelime seçer ve `w1` değişkenine atar.

### 5. Kelime Listesi ve Toplam Kelime Sayısı
```python
kelime_listesi = list(fasttext_model.key_to_index.keys())
total_words = len(kelime_listesi)
print(f"Modeldeki toplam kelime sayısı: {total_words}")
print(f"Seçilen gizli kelime: {w1}")
```
- Modeldeki kelimeleri bir listeye dönüştürür ve toplam kelime sayısını hesaplayarak ekrana yazdırır.
- Seçilen gizli kelimeyi kullanıcıya gösterir.

### 6. Oyun Döngüsü
```python
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

    vec1 = fasttext_model[w1]
    vec2 = fasttext_model[w2]

    distance = pythagorean_distance(vec1, vec2)

    scaled_distance = scale_distance(distance, total_words)
    print(f"Seçilen kelime ile girilen kelime ARASINDAKİ KELİME SAYISI: {scaled_distance}")

    if distance <= 0.5:
        print("Tebrikler! Doğru tahmin!")
        break
```
- Kullanıcıdan kelime girişi almak için sonsuz bir döngü oluşturur.
- Kullanıcı `çıkış` komutunu verene kadar döngü devam eder.
- Kullanıcıdan alınan kelimenin modelde olup olmadığını kontrol eder.
- Vektörler arasındaki mesafeyi hesaplar ve mesafeyi ölçeklendirir.
- Kullanıcıya, seçilen kelime ile girilen kelime arasındaki ölçeklendirilmiş mesafeyi gösterir.
- Eğer mesafe belirli bir eşiğin altındaysa, kullanıcıyı tebrik eder.

## Sonuç
Bu kod, Gensim kütüphanesinin FastText modeli ile kelime benzerliklerini kullanarak eğlenceli bir tahmin oyunu sunmaktadır. Kullanıcı, kelime gömme modelinden rastgele seçilen bir kelimeyi tahmin etmeye çalışır ve iki kelime arasındaki mesafeyi hesaplayarak doğru tahmin yapıp yapmadığını öğrenir.
