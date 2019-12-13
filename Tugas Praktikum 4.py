data = []
no = 0
while(True):
    Nama = input("Nama         : ")
    NIM = input("NIM          : ")
    Tugas = int(input("Nilai Tugas  : "))
    UTS = int(input("Nilai UTS    : "))
    UAS = int(input("Nilai UAS    : "))
    Akhir = (30 * Tugas / 100) + (35 * UTS / 100) + (35 * UAS / 100)
    data.append([Nama, NIM, Tugas, UTS, UAS, Akhir])
    ulangi = input("Tambah data (y/t)? ")
    if ulangi.lower() == "t":
        break

print("\nDaftar Nama\n")
print("=======================================================================================")
print("| No |    Nama    |      NIM      |    Tugas    |    UTS    |    UAS    |    Akhir    |")
print("=======================================================================================")
for x in data:
    no = no+1
    print("|", no, " | {0:7s}    |   {1:11s} | {2:6d}      | {3:5d}     |  {4:4d}     |    {5:4.2f}    |".format(x[0],
        x[1], x[2], x[3], x[4], x[5]))
print("=======================================================================================")
