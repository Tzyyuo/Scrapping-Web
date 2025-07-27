#!/usr/bin/env python3
"""
Script sederhana untuk menjalankan Mass Data Collector
Penggunaan: python run_mass_collection.py
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
    print("📋 Pastikan file config.py dan mass_data_collector.py ada di folder yang sama")
    sys.exit(1)

def print_banner():
    """Print banner aplikasi"""
    print("=" * 60)
    print("🚀 MASS DATA COLLECTOR - Pengumpul Data Perusahaan Otomatis")
    print("=" * 60)
    print("📊 Mengumpulkan data dari berbagai sumber:")
    print("   • IDX (Bursa Efek Indonesia)")
    print("   • Business Directories")
    print("   • Google Maps")
    print("=" * 60)

def print_config_summary():
    """Print ringkasan konfigurasi"""
    print("\n📋 KONFIGURASI SAAT INI:")
    print(f"   • IDX Companies: {'✅ Enabled' if config.IDX_SETTINGS['enabled'] else '❌ Disabled'}")
    print(f"   • Business Directories: {'✅ Enabled' if config.DIRECTORY_SETTINGS['enabled'] else '❌ Disabled'}")
    print(f"   • Google Maps: {'✅ Enabled' if config.GOOGLE_MAPS_SETTINGS['enabled'] else '❌ Disabled'}")
    print(f"   • Save to Excel: {'✅ Enabled' if config.OUTPUT_SETTINGS['save_to_excel'] else '❌ Disabled'}")
    print(f"   • Append to Monthly Plan: {'✅ Enabled' if not config.OUTPUT_SETTINGS['upload_to_google_sheets'] else '❌ Disabled'}")
    
    if config.IDX_SETTINGS['enabled']:
        print(f"   • IDX Limit: {config.IDX_SETTINGS['limit']} companies")
    
    if config.DIRECTORY_SETTINGS['enabled']:
        print(f"   • Directory Pages: {config.DIRECTORY_SETTINGS['pages_per_directory']} pages")
    
    if config.GOOGLE_MAPS_SETTINGS['enabled']:
        print(f"   • Google Maps Queries: {len(config.GOOGLE_MAPS_SETTINGS['queries'])} queries")

def check_requirements():
    """Check apakah semua requirement terpenuhi"""
    print("\n🔍 MEMERIKSA REQUIREMENTS...")
    
    # Check Monthly Plan Excel file
    if not config.OUTPUT_SETTINGS['upload_to_google_sheets']:  # If using Monthly Plan
        monthly_plan_file = config.OUTPUT_SETTINGS.get('monthly_plan_filename', 'Monthly Plan NEXT IT 2024.xlsx')
        if not os.path.exists(monthly_plan_file):
            print(f"❌ File {monthly_plan_file} tidak ditemukan!")
            print("📋 Pastikan file Monthly Plan Excel ada di folder yang sama")
            return False
        else:
            print(f"✅ File {monthly_plan_file} ditemukan")
    
    # Check CSV file for IDX
    if config.IDX_SETTINGS['enabled']:
        if not os.path.exists('daftar_perusahaan_idx.csv'):
            print("❌ File daftar_perusahaan_idx.csv tidak ditemukan!")
            print("📋 Jalankan get_company_list.py terlebih dahulu")
            return False
        else:
            print("✅ File daftar_perusahaan_idx.csv ditemukan")
    
    # Check Chrome driver
    try:
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.quit()
        print("✅ Chrome driver berfungsi")
    except Exception as e:
        print(f"❌ Chrome driver error: {e}")
        print("📋 Pastikan chromedriver.exe ada di folder yang sama")
        return False
    
    print("✅ Semua requirements terpenuhi!")
    return True

def run_collection():
    """Jalankan proses pengumpulan data"""
    print("\n🚀 MEMULAI PENGUMPULAN DATA...")
    print(f"⏰ Waktu mulai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Inisialisasi collector
        collector = MassDataCollector()
        
        # Konfigurasi berdasarkan config.py
        idx_limit = config.IDX_SETTINGS['limit'] if config.IDX_SETTINGS['enabled'] else 0
        directory_pages = config.DIRECTORY_SETTINGS['pages_per_directory'] if config.DIRECTORY_SETTINGS['enabled'] else 0
        google_maps_queries = config.GOOGLE_MAPS_SETTINGS['queries'] if config.GOOGLE_MAPS_SETTINGS['enabled'] else None
        
        # Jalankan pengumpulan data
        data = collector.run_mass_collection(
            idx_limit=idx_limit,
            directory_pages=directory_pages,
            google_maps_queries=google_maps_queries
        )
        
        print(f"\n🎉 PENGUMPULAN DATA SELESAI!")
        print(f"📊 Total data yang dikumpulkan: {len(data)} perusahaan")
        print(f"⏰ Waktu selesai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return data
        
    except KeyboardInterrupt:
        print("\n⚠️ Proses dihentikan oleh user")
        return []
    except Exception as e:
        print(f"\n❌ Error selama pengumpulan data: {str(e)}")
        return []

def main():
    """Main function"""
    print_banner()
    print_config_summary()
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Requirements tidak terpenuhi. Silakan perbaiki terlebih dahulu.")
        return
    
    # Konfirmasi user
    print("\n❓ Apakah Anda ingin melanjutkan? (y/n): ", end="")
    try:
        response = input().lower().strip()
        if response not in ['y', 'yes', 'ya']:
            print("❌ Proses dibatalkan.")
            return
    except KeyboardInterrupt:
        print("\n❌ Proses dibatalkan.")
        return
    
    # Jalankan pengumpulan data
    data = run_collection()
    
    if data:
        print(f"\n✅ Proses berhasil! {len(data)} data perusahaan telah dikumpulkan.")
        print("📁 Cek file Excel yang dihasilkan untuk melihat hasilnya.")
    else:
        print("\n❌ Tidak ada data yang berhasil dikumpulkan.")

if __name__ == "__main__":
    main() 