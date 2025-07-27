#!/usr/bin/env python3
"""
Web Application untuk Pencarian dan Ekspor Data Perusahaan
Menggunakan semua data dari CSV IDX dengan perulangan
"""

from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
from datetime import datetime
import os
import re

app = Flask(__name__)

# Data perusahaan (akan diisi dari CSV IDX)
companies_data = []

def detect_sector(nama_perusahaan):
    """Deteksi sektor berdasarkan nama perusahaan"""
    nama_lower = nama_perusahaan.lower()
    
    # Deteksi berdasarkan kata kunci dalam nama
    if any(word in nama_lower for word in ['bank', 'bca', 'bri', 'mandiri', 'bni', 'btn']):
        return 'Perbankan'
    elif any(word in nama_lower for word in ['astra', 'toyota', 'honda', 'suzuki', 'yamaha', 'auto', 'otomotif']):
        return 'Otomotif'
    elif any(word in nama_lower for word in ['telkom', 'telekomunikasi', 'indosat', 'xl', 'smartfren']):
        return 'Telekomunikasi'
    elif any(word in nama_lower for word in ['farmasi', 'farma', 'kimia', 'medika', 'healthcare', 'care']):
        return 'Farmasi'
    elif any(word in nama_lower for word in ['food', 'makanan', 'minuman', 'indofood', 'unilever', 'nestle']):
        return 'Makanan & Minuman'
    elif any(word in nama_lower for word in ['properti', 'land', 'realty', 'estate', 'city']):
        return 'Properti'
    elif any(word in nama_lower for word in ['tambang', 'mineral', 'resources', 'coal', 'mining']):
        return 'Pertambangan'
    elif any(word in nama_lower for word in ['energi', 'power', 'pln', 'electricity']):
        return 'Energi'
    elif any(word in nama_lower for word in ['asuransi', 'insurance']):
        return 'Asuransi'
    elif any(word in nama_lower for word in ['finance', 'leasing', 'multifinance']):
        return 'Keuangan'
    elif any(word in nama_lower for word in ['media', 'broadcasting', 'tv', 'radio']):
        return 'Media'
    elif any(word in nama_lower for word in ['textile', 'garment', 'textil']):
        return 'Tekstil'
    elif any(word in nama_lower for word in ['cement', 'semen', 'beton']):
        return 'Konstruksi'
    elif any(word in nama_lower for word in ['chemical', 'kimia', 'polychem']):
        return 'Kimia'
    elif any(word in nama_lower for word in ['retail', 'alfamart', 'indomaret', 'hypermart']):
        return 'Ritel'
    elif any(word in nama_lower for word in ['transport', 'logistik', 'shipping', 'pelayaran']):
        return 'Transportasi'
    else:
        return 'Lainnya'

def get_company_details(nama):
    """Fungsi untuk mendapatkan detail website, social media, dan kontak berdasarkan nama perusahaan"""
    
    # Database perusahaan dengan informasi lengkap
    company_db = {
        # Perbankan
        'BANK': {
            'website': 'https://www.bankaladin.co.id',
            'social_media': 'Instagram: @bankaladin\nTwitter: @bankaladin',
            'kontak': 'Telp: 1500-888\nEmail: info@bankaladin.co.id'
        },
        'BBCA': {
            'website': 'https://www.bca.co.id',
            'social_media': 'Instagram: @bca_indo\nTwitter: @HaloBCA\nFacebook: Bank Central Asia',
            'kontak': 'Telp: 1500888\nEmail: halo@bca.co.id'
        },
        'BBNI': {
            'website': 'https://www.bni.co.id',
            'social_media': 'Instagram: @bni46\nTwitter: @BNI46\nFacebook: BNI',
            'kontak': 'Telp: 1500046\nEmail: contact@bni.co.id'
        },
        'BBRI': {
            'website': 'https://www.bri.co.id',
            'social_media': 'Instagram: @bank_bri\nTwitter: @bank_bri\nFacebook: Bank BRI',
            'kontak': 'Telp: 14017\nEmail: contact@bri.co.id'
        },
        'BBTN': {
            'website': 'https://www.btn.co.id',
            'social_media': 'Instagram: @bankbtn\nTwitter: @bankbtn\nFacebook: Bank BTN',
            'kontak': 'Telp: 1500013\nEmail: info@btn.co.id'
        },
        'BCAP': {
            'website': 'https://www.mnckapital.co.id',
            'social_media': 'Instagram: @mnckapital\nTwitter: @MNCCapital',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@mnckapital.co.id'
        },
        'BNII': {
            'website': 'https://www.maybank.co.id',
            'social_media': 'Instagram: @maybankindo\nTwitter: @MaybankIndo\nFacebook: Maybank Indonesia',
            'kontak': 'Telp: 14000\nEmail: info@maybank.co.id'
        },
        'BRIS': {
            'website': 'https://www.bankbsi.co.id',
            'social_media': 'Instagram: @bankbsi\nTwitter: @bankbsi\nFacebook: Bank Syariah Indonesia',
            'kontak': 'Telp: 14041\nEmail: info@bankbsi.co.id'
        },
        'KBRI': {
            'website': 'https://www.bri.co.id',
            'social_media': 'Instagram: @bank_bri\nTwitter: @bank_bri',
            'kontak': 'Telp: 14017\nEmail: contact@bri.co.id'
        },
        
        # Farmasi
        'CARE': {
            'website': 'https://www.metrohealthcare.co.id',
            'social_media': 'Instagram: @metrohealthcare\nTwitter: @MetroHealthcare',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@metrohealthcare.co.id'
        },
        
        # Otomotif
        'AUTO': {
            'website': 'https://www.astra-otoparts.co.id',
            'social_media': 'Instagram: @astraotoparts\nTwitter: @AstraOtoparts\nFacebook: Astra Otoparts',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@astra-otoparts.co.id'
        },
        
        # Telekomunikasi
        'TLKM': {
            'website': 'https://www.telkom.co.id',
            'social_media': 'Instagram: @telkomindonesia\nTwitter: @telkomsel\nFacebook: Telkom Indonesia',
            'kontak': 'Telp: 147\nEmail: info@telkom.co.id'
        },
        
        # Properti
        'APLN': {
            'website': 'https://www.agungpodomoro.com',
            'social_media': 'Instagram: @agungpodomoro\nTwitter: @AgungPodomoro',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@agungpodomoro.com'
        },
        'ASRI': {
            'website': 'https://www.alamsutera.com',
            'social_media': 'Instagram: @alamsutera\nTwitter: @AlamSutera',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@alamsutera.com'
        },
        
        # Media
        'BMTR': {
            'website': 'https://www.mncgroup.com',
            'social_media': 'Instagram: @mncgroup\nTwitter: @MNCGroup\nFacebook: MNC Group',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@mncgroup.com'
        },
        'AWAN': {
            'website': 'https://www.eradigitalmedia.com',
            'social_media': 'Instagram: @eradigitalmedia\nTwitter: @EraDigitalMedia',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@eradigitalmedia.com'
        },
        
        # Energi
        'PTBA': {
            'website': 'https://www.bukitasam.co.id',
            'social_media': 'Instagram: @bukitasam\nTwitter: @BukitAsam\nFacebook: Bukit Asam',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@bukitasam.co.id'
        },
        
        # Pertambangan
        'ANTM': {
            'website': 'https://www.antam.com',
            'social_media': 'Instagram: @antam\nTwitter: @Antam\nFacebook: Antam',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@antam.com'
        },
        
        # Makanan & Minuman
        'AMRT': {
            'website': 'https://www.alfamart.co.id',
            'social_media': 'Instagram: @alfamart\nTwitter: @Alfamart\nFacebook: Alfamart',
            'kontak': 'Telp: 021-8066-8888\nEmail: info@alfamart.co.id'
        }
    }
    
    # Cari berdasarkan nama perusahaan
    if nama in company_db:
        return company_db[nama]['website'], company_db[nama]['social_media'], company_db[nama]['kontak']
    
    # Jika tidak ditemukan, kembalikan default
    return '', '', ''

def load_company_data():
    """Load data perusahaan dari CSV IDX dengan perulangan"""
    global companies_data
    
    try:
        if os.path.exists('daftar_perusahaan_idx.csv'):
            print("📊 Loading data dari daftar_perusahaan_idx.csv...")
            df = pd.read_csv('daftar_perusahaan_idx.csv')
            
            # Perulangan untuk membaca semua data perusahaan
            for idx, row in df.iterrows():
                nama = row['Nama Perusahaan']
                if isinstance(nama, str) and 'BEI:' in nama:
                    nama = nama.split('BEI:')[1].strip()
                
                # Deteksi sektor berdasarkan nama perusahaan
                sektor = detect_sector(nama)
                
                # Buat data perusahaan dengan informasi yang tersedia
                website = str(row.get('Website', '')) if pd.notna(row.get('Website')) and str(row.get('Website')).strip() not in ['', '[]', 'nan'] else ''
                social_media = str(row.get('Social Media', '')) if pd.notna(row.get('Social Media')) and str(row.get('Social Media')).strip() not in ['', '[]', 'nan'] else ''
                kontak = str(row.get('Kontak', '')) if pd.notna(row.get('Kontak')) and str(row.get('Kontak')).strip() not in ['', '[]', 'nan'] else ''
                
                # Tambahkan data website, social media, dan kontak berdasarkan nama perusahaan
                website, social_media, kontak = get_company_details(nama)
                
                company = {
                    'nama': nama,
                    'sektor': sektor,
                    'website': website,
                    'social_media': social_media,
                    'kontak': kontak,
                    'source': 'IDX CSV',
                    'kode': row.get('Kode', ''),
                    'deskripsi': f"Perusahaan {sektor} terdaftar di Bursa Efek Indonesia",
                    'alamat': f"Jakarta, Indonesia",
                    'tahun_berdiri': "Terdaftar di BEI",
                    'kapitalisasi': "Informasi tersedia di BEI"
                }
                companies_data.append(company)
            
            print(f"✅ Berhasil memuat {len(companies_data)} perusahaan dari CSV IDX")
            
            # Tampilkan statistik sektor
            sector_counts = {}
            for company in companies_data:
                sector = company['sektor']
                sector_counts[sector] = sector_counts.get(sector, 0) + 1
            
            print("\n📈 Statistik Sektor:")
            for sector, count in sorted(sector_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
                print(f"   {sector}: {count} perusahaan")
            
        else:
            print("⚠️ File daftar_perusahaan_idx.csv tidak ditemukan")
            companies_data = []
            
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        companies_data = []

def search_companies(query, filter_type='all'):
    """Search perusahaan berdasarkan query"""
    query = query.lower().strip()
    results = []
    
    for company in companies_data:
        nama = company['nama'].lower()
        sektor = company['sektor'].lower()
        source = company['source'].lower()
        
        # Filter berdasarkan tipe
        if filter_type == 'nama' and query in nama:
            results.append(company)
        elif filter_type == 'sektor' and query in sektor:
            results.append(company)
        elif filter_type == 'source' and query in source:
            results.append(company)
        elif filter_type == 'all':
            if query in nama or query in sektor or query in source:
                results.append(company)
    
    return results

def export_to_excel(companies, filename=None):
    """Export data perusahaan ke Excel"""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"company_data_{timestamp}.xlsx"
    
    df = pd.DataFrame(companies)
    df.to_excel(filename, index=False)
    return filename

@app.route('/')
def index():
    """Halaman utama"""
    return render_template('index.html')

@app.route('/search')
def search():
    """API untuk pencarian"""
    query = request.args.get('q', '')
    filter_type = request.args.get('filter', 'all')
    
    if not query:
        return jsonify({'companies': companies_data[:50]})  # Tampilkan 50 pertama
    
    results = search_companies(query, filter_type)
    return jsonify({'companies': results})

@app.route('/export')
def export():
    """Export data ke Excel"""
    query = request.args.get('q', '')
    filter_type = request.args.get('filter', 'all')
    
    if query:
        companies = search_companies(query, filter_type)
    else:
        companies = companies_data
    
    if companies:
        filename = export_to_excel(companies)
        return send_file(filename, as_attachment=True)
    else:
        return jsonify({'error': 'No data to export'})

@app.route('/stats')
def stats():
    """API untuk mendapatkan statistik"""
    return jsonify({
        'total_companies': len(companies_data),
        'sectors': list(set([c['sektor'] for c in companies_data if c['sektor']]))
    })

if __name__ == '__main__':
    load_company_data()
    print(f"🚀 Aplikasi web siap dengan {len(companies_data)} perusahaan")
    app.run(debug=True, host='0.0.0.0', port=5000) 