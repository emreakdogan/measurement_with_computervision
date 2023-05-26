# Bilgisayarlı Görü ile Görüntüden Nesnenin Boyutunu Çıkarma ve En Uygun Şekilde Yerleştirme 
## Proje İçeriği
Bu proje, özel olarak boyutunu tespit etmek istediğimiz nesnenin bilgisayarlı görü ile bu proje özelinde YOLO algoritması kullanarak nesne tanıma modeli eğitilmiştir, daha sonra bu tanınan nesnenin kendi boyut çıkartma algoritması ile nesnenin gerçek boyut bilgilerine küçük bir hata payı ile erişme imkanı vermektedir.
Not: Bu proje de özel olarak kargo kutuları tespit edilmiş ve onun boyut bilgileri çıkarılmıştır.
## Kullanım
Bu kodu kullanmak için, app.py dosyasını çalıştırmanız ve yanında bir referans objesi(bu projede 1 Türk Lirası madeni para kullanılmıştır) olmak koşuluyla  fotoğrafını çektiğiniz kargonuzun fotoğrafını base64 formatında göndermeniz yeterli olacaktır. Gönderimden sonra  JSON formatında obje tipleri, güven aralığı ve boyut bilgileri gönderilecektir. 
## Örnek
![Ekran görüntüsü 2023-04-27 190639](https://github.com/emreakdogan/thy_measurement_with_computervision/assets/95315841/7628d98d-999e-4054-8210-d5e81a669bef)

![Ekran görüntüsü 2023-04-26 123113](https://github.com/emreakdogan/thy_measurement_with_computervision/assets/95315841/35c257a3-b14d-4857-84ef-774e2c49cc3d)



