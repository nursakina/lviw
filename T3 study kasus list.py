barang = []

menu = 0

while menu !=7 :
    print('''
    1. menambahkan
    2. menghapus
    3. mengedit
    4. menampilkan
    5. mencari barang
    6. mencari index
    7. keluar
    ''')
    
    menu = int(input('masukkan operator anda :'))

    if menu == 1:
        while True :
            lanjut = input("masukkan barang : ")
            barang.append(lanjut)

            print("barang sekarang : ",barang)

            stop =input("ketik y jika ingin berhenti : ")
            if stop == "y" :
                break

    elif menu == 2 :
        while True :
            item = int(input("masukkan index yang akan kita hapus :"))

            if item >= len(barang) :
                print("index tidak ditemukan")

            else :
                print(barang.pop(item))

            print("barang sekarang : ",barang)

            stop =input("ketik y jika ingin berhenti : ")
            if stop == "y" :
                break
    
    elif menu == 3 :
        while True :
            item = int(input("masukkan index yang akan diedit :"))

            if item >= len(barang) :
                print("index tidak ditemukan")

            else :
                barang[item] = input("masukkan barang baru : ")

            print("barang sekarang : ",barang)

            stop =input("ketik y jika ingin berhenti : ")
            if stop == "y" :
                break
    
    elif menu == 4 :
        for i in range(len(barang)) :
            print("barang yang tersedia",barang[i])


    elif menu == 5 :
        item = input("masukkan barang yang dicari : ")
       
        if item in barang :
            print("barang ada")

        else :
            print("barang tidak ada")

    
    elif menu == 6 :
        item = input ("masukkan nama barang : ")
         
        if item in barang : 
            print(item, "berada pada index ke- ",barang.index(item))

        else :
            print("barang tidak ditemukan ")

    elif menu == 7 :
        print("periksa kembali inputan anda")

    