import time; # digunakan untuk mengimport modul time
import calendar; # digunakan untuk mengimport modul calendar

ticks = time.time()
print("Berjalan sejak 12:00am, January 1, 1970", ticks)

localtime = time.localtime(time.time())
print("Waktu lokal saat ini :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print("Waktu lokal saat ini :", localtime)

cal = calendar.month(2022, 2)
print("Dibawah ini adalah kalender:")
print(cal)