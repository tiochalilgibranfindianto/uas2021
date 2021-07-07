# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:47:35 2021

@author: UAS 2021 | Tio Chalil Gibran Findianto_20083000152_2E
"""
import datetime
from time import process_time_ns

x = datetime.datetime.now()
ulang="y"
while ulang=="y" or ulang =="Y":
    print("========================================================")
    print("           PERHITUNGAN GAJI KARYAWAN CV. LOGOS   ")
    print("              Tanggal : ",x.strftime("%x"))
    print("========================================================")

    #Input
    golongan = ['1','2','3']
    gajipokok = ['2500000','4500000','6500000']

    nama = input("Nama                    = ")
    g= input("Golongan                = ")
    gol = int(g)
    if gol == 1 :
        idx = 0
        tunjangan = 0.01
    elif gol == 2:
        idx = 1
        tunjangan = 0.03
    elif gol == 3:
        idx = 2
        tunjangan = 0.05
    else :
        print("Tidak ada Golongan lain, Coba lagi kembali Golongan dengan Benar")

    print("LAKI-LAKI atau PEREMPUAN")
    jenis_kelamin = input("Jenis Kelamin           = ")
    
    print ("KAWIN atau BELUM")
    status_kawin = input("Status Kawin            = ")

    print ("YA atau TIDAK")
    status_anak = input("Apakah punya Anak       = ")

    #istri
    if jenis_kelamin == "LAKI-LAKI" or "Laki-laki" or "laki-laki" and status_kawin == "KAWIN" or "Kawin" or "kawin":
        tunjanganistri = int(gajipokok[idx]) * tunjangan
    else :
        tunjanganistri = 0
    #Anak
    if status_kawin == "KAWIN" or "Kawin" or "kawin" and status_anak == "YA" or "Ya" or "ya":
        tunjangananak = int(gajipokok[idx]) * 0.02
    else :
        tunjangananak = 0
    gajibruto = int(gajipokok[idx]) + int(tunjanganistri) + int(tunjangananak)
    biayajabatan = int(gajibruto) * 0.05
    iuran_pensiun = 15500
    iuran_organisasi = 3500
    GajiNetto = int(gajibruto) - int(iuran_organisasi) - int(iuran_pensiun)
    
    #Output
    print("========================================================")
    print("                        SLIP GAJI                  ")
    print("               Tanggal : ",x.strftime("%x"))
    print("========================================================")

    print("Nama                  = " + nama)
    print("Golongan              = " + str(gol))
    print("jenis Kelamin         = " + jenis_kelamin)
    print("Staus Kawin           = " + status_kawin)
    print("Gaji Pokok            = Rp. " + gajipokok[idx])
    print("Tunjangan Istri       = Rp. " + str(tunjanganistri))
    print("Tunjangan Anak        = Rp. " + str(tunjangananak))
    print(">>Gaji Bruto          = Rp. " + str(gajibruto))
    print("--------------------------------------------------------")
    print("Biaya Jabatan         = Rp. " + str(biayajabatan))
    print("Iuran Pensiun         = Rp. " + str(iuran_pensiun))
    print("Iuran Organisasi      = Rp. " + str(iuran_organisasi))
    print(">>Gaji Netto          = Rp. " + str(GajiNetto))
    
    #Ulangi
    ulang = input(" Ulangi Program Gajian? y/t = ")
    if ulang=="t" or ulang=="T":
        break
