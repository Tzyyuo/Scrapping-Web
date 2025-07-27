import pandas as pd
import numpy as np

def gabungkan_data_improved():
    """
    Menggabungkan data perusahaan dari hasil_scrapping.csv dengan data social media dari sosmed.csv
    dengan penanganan yang lebih cermat untuk perbedaan data
    """
    print("[INFO] Membaca file hasil_scrapping.csv...")
    
    # Baca data perusahaan
    try:
        df_perusahaan = pd.read_csv('hasil_scrapping.csv')
        print(f"[INFO] Berhasil membaca {len(df_perusahaan)} data perusahaan")
    except Exception as e:
        print(f"[ERROR] Gagal membaca hasil_scrapping.csv: {e}")
        return
    
    print("[INFO] Membaca file sosmed.csv...")
    
    # Baca data social media
    try:
        df_sosmed = pd.read_csv('sosmed.csv')
        print(f"[INFO] Berhasil membaca {len(df_sosmed)} data social media")
    except Exception as e:
        print(f"[ERROR] Gagal membaca sosmed.csv: {e}")
        return
    
    # Bersihkan nama perusahaan (hapus spasi di awal/akhir)
    df_perusahaan['nama_clean'] = df_perusahaan['nama'].str.strip()
    df_sosmed['nama_clean'] = df_sosmed['nama'].str.strip()
    
    # Buat set nama perusahaan dari kedua file
    set_perusahaan = set(df_perusahaan['nama_clean'])
    set_sosmed = set(df_sosmed['nama_clean'])
    
    print(f"\n=== ANALISIS DATA ===")
    print(f"Total perusahaan di hasil_scrapping.csv: {len(set_perusahaan)}")
    print(f"Total perusahaan di sosmed.csv: {len(set_sosmed)}")
    
    # Cari perusahaan yang ada di hasil_scrapping tapi tidak di sosmed
    perusahaan_tanpa_sosmed = set_perusahaan - set_sosmed
    print(f"\nPerusahaan yang ADA di hasil_scrapping.csv tapi TIDAK ADA di sosmed.csv: {len(perusahaan_tanpa_sosmed)}")
    
    # Cari perusahaan yang ada di sosmed tapi tidak di hasil_scrapping
    sosmed_tanpa_perusahaan = set_sosmed - set_perusahaan
    print(f"Perusahaan yang ADA di sosmed.csv tapi TIDAK ADA di hasil_scrapping.csv: {len(sosmed_tanpa_perusahaan)}")
    
    # Perusahaan yang ada di kedua file
    perusahaan_umum = set_perusahaan & set_sosmed
    print(f"Perusahaan yang ada di KEDUA file: {len(perusahaan_umum)}")
    
    # Gabungkan data berdasarkan nama perusahaan yang sudah dibersihkan
    print("\n[INFO] Menggabungkan data...")
    
    # Gunakan nama_clean sebagai key untuk merge
    df_gabungan = pd.merge(
        df_perusahaan, 
        df_sosmed[['nama_clean', 'facebook', 'instagram', 'twitter', 'linkedin', 'youtube']], 
        on='nama_clean', 
        how='left'
    )
    
    # Hapus kolom nama_clean yang tidak diperlukan
    df_gabungan = df_gabungan.drop('nama_clean', axis=1)
    
    # Ganti nilai NaN dengan '-'
    kolom_sosmed = ['facebook', 'instagram', 'twitter', 'linkedin', 'youtube']
    for kolom in kolom_sosmed:
        df_gabungan[kolom] = df_gabungan[kolom].fillna('-')
    
    # Simpan hasil gabungan
    output_file = 'data_perusahaan_lengkap.csv'
    df_gabungan.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"\n[SUCCESS] Data berhasil digabungkan dan disimpan ke '{output_file}'")
    print(f"[INFO] Total data: {len(df_gabungan)} perusahaan")
    
    # Tampilkan statistik
    print("\n=== STATISTIK DATA ===")
    print(f"Perusahaan dengan Facebook: {len(df_gabungan[df_gabungan['facebook'] != '-'])}")
    print(f"Perusahaan dengan Instagram: {len(df_gabungan[df_gabungan['instagram'] != '-'])}")
    print(f"Perusahaan dengan Twitter: {len(df_gabungan[df_gabungan['twitter'] != '-'])}")
    print(f"Perusahaan dengan LinkedIn: {len(df_gabungan[df_gabungan['linkedin'] != '-'])}")
    print(f"Perusahaan dengan YouTube: {len(df_gabungan[df_gabungan['youtube'] != '-'])}")
    
    # Tampilkan perusahaan yang tidak memiliki social media
    perusahaan_tanpa_sosmed_list = df_gabungan[df_gabungan['facebook'] == '-'].head(10)['nama'].tolist()
    print(f"\n=== CONTOH PERUSAHAAN TANPA SOCIAL MEDIA ===")
    for i, nama in enumerate(perusahaan_tanpa_sosmed_list):
        print(f"{i+1}. {nama}")
    
    # Tampilkan beberapa contoh data lengkap
    print("\n=== CONTOH DATA LENGKAP ===")
    contoh_data = df_gabungan.head(3)
    for idx, row in contoh_data.iterrows():
        print(f"\nPerusahaan: {row['nama']}")
        print(f"Sektor: {row['sektor']}")
        print(f"Website: {row['website']}")
        print(f"Kontak: {row['kontak']}")
        print(f"Facebook: {row['facebook']}")
        print(f"Instagram: {row['instagram']}")
        print(f"Twitter: {row['twitter']}")
        print(f"LinkedIn: {row['linkedin']}")
        print(f"YouTube: {row['youtube']}")
        print("-" * 50)
    
    # Simpan juga data yang tidak cocok untuk analisis
    if len(perusahaan_tanpa_sosmed) > 0:
        df_tanpa_sosmed = df_perusahaan[df_perusahaan['nama_clean'].isin(perusahaan_tanpa_sosmed)]
        df_tanpa_sosmed = df_tanpa_sosmed.drop('nama_clean', axis=1)
        df_tanpa_sosmed.to_csv('perusahaan_tanpa_sosmed.csv', index=False, encoding='utf-8')
        print(f"\n[INFO] Data perusahaan tanpa social media disimpan ke 'perusahaan_tanpa_sosmed.csv'")
    
    if len(sosmed_tanpa_perusahaan) > 0:
        df_sosmed_terpisah = df_sosmed[df_sosmed['nama_clean'].isin(sosmed_tanpa_perusahaan)]
        df_sosmed_terpisah = df_sosmed_terpisah.drop('nama_clean', axis=1)
        df_sosmed_terpisah.to_csv('sosmed_tanpa_perusahaan.csv', index=False, encoding='utf-8')
        print(f"[INFO] Data social media tanpa perusahaan disimpan ke 'sosmed_tanpa_perusahaan.csv'")
    
    return df_gabungan

if __name__ == "__main__":
    gabungkan_data_improved() 