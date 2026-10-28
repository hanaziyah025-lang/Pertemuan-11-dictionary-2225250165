
def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")


def rata_rata_nilai(data):
    if not data:
        return 0

    total = 0
    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "2225250001": {"nama": "Andi Saputra", "kelas": "3B", "nilai": 85},
    "2225250002": {"nama": "Bunga Lestari", "kelas": "3B", "nilai": 78},
    "2225250003": {"nama": "Citra Amelia", "kelas": "3B", "nilai": 92},
    "2225250004": {"nama": "Dimas Pratama", "kelas": "3B", "nilai": 74},
    "2225250005": {"nama": "Eka Putri", "kelas": "3B", "nilai": 88}
}

# 1. Pencarian mahasiswa yang tersedia
print("=== PENCARIAN MAHASISWA ===")
print(cari_mahasiswa(data_mahasiswa, "2225250003"))

# 2. Pencarian mahasiswa yang tidak tersedia
print(cari_mahasiswa(data_mahasiswa, "2225250099"))

# 3. Memperbarui nilai mahasiswa
data_mahasiswa["2225250002"]["nilai"] = 82
print("\nNilai mahasiswa 2225250002 berhasil diubah menjadi 82.")

# 4. Menambahkan mahasiswa baru
data_mahasiswa["2225250006"] = {
    "nama": "Fajar Ramadhan",
    "kelas": "3B",
    "nilai": 80
}
print("Mahasiswa 2225250006 berhasil ditambahkan.")

# 5. Menampilkan seluruh data menggunakan items()
print("\n=== REKAP DATA MAHASISWA ===")
for nim, data in data_mahasiswa.items():
    print(
        f"NIM: {nim}, Nama: {data['nama']}, "
        f"Kelas: {data['kelas']}, Nilai: {data['nilai']}"
    )

# 6. Menghitung rata-rata nilai kelas
print("\n=== RATA-RATA NILAI KELAS ===")
print(f"Rata-rata nilai: {rata_rata_nilai(data_mahasiswa):.2f}")
