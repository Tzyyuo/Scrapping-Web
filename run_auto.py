#!/usr/bin/env python3
"""
Script otomatis untuk menjalankan Mass Data Collector
Tanpa konfirmasi user - langsung jalankan
"""

import sys
import os
from datetime import datetime

# Import konfigurasi dan collector
try:
    import config
    from mass_data_collector import MassDataCollector
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    sys.exit(1)

def main():
    """Main function - jalankan otomatis"""
    print("🚀 MASS DATA COLLECTOR - AUTO MODE")
    print("=" * 50)
    print(f"⏰ Waktu mulai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Inisialisasi collector
        collector = MassDataCollector()
        
        # Konfigurasi berdasarkan config.py
        idx_limit = config.IDX_SETTINGS['limit'] if config.IDX_SETTINGS['enabled'] else 0
        directory_pages = config.DIRECTORY_SETTINGS['pages_per_directory'] if config.DIRECTORY_SETTINGS['enabled'] else 0
        google_maps_queries = config.GOOGLE_MAPS_SETTINGS['queries'] if config.GOOGLE_MAPS_SETTINGS['enabled'] else None
        
        print(f"📊 Konfigurasi:")
        print(f"   • IDX Companies: {idx_limit}")
        print(f"   • Directory Pages: {directory_pages}")
        print(f"   • Google Maps Queries: {len(google_maps_queries) if google_maps_queries else 0}")
        
        # Jalankan pengumpulan data
        data = collector.run_mass_collection(
            idx_limit=idx_limit,
            directory_pages=directory_pages,
            google_maps_queries=google_maps_queries
        )
        
        print(f"\n🎉 PENGUMPULAN DATA SELESAI!")
        print(f"📊 Total data yang dikumpulkan: {len(data)} perusahaan")
        print(f"⏰ Waktu selesai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        if data:
            print(f"✅ Proses berhasil! {len(data)} data perusahaan telah dikumpulkan.")
            print("📁 Cek file Excel yang dihasilkan untuk melihat hasilnya.")
        else:
            print("❌ Tidak ada data yang berhasil dikumpulkan.")
            
    except KeyboardInterrupt:
        print("\n⚠️ Proses dihentikan oleh user")
    except Exception as e:
        print(f"\n❌ Error selama pengumpulan data: {str(e)}")

if __name__ == "__main__":
    main() 