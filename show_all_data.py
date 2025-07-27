#!/usr/bin/env python3
"""
Script untuk menampilkan semua data perusahaan dari CSV IDX
"""

import pandas as pd
import os

def show_all_company_data():
    """Tampilkan semua data perusahaan dari CSV IDX"""
    print("📊 Menampilkan semua data perusahaan dari CSV IDX...")
    print("=" * 80)
    
    try:
        if os.path.exists('daftar_perusahaan_idx.csv'):
            df = pd.read_csv('daftar_perusahaan_idx.csv')
            print(f"✅ Total perusahaan di CSV: {len(df)}")
            
            # Tampilkan statistik sektor
            print("\n📈 Statistik Sektor Bisnis:")
            sector_counts = df['Sektor Bisnis'].value_counts()
            for sector, count in sector_counts.head(10).items():
                print(f"   {sector}: {count} perusahaan")
            
            # Tampilkan contoh perusahaan farmasi
            print("\n💊 Contoh Perusahaan Farmasi:")
            farmasi_companies = df[df['Sektor Bisnis'].str.contains('Farmasi', case=False, na=False)]
            for idx, row in farmasi_companies.head(5).iterrows():
                nama = row['Nama Perusahaan']
                if 'BEI:' in nama:
                    nama = nama.split('BEI:')[1].strip()
                print(f"   - {nama}")
            
            # Tampilkan contoh perusahaan perbankan
            print("\n🏦 Contoh Perusahaan Perbankan:")
            bank_companies = df[df['Sektor Bisnis'].str.contains('Bank', case=False, na=False)]
            for idx, row in bank_companies.head(5).iterrows():
                nama = row['Nama Perusahaan']
                if 'BEI:' in nama:
                    nama = nama.split('BEI:')[1].strip()
                print(f"   - {nama}")
            
            # Tampilkan contoh perusahaan otomotif
            print("\n🚗 Contoh Perusahaan Otomotif:")
            auto_companies = df[df['Sektor Bisnis'].str.contains('Otomotif', case=False, na=False)]
            for idx, row in auto_companies.head(5).iterrows():
                nama = row['Nama Perusahaan']
                if 'BEI:' in nama:
                    nama = nama.split('BEI:')[1].strip()
                print(f"   - {nama}")
            
            print("\n" + "=" * 80)
            print("🎯 Kata Kunci untuk Pencarian di Aplikasi Web:")
            print("   - 'farmasi' → Perusahaan farmasi")
            print("   - 'bank' → Perusahaan perbankan")
            print("   - 'otomotif' → Perusahaan otomotif")
            print("   - 'telekomunikasi' → Perusahaan telekomunikasi")
            print("   - 'makanan' → Perusahaan makanan & minuman")
            print("   - 'properti' → Perusahaan properti")
            print("   - 'energi' → Perusahaan energi")
            print("   - 'pertambangan' → Perusahaan pertambangan")
            
        else:
            print("❌ File daftar_perusahaan_idx.csv tidak ditemukan")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    show_all_company_data() 