#Membuat Program Menghitung Bangun Ruang Balok dan Kubus
print("Membuat Program Menghitung Bangun Ruang Balok dan Kubus")



#Menghitung Luas Permukaan dan Volumme Kubus
print("Menghitung Luas Permukaan dan Volume Kubus")

r = int(input("Masukkan rusuknya = "))

Luas = 6*r*r
Volume = r*r*r

print("Luas permukaan kubus adalah", Luas)
print("Volume kubus adalah", Volume)



#Menghitung Luas Permukaan dan Volume Balok
print("Menghitung Luas Permukaan dan Volume Balok")

P = int(input("Masukkan panjang = "))
L = int(input("Masukkan lebar = "))
T = int(input("Masukkan tinggi = "))

Luas = 2*(P*L)+(P*T)+(L*T)
Volume = P*L*T

print("Luas permukaan balok adalah", Luas)
print("Volume balok adalah", Volume)