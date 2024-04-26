# input dari user

coba = input("masukkan nilai")
print("coba : ", "tipe datanya :", type(coba))

# aritmatika 
x = 10
y = 2

# penjumlahan +
hasil = x + y 
print(x, '+', y, '=', hasil)

# penguramgam -
hasil = x - y
print(x, '-', y, '=', hasil)

# perkalian *
hasil = x * y
print(x, '*', y,'=', hasil)

# pembagian /
hasil = x / y
print(x, '/', y, '=', hasil)

#exponen (perpangkatan) **
hasil = x ** y
print(x, '**', y, '=', hasil)

#modulus (sisa bagi) %
hasil = x % y
print(x, '%', y, '=', hasil)

# floar division (pembulatan kebawah) //
hasil = x // y
print(x, '//', y, '=', hasil)

# aritmatika prioritas
# () , exponen ** , perkalian / , penjumlahan +
x = 3
y = 4
z = 5
hasil = x ** y * z + x / y - z % x // y
print(x, '**', y, '*', z, '+', x, '/', y, '-', z, '%', x, '//', y, '=', hasil) 
 



