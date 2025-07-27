import csv
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
]

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")
driver = webdriver.Chrome(options=chrome_options)

def get_td_content_by_label(soup, label):
    for tr in soup.find_all("tr"):
        td_label = tr.find("td", class_="td-name")
        td_content = tr.find("td", class_="td-content")
        if td_label and td_content and label.lower() in td_label.get_text(strip=True).lower():
            if label.lower() in ["situs", "website"]:
                a_tag = td_content.find("a")
                if a_tag:
                    return a_tag.get_text(strip=True)
            span = td_content.find("span")
            if span:
                return span.get_text(strip=True)
            return td_content.get_text(strip=True)
    return "-"

csv_file = 'hasil_scrapping.csv'
header = ['nama', 'sektor', 'website', 'kontak', 'sosmed']
existing_names = set()

# Cek dan baca nama yang sudah ada di hasil_scrapping.csv
if os.path.exists(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_names.add(row['nama'])

data_list = []  # List untuk menampung hasil scraping baru

with open('daftar_perusahaan_idx.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nama_perusahaan = row['Nama Perusahaan']
        if ": " in nama_perusahaan:
            kode = nama_perusahaan.split(": ")[1]
        else:
            kode = row['Kode'].strip()

        url = f"https://www.idx.co.id/id/perusahaan-tercatat/profil-perusahaan-tercatat/{kode}"
        print(f"[INFO] Scraping: {kode} ({url})")

        headers = {
            'User-Agent': random.choice(user_agents),
            'Referer': 'https://www.google.com/'
        }

        # Cek apakah nama sudah ada di hasil_scrapping.csv
        # (nama diambil setelah scraping, jadi scraping tetap dilakukan, tapi bisa dioptimalkan jika ingin skip sebelum scraping)
        # Untuk efisiensi, scraping tetap dilakukan, lalu dicek nama hasil scraping
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"[ERROR] requests gagal: {e}, coba pakai Selenium...")
            try:
                driver.get(url)
                time.sleep(3)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
            except Exception as e2:
                print(f"[ERROR] Selenium juga gagal: {e2}")
                continue

        nama    = get_td_content_by_label(soup, "Nama")
        sektor  = get_td_content_by_label(soup, "Sektor")
        website = get_td_content_by_label(soup, "Situs")
        kontak  = get_td_content_by_label(soup, "Telepon")
        sosmed  = "-"  # Jika memang tidak ada, isi "-"

        # Skip jika nama sudah ada di existing_names
        if nama in existing_names:
            print(f"[SKIP] {nama} sudah ada di hasil_scrapping.csv")
            continue

        print(f"nama   : {nama}")
        print(f"sektor : {sektor}")
        print(f"website: {website}")
        print(f"sosmed : {sosmed}")
        print(f"kontak : {kontak}")
        print("-" * 50)

        # Simpan hasil ke list
        data_list.append({
            'nama': nama,
            'sektor': sektor,
            'website': website,
            'kontak': kontak,
            'sosmed': sosmed
        })

        time.sleep(random.uniform(2, 5))

driver.quit()

# Simpan data baru ke CSV (append jika file sudah ada, tulis header hanya jika file baru)
if data_list:
    write_header = not os.path.exists(csv_file)
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if write_header:
            writer.writeheader()
        for data in data_list:
            writer.writerow(data)
    print(f"\nData baru berhasil ditambahkan ke {csv_file}")
else:
    print("\nTidak ada data baru untuk ditambahkan.")
