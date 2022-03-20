#membuat dictionary dan mengisi value/nilai ke dalamnya
identitas = {'nama' : 'nursakina','umur' : '19',  'alamat' :'malunda'}

#Meanmapilkan dictionary dengan perulangan
for i in identitas :
    print(i,":", identitas[i])


#mengupdate salah satu nilai/value dalam dictionary
identitas ['nama'] = 'sakina'
print(identitas)

#menghapus salah satu nilai/value dalam dictionary
identitas.pop ('umur')
print(identitas)

#menambahkan salah satu nilai/value kedalam dictionary
identitas ['hobi'] = 'ngemil'
print(identitas)