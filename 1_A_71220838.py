print ('======= Program Manipulasi String =======')
print ('Pilihan Menu :')
print ('1. Hitung Kata')
print ('2. Ubah Kata')
pilihan = int(input('Pilihan Anda: '))
kata = input('Masukkan sebuah kalimat/kata: ')
def hitung_kata():
    a = input('Masukkan kata yang ingin dihitung : ')
    ax = kata.count(a)
    print ('Terdapat sebanyak',ax,'kata',a,'di dalam kalimat')
def ubah_kata():
    b = input('Masukkan kata yang ingin di ubah: ')
    bx = input('Masukkan kata pengganti: ')
    by = kata.replace(b,bx)
    print ('String berhasil diubah menjadi: ',by)
if pilihan == 1:
    hitung_kata()
elif pilihan == 2:
    ubah_kata()
else:
    print ('Pilihan yang anda input tidak terdaftar di daftar pilihan')