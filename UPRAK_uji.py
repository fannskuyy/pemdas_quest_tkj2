print("============")
print("bangun ruang")
print("============")

print("\n1,balok")

panjang = int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi = int(input("masukan nilai tinggi: "))
volume_balok = panjang * lebar * tinggi 
print("volume balok adalah:", volume_balok)

print("\n2,limas")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
volume_l= alas * tinggi 
print("volume limas adalah: ", volume_l)

print("\n3,tabung")

r =int(input("masukan jari jari: "))
t =int(input("masukan nilai tinngi: "))
keliling = 2 * 3,14 * r
luas_tb = 3,14 * r * r
print("keliling =" ,keliling)
print("luas =" ,luas_tb)

print("\n4, dolar")

kursdolar = 14000
rupiah = float(input("masukan uang rupiah anda: "))
rupTodol = rupiah / kursdolar
doldecimal = round(rupTodol, 2)
print("rp.",rupiah, "==> US$", doldecimal)