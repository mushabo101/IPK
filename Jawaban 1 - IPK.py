#list untuk menyimpan setiap input
NIM = []
Nama = []
Alamat = []
AsalSekolah = []
KodeProdi = []
IPKAwal = []
Nilai_UTS_UAS_TM = []
NilaiIPS = []
IPKAkhir = []
Beasiswa = []
u = []
v = []
x = int(input('Masukkan Jumlah yang ingin diinput : ')) #variabel jumlah yang ingin di input
for i in range(1,x+1): # perulangan sebanyak input (x)
    a = int(input('Masukkan NIM : ')) #input NIM di terminal
    b = input('Masukkan Nama : ') #input Nama di terminal
    c = input('Masukkan Alamat : ') #input Alamat di terminal
    d = input('Masukkan Asal Sekolah : ') #input Asal Sekolah di terminal
    e = input('Kode Prodi : ') #input Kode Prodi di terminal
    f = int(input('Nilai IPK Awal : ')) #input IPK Awal di terminal
    g = list(map(int,input('masukkan nilai UTS,UAS,TM :').split(','))) #input Nilai UTS,UAS,TM di terminal
    print("--------------------------------------------------")
    h= g[0]*0.3+g[1]*0.4+g[2]*0.3 #menghitung Nilai IPS
    j = (f+h)/2 #menghitung Nilai IPK akhir


#Statment untuk menentukan beasiswa berdasarkan prodi TI dan SI
    if e == 'TI' or e == 'SI' and j > 75 and j < 85:
        Bea = 'Beasiswa 20%'
    elif e == 'TI' or e == 'SI' and j > 85 and j < 100:
        Bea ='Beasiswa 30%'
#Statment untuk menentukan beasiswa berdasarkan prodi DKV
    elif e == 'DKV' and j > 75 and j < 85:
        Bea ='Beasiswa 25%'

    elif e == 'DKV' and j > 85 and j < 100:
        Bea ='Beasiswa 35%'
#Statment bila semua tidak terpenuhi
    else :
        Bea = 'Tidak terpenuhi'

#menambahkan hasil input dan perhitungan ke list (u)    
    u.append(a)
    u.append(b)
    u.append(c)
    u.append(d)
    u.append(e)
    u.append(f)
    u.append(g)
    u.append(h)
    u.append(j)
    u.append(Bea)
    v.append(u)

#masih kesulitan untuk menampilkan hasil di terminal
for j in range(len(v)):
    for k in range(10):
        print('NIM Adalah',v[j][k])
        print('Nama Adalah',v[j][k])
        print('Alamat Adalah',v[j][k])
        print('Asal Sekolah Adalah',v[j][k])
        print('Kode Prodi Adalah',v[j][k])
        print('IPK Awal Adalah',v[j][k])
        print('Nilai UTS UAS TM',v[j][k])
        print('Nilai IPS',v[j][k])
        print('IPK AKHIR',v[j][k])
        print('Keterangan : ',v[j][k])
