#kullanıcıya adını ve dogum tarihini sorunuz.
#girilen dogum tarihine göre yasını hesaplayınız.

ad = input("adiniz: ")                   #string türünde veri
dogum_yil = int(input("Dogum yılı :"))   #int türünde veri 

yas = 2024 - dogum_yil #yaş hesaplama

print("Merhaba" ,ad,"yaşınız",yas) #çıktı