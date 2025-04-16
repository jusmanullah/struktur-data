def bintang_ganjil(n):
    for i in range(n):
        bintang = '*' * (2 * i + 1)
        spasi = ' ' * (n - i - 1)
        print(spasi + bintang + spasi)

# Contoh penggunaan
baris = int(input("Masukkan jumlah baris: "))
bintang_ganjil(baris)