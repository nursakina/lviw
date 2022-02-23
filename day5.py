nama = "sakina"
nim = "D0221334"
gaji_pokok = 1000000
gaji_lembur_per_jam = 5000
lama_lembur = 11
pajak = 10/100
total_gaji_lembur = gaji_lembur_per_jam * lama_lembur
total_pajak1 = gaji_pokok*pajak
total_pajak2 = total_gaji_lembur*pajak
gaji_kotor = gaji_pokok - total_pajak1
gaji_kotor2 = total_gaji_lembur - total_pajak2
gaji_bersih = gaji_kotor+ gaji_kotor2



print("nama\t:", nama, nim)
print("gaji pokok : ", gaji_pokok)
print("total pajak gaji bersih : ", total_pajak1)
print("total pajak gaji lembur : ", total_pajak2)
print("total gaji kotor :", gaji_kotor)
print("total gaji lembur : ", total_gaji_lembur)
print("Gaji bersih adalah : ",gaji_bersih)
