# scrapping-webs
# IDX Company Data Web Application

Aplikasi web untuk mencari dan menampilkan data perusahaan yang terdaftar di Bursa Efek Indonesia (IDX). Aplikasi ini menyediakan fitur pencarian, filter, dan ekspor data ke Excel.

## 🚀 Fitur Utama

- **Pencarian Perusahaan**: Cari berdasarkan nama, sektor, atau semua kategori
- **Filter Data**: Filter berdasarkan nama, sektor, atau sumber data
- **Tampilan Detail**: Informasi lengkap perusahaan termasuk website, social media, dan kontak
- **Ekspor Excel**: Export hasil pencarian ke file Excel
- **Statistik**: Tampilan statistik sektor bisnis

## 📋 Prerequisites

Sebelum menjalankan aplikasi, pastikan Anda telah menginstall:

- Python 3.7 atau lebih baru
- pip (Python package manager)

## 🛠️ Installation

### 1. Clone Repository
```bash
git clone <URL_REPOSITORY_ANDA>
cd Scrapping
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Jika file `requirements.txt` tidak ada, install dependencies secara manual:
```bash
pip install flask pandas openpyxl requests selenium
```

### 3. Download ChromeDriver
Pastikan ChromeDriver sudah ada di folder `Scrapping/` atau download dari:
https://chromedriver.chromium.org/

## 🚀 Cara Menjalankan Aplikasi

### Langkah 1: Masuk ke Directory
```bash
cd Scrapping
```

### Langkah 2: Jalankan Web Application
```bash
python web_app_fixed.py
```

### Langkah 3: Buka Browser
Buka browser dan akses:
```
http://localhost:5000
```

## 📖 Cara Penggunaan

### 1. Halaman Utama
- Aplikasi akan menampilkan halaman utama dengan search bar
- Klik "Tampilkan Semua" untuk melihat semua 941 perusahaan

### 2. Pencarian Perusahaan
- Masukkan kata kunci di search bar
- Pilih filter: "Semua", "Nama", atau "Sektor"
- Klik tombol "Cari" atau tekan Enter

### 3. Kata Kunci Pencarian yang Valid
Berikut beberapa kata kunci yang bisa digunakan:

**Sektor Perbankan:**
- Bank, Perbankan, BCA, BNI, BRI, Mandiri

**Sektor Farmasi:**
- Farmasi, Kimia, Kalbe, Dexa

**Sektor Otomotif:**
- Otomotif, Astra, Toyota, Honda

**Sektor Properti:**
- Properti, Real Estate, Property

**Sektor Media:**
- Media, Telekomunikasi, Telkom

**Sektor Energi:**
- Energi, Pertambangan, Oil & Gas

**Sektor Makanan & Minuman:**
- Makanan, Minuman, Food & Beverage

### 4. Melihat Detail Perusahaan
- Klik pada nama perusahaan untuk melihat detail lengkap
- Informasi yang ditampilkan:
  - Nama perusahaan
  - Sektor bisnis
  - Website (jika tersedia)
  - Social media (jika tersedia)
  - Kontak (jika tersedia)

### 5. Export ke Excel
- Setelah melakukan pencarian
- Klik tombol "Export ke Excel"
- File akan otomatis terdownload

## 📊 Statistik Data

Aplikasi memuat 941 perusahaan dari IDX dengan distribusi sektor:
- Lainnya: 922 perusahaan
- Perbankan: 9 perusahaan
- Properti: 2 perusahaan
- Media: 2 perusahaan
- Energi: 1 perusahaan
- Otomotif: 1 perusahaan
- Farmasi: 1 perusahaan
- Pertambangan: 1 perusahaan
- Makanan & Minuman: 1 perusahaan
- Telekomunikasi: 1 perusahaan

## 🔧 Troubleshooting

### Error: "No such file or directory"
```bash
# Pastikan Anda berada di directory yang benar
cd Scrapping
ls  # untuk melihat file yang ada
```

### Error: "Module not found"
```bash
# Install ulang dependencies
pip install flask pandas openpyxl requests selenium
```

### Error: ChromeDriver not found
- Download ChromeDriver dari https://chromedriver.chromium.org/
- Letakkan file `chromedriver.exe` di folder `Scrapping/`

### Aplikasi tidak bisa diakses
- Pastikan port 5000 tidak digunakan aplikasi lain
- Coba akses http://127.0.0.1:5000 sebagai alternatif

## 📁 Struktur File

```
Scrapping/
├── web_app_fixed.py          # Aplikasi web utama
├── daftar_perusahaan_idx.csv # Data 941 perusahaan IDX
├── templates/
│   └── index.html           # Template halaman web
├── requirements.txt          # Dependencies Python
├── chromedriver.exe         # ChromeDriver untuk scraping
└── README.md               # File ini
```

## 🎯 Contoh Penggunaan

### Mencari Bank
1. Masukkan "Bank" di search bar
2. Pilih filter "Semua"
3. Klik "Cari"
4. Hasil: 9 perusahaan perbankan

### Mencari Farmasi
1. Masukkan "Farmasi" di search bar
2. Pilih filter "Sektor"
3. Klik "Cari"
4. Hasil: 1 perusahaan farmasi

### Export Data
1. Lakukan pencarian
2. Klik "Export ke Excel"
3. File Excel akan terdownload dengan nama `hasil_pencarian.xlsx`

## 📞 Support

Jika mengalami masalah, pastikan:
1. Python dan dependencies terinstall dengan benar
2. File `daftar_perusahaan_idx.csv` ada di folder yang sama
3. Port 5000 tidak digunakan aplikasi lain
4. Browser mendukung JavaScript

## 🔄 Update Data

Untuk memperbarui data perusahaan:
1. Ganti file `daftar_perusahaan_idx.csv` dengan data terbaru
2. Restart aplikasi web
3. Data akan otomatis terupdate

---

**Note**: Aplikasi ini menggunakan data dari Bursa Efek Indonesia (IDX) dan hanya untuk tujuan informasi. Pastikan untuk memverifikasi data sebelum digunakan untuk keputusan bisnis.
