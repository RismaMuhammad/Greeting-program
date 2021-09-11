print('Hello Bro')

waktu=int(input("Masukkan Jam Berapa Sekarang :"))
if waktu >= 1 and waktu < 12:
    print("Selamat Pagi")
elif waktu >= 12 and waktu < 16:
    print("Selamat Siang")
elif waktu >= 16 and waktu < 18:
    print("Selamat Sore")
elif waktu >= 18 and waktu < 24:
    print("Selamat Malam")
else:
    print("Masukkan Waktu Yang Benar")