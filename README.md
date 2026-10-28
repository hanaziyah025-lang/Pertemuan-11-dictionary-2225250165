
# Pertemuan 11 - Dictionary/Map

**Nama:** Hana Karimah Ghoziyah  
**NIM:** 2225250165  
**Kelas:** 3B

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value untuk menyimpan, mengakses, dan mengelola data mahasiswa.

## Struktur Data

Program menggunakan dictionary untuk menyimpan data mahasiswa. Key utama berupa NIM mahasiswa, sedangkan value berupa dictionary yang berisi nama dan nilai mahasiswa.

Contoh:
- A001: nama Ayu, nilai 85
- A002: nama Budi, nilai 78

NIM digunakan sebagai key utama agar data setiap mahasiswa mudah dicari.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal VS Code:

```bash
python3 praktik/data_mahasiswa.py
```

Jika perintah `python3` tidak bisa digunakan di Windows, coba:

```powershell
python praktik/data_mahasiswa.py
```

## Test Case

| No. | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Mencari NIM A001 | Data Ayu ditemukan | Data Ayu ditemukan | Berhasil |
| 2 | Mencari NIM A002 | Data Budi ditemukan | Data Budi ditemukan | Berhasil |
| 3 | Mencari NIM A003 | Data tidak ditemukan | Data tidak ditemukan | Berhasil |
| 4 | Mengakses key yang tidak tersedia menggunakan `get()` | Mengembalikan pesan default | Pesan default ditampilkan | Berhasil |

## Refleksi

Kesalahan yang dapat terjadi adalah mengakses key yang tidak tersedia secara langsung, misalnya `data["kelas"]`, sehingga program menghasilkan `KeyError`. Kesalahan ini dapat diperbaiki dengan memeriksa keberadaan key menggunakan operator `in` atau menggunakan `data.get("kelas", "Belum ada")` agar program menampilkan nilai default ketika key tidak ditemukan.
