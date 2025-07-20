#!/usr/bin/env python3
"""
Script sederhana untuk mengecek aplikasi web
"""

import requests

def check_web_app():
    print("🔍 Mengecek aplikasi web...")
    print("=" * 50)
    
    try:
        # Cek apakah aplikasi berjalan
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("✅ Aplikasi web berjalan di http://localhost:5000")
        else:
            print(f"❌ Aplikasi web error: {response.status_code}")
            return
        
        # Test pencarian
        print("\n🔍 Testing pencarian...")
        
        # Test pencarian farmasi
        response = requests.get('http://localhost:5000/search?q=farmasi&filter=all', timeout=5)
        if response.status_code == 200:
            data = response.json()
            companies = data.get('companies', [])
            print(f"✅ Pencarian 'farmasi': {len(companies)} hasil")
            for company in companies[:3]:
                print(f"   - {company['nama']} ({company['sektor']})")
        
        # Test pencarian perbankan
        response = requests.get('http://localhost:5000/search?q=perbankan&filter=all', timeout=5)
        if response.status_code == 200:
            data = response.json()
            companies = data.get('companies', [])
            print(f"✅ Pencarian 'perbankan': {len(companies)} hasil")
            for company in companies[:3]:
                print(f"   - {company['nama']} ({company['sektor']})")
        
        print("\n" + "=" * 50)
        print("🌐 Buka browser dan akses: http://localhost:5000")
        print("📝 Ketik kata kunci di search bar dan klik 'Cari'")
        print("💡 Contoh kata kunci: farmasi, perbankan, otomotif")
        
    except requests.exceptions.ConnectionError:
        print("❌ Aplikasi web tidak dapat diakses")
        print("💡 Jalankan: python web_app.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_web_app() 