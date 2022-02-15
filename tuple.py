# contoh sederhana pembuatan Tuple pada Python
tup1 = ("Andi", "Budi", "Caca", 1996, 2000)
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d","e"

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# update nilai dalam tuple
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Aksi seperti dibawah ini tidak bisa dilakukan pada tuple python
# Karena memang nilai pada tuple python tidak bisa diubah
# tup1[0] = 100;

# Jadi, buatlah tuple baru sebagai berikut
tup3 = tup1 + tup2
print(tup3)

# menghapus nilai dalam Tuple Python
tup = ("Andi", "Budi", "Caca", 1996, 2000)
print(tup)

# hapus Tuple dengan statements del
del tup

# lalu buat kembali tuple yang baru dengan element yang diinginkan
tup = ("Bahasa", "Literasi", 2023)
print("Setelah menghapus tuple : ", tup)