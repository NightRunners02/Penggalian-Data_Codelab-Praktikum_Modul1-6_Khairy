import statistics

matkul_nilai = (
    {"Matematika": 80, "Fisika": 75, "Kimia": "", "Biologi": 85, "Informatika": 90,
     "Sejarah": 70, "Ekonomi": "", "Geografi": 88, "Sosiologi": 92, "Statistika": ""}
)

matkul_nilai_bersih = {k: v for k, v in matkul_nilai.items() if isinstance(v, (int, float))}
print("Data setelah menghapus entri kosong:", matkul_nilai_bersih)

jumlah_tersisa = len(matkul_nilai_bersih)
print("Jumlah entri setelah penghapusan:", jumlah_tersisa)

matkul_sorted = dict(sorted(matkul_nilai_bersih.items(), key=lambda x: x[1]))
print("Data setelah sorting ascending:", matkul_sorted)

matkul_tertinggi = max(matkul_nilai_bersih, key=matkul_nilai_bersih.get)
print("Mata kuliah dengan nilai tertinggi:", matkul_tertinggi)

rata_rata = statistics.mean(matkul_nilai_bersih.values())
print("Rata-rata nilai mata kuliah:", rata_rata)