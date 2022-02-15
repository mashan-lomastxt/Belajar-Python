# Latihan konversi satuan
# Program konversi celcius ke satuan lain

print("\nProgram konversi satuan temperature\n")

# Celcius
celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu adalah", celcius, "derajat celcius")

# Reamur
reamur = 4/5 * celcius
print("Suhu dalam reamur adalah", reamur, "derajat reamur")

# Fahrenheit
fahrenheit = 9/5 * celcius + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "derajat fahrenheit")

# Kelvin
kelvin = celcius + 273.15
print("Suhu dalam kelvin adalah", kelvin, "derajat kelvin")