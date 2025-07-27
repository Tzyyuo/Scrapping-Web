#!/usr/bin/env python3
"""
Script untuk menampilkan kata kunci yang valid untuk pencarian
"""

import pandas as pd
import os

def show_valid_keywords():
    """Tampilkan kata kunci yang valid untuk pencarian"""
    print("🔍 Kata Kunci Valid untuk Pencarian")
    print("=" * 60)
    
    try:
        if os.path.exists('daftar_perusahaan_idx.csv'):
            df = pd.read_csv('daftar_perusahaan_idx.csv')
            
            # Analisis kata kunci berdasarkan nama perusahaan
            keywords = {
                'Perbankan': ['bank', 'bca', 'bri', 'mandiri', 'bni', 'btn', 'perbankan'],
                'Otomotif': ['astra', 'auto', 'otomotif', 'toyota', 'honda'],
                'Telekomunikasi': ['telkom', 'telekomunikasi', 'indosat', 'xl'],
                'Farmasi': ['farmasi', 'farma', 'kimia', 'care', 'medika'],
                'Makanan & Minuman': ['food', 'indofood', 'unilever', 'makanan'],
                'Properti': ['properti', 'land', 'realty', 'estate', 'city'],
                'Pertambangan': ['tambang', 'mineral', 'resources', 'coal'],
                'Energi': ['energi', 'power', 'pln', 'electricity'],
                'Asuransi': ['asuransi', 'insurance'],
                'Keuangan': ['finance', 'leasing', 'multifinance'],
                'Media': ['media', 'broadcasting', 'tv', 'radio'],
                'Tekstil': ['textile', 'garment', 'textil'],
                'Konstruksi': ['cement', 'semen', 'beton'],
                'Kimia': ['chemical', 'kimia', 'polychem'],
                'Ritel': ['retail', 'alfamart', 'indomaret'],
                'Transportasi': ['transport', 'logistik', 'shipping']
            }
            
            print("📋 Kata Kunci Berdasarkan Sektor:")
            for sektor, kata_kunci in keywords.items():
                print(f"\n🏢 {sektor}:")
                for keyword in kata_kunci:
                    print(f"   • {keyword}")
            
            # Tampilkan contoh nama perusahaan yang bisa dicari
            print(f"\n📊 Total Perusahaan di CSV: {len(df)}")
            
            # Contoh nama perusahaan yang bisa dicari
            print("\n🎯 Contoh Nama Perusahaan yang Bisa Dicari:")
            sample_companies = [
                'Astra International Tbk',
                'Bank Central Asia Tbk', 
                'Bank Rakyat Indonesia Tbk',
                'Bank Mandiri Tbk',
                'Telkom Indonesia Tbk',
                'Indofood Sukses Makmur Tbk',
                'Unilever Indonesia Tbk',
                'Kalbe Farma Tbk',
                'Kimia Farma Tbk',
                'Astra Otoparts Tbk',
                'Sumber Alfaria Trijaya Tbk',
                'Alam Sutera Realty Tbk',
                'Agung Podomoro Land Tbk',
                'Bumi Resources Tbk',
                'Aneka Tambang Tbk',
                'Bukit Asam Tbk',
                'Perusahaan Gas Negara Tbk',
                'PLN Tbk',
                'Asuransi Bintang Tbk',
                'BFI Finance Indonesia Tbk',
                'Global Mediacom Tbk',
                'Trisula Textile Industries Tbk',
                'Semen Indonesia Tbk',
                'Polychem Indonesia Tbk',
                'Alfamart Tbk',
                'Indomaret',
                'Blue Bird Tbk',
                'Pelabuhan Indonesia Tbk'
            ]
            
            for company in sample_companies:
                print(f"   • {company}")
            
            print("\n" + "=" * 60)
            print("💡 CARA PENGGUNAAN:")
            print("1. Buka browser: http://localhost:5000")
            print("2. Ketik kata kunci di search bar")
            print("3. Klik tombol 'Cari'")
            print("4. Lihat hasil pencarian")
            print("5. Gunakan filter untuk mencari berdasarkan nama/sektor/sumber")
            
        else:
            print("❌ File daftar_perusahaan_idx.csv tidak ditemukan")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    show_valid_keywords() 