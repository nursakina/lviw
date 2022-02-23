#OPERATOR ARITMETIKA DAN PERCABGAN 
bil1 = int(input('masukkkan nilai : '))
bil2 = int(input('masukkan nilai = '))
print('kalkulator sederhana')
print('''operator aritmetika 
1.penjumlahan [+]
2.pengurangan [-]
3.pembagian [/]
4.perkalian [*]''')

operator = int(input('masukkkan operator pilihan kita :'))
if operator == 1:
    hasil = bil1 + bil2 
elif operator == 2:
    hasil = bil1 / bil2
elif operator == 3:
    hasil = bil1 - bil2
elif operator == 4:
    hasil = bil1 * bil2

else :
    hasil = 'pilihan tidak tersedia'
print(hasil)



print('-'*100)

n = int(input('masukkkan nilai :'))
n = int(input('masukkan nilai :'))

print('kalkulator sederhana')
print(''' operator aritmetika
1. penjumlahan [+]
2. pengurangan [-]
3. perkalian[*]
4. pembagian [/]
5. perpangkatan [**]
6. sisa bagi [%]
7.pembagian bulat [//]''')

operator = int(input('masukkkan operator pilihan kita :'))
if n == 1 :
    hasil = n + n 
elif n == 2 :
    hasil = n-n
elif n == 3 :
    hasil = n*n
elif n == 4 :
    hasil = n/n
elif n == 5 :
    hasil = n**n
elif n == 6 :
    hasil = n%n
elif n == 7 :
    hasil = n//n
else :
    ('hasil operator tidak ditemukan')
print(hasil)
