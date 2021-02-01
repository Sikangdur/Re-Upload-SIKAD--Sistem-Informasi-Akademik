   #soal 1

print("Fiture Pengisian Rancangan Studi")
nim = input("Masukan Nim Anda :")

a= nim[5:7]
if (a=="20"):
  max_sks = 20
  print("tahun Pertama anda bisa  bisa mengambil paling banyak ", max_sks )
elif (a=="19"):
  max_sks = 22
  print("tahun kedua anda  bisa mengambil paling banyak ", max_sks )
elif (a=="18"):
  max_sks = 24
  print( "tahun ketiga anda  bisa mengambil paling banyak ", max_sks )
elif (a=="17"):
  max_sks = 26
  print("tahun keempat anda   bisa mengambil paling banyak ", max_sks )
else:
  print("NIM TIDAK VALID")
  exit()
jumlah_sks=0
while True:
  print("Jumlah SKS yang diambil", jumlah_sks)
  matkul=input("Masukkan nama mata kuliah yang diambil atau X untuk selesai:")

  if (matkul == "x" or matkul =="X"):
    print("Pengisian Rencana Studi selesai.")

  sks=int(input("Masukkan beban SKS mata kuliah tersebut:"))
  jumlah_sks+=sks
  if (jumlah_sks == sks):
    print("Pengisian Rencana Studi selesai.")
  else:
      matkul_sks = int(input("Masukkan beban SKS mata kuliah tersebut : "))
      jumlah_sks += matkul_sks
      if jumlah_sks > matkul_sks:
                print("Jumlah SKS melebihi SKS maksimal. Pengisian rencana studi selesai.")
                status = "x"
  exit()
