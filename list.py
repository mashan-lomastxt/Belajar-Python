# contoh sederhana membuat List dalam python
list1 = ["Struktur Data", "Statistika", "Keamanan Jaringan", 1993, 2021]
list2 = [1,2,3,4,5]
list3 = ["a","b","c","d","e"]

print("list1[0]: ", list1[0])
print("list1[1:5]: ", list1[1:5])

list = ["Struktur Data", "Statistika", "Keamanan Jaringan", 1993, 2021]
print("Nilai ada pada index ke-2: ", list[2])

# update nilai dalam list
list[1] = 2022
print("Nilai baru pada index 1: ", list[1])

# hapus nilai dalam list
list = ["Struktur Data", "Statistika", "Keamanan Jaringan", 1993, 2021]
print(list)
del list[1]
print("Setelah dihapus nilai pada index 1 : ", list)