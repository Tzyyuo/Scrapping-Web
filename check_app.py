#!/usr/bin/env python3
"""
Script untuk mengecek status aplikasi web
"""

import requests
import time

def check_app_status():
    """Cek status aplikasi web"""
    try:
        # Coba akses aplikasi
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("✅ Aplikasi web berjalan dengan baik!")
            print("🌐 URL: http://localhost:5000")
            return True
        else:
            print(f"❌ Aplikasi web error dengan status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Aplikasi web tidak dapat diakses")
        print("💡 Pastikan aplikasi web sudah dijalankan dengan: python web_app.py")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_search():
    """Test pencarian data"""
    try:
        # Test pencarian farmasi
        response = requests.get('http://localhost:5000/search?q=farmasi&filter=all', timeout=5)
        if response.status_code == 200:
            data = response.json()
            companies = data.get('companies', [])
            print(f"✅ Pencarian 'farmasi' berhasil! Ditemukan {len(companies)} perusahaan:")
            
            for i, company in enumerate(companies[:5], 1):  # Tampilkan 5 pertama
                print(f"   {i}. {company['nama']} - {company['sektor']}")
            
            if len(companies) > 5:
                print(f"   ... dan {len(companies) - 5} perusahaan lainnya")
            
            return True
        else:
            print(f"❌ Error dalam pencarian: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error dalam test pencarian: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Mengecek status aplikasi web...")
    print("=" * 50)
    
    # Cek status aplikasi
    if check_app_status():
        print("\n🔍 Testing pencarian data...")
        test_search()
    
    print("\n" + "=" * 50)
    print("📝 Instruksi:")
    print("1. Buka browser dan akses: http://localhost:5000")
    print("2. Ketik 'farmasi' di search bar")
    print("3. Klik tombol 'Cari'")
    print("4. Anda akan melihat daftar perusahaan farmasi")
    print("5. Klik 'Export Excel' untuk download data") 