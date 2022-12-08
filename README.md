# Jernihin

Aplikasi Pendeteksi Kualitas Air

## Daftar Isi

1. [Daftar Isi](#daftar-isi "Daftar Isi")
2. [Website Jernihin](#website-jernihin "Website Jernihin")
3. [Apa itu Jernihin?](#apa-itu-jernihin "Apa itu Jernihin?")
   1. [Latar Belakang](#1-latar-belakang "Latar Belakang")
   2. [Tujuan](#2-tujuan "Tujuan")
   3. [Instalasi dan Deployment](#3-instalasi-dan-deployment "Instalasi dan Deployment")
   4. [Cara Kerja](#4-cara-kerja "Cara Kerja")
   5. [Referensi](#5-referensi "Referensi")
   6. [Developers](#6-developers "Developers")

## Website Jernihin

Tautan akses website <a href="https://jernihin.up.railway.app" title="Jernihin" target="_blank">Jernihin</a>.

## Apa itu Jernihin?

### 1. Latar Belakang
tes
Sumber daya alam yang berpotensi besar bagi makhluk hidup dan setiap tahun
mengalami peningkatan adalah air. [1] Menurut Data SDG, indeks kualitas air Indonesia
tahun 2020 sebesar 53,53, meningkat dari tahun sebelumnya. Pengukuran air bisa dilihat
dari variabel kimia seperti nilai pH, TDS yang berperan penting dalam menentukan kualitas
air. Untuk mengetahui kualitas air perlu dilakukan pemantauan secara berkala. [2] Salah satu
upaya untuk membantu strategi pengelolaan sumber daya air dengan membangun aplikasi
website menggunakan metode deep learning untuk memprediksi kualitas air dari beberapa
variabel. Aplikasi ini diharapkan dapat memberikan alternatif lain dalam pengelolaan dan
pemantauan kualitas air.


### 2. Tujuan

Tujuan akhir dari proyek ini adalah sebuah aplikasi website yang dapat memberikan
hasil prediksi kualitas air, apakah aman untuk dikonsumsi atau tidak layak untuk dikonsumsi
berdasarkan kandungan partikel di dalam air dan sanitasi sumber daya air yang bersih. Untuk
melakukan prediksi kualitas air, dibutuhkan sejumlah data terkait variabel-variabel
pengukuran kualitas air yang dibutuhkan.
Hasil pengukuran yang akan digunakan sebagai data dapat dilakukan dengan beberapa
cara, yaitu dengan melakukan pengukuran secara mandiri kandungan partikel dan variabel
pengukuran kualitas air lainnya menggunakan alat Water Test Strip Kit dengan harga sekitar
Rp100.000 hingga Rp250.000. Selain itu, untuk memperoleh data hasil pengukuran uji
kualitas air dapat dilakukan dengan cara mendapatkan data tersebut melalui lembaga
penelitian atau institusi pendidikan yang memiliki laboratorium pengujian kualitas air yang
dapat membantu mengumpulkan data hasil pengukuran tersebut secara tepat.

### 3. Instalasi dan Deployment

Agar dapat menjalankan aplikasi website ini pada *virtual environment* lokal, silakan ikuti langkah-langkah berikut ini:

1. Clone Repository ini
   ```bash
   git clone https://github.com/aNdr3W03/Jernihin.git
   ```

2. Install Python Virtual Environment
   ```bash
   virtualenv venv
   ```

3. Install semua *requirements* yang dibutuhkan
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi web dengan Flask
   ```bash
   flask run
   ```
   atau
   ```bash
   python app.py
   ```

5. Hentikan program aplikasi atau *server* dengan cara `ctrl + c`

### 4. Cara Kerja



### 5. Referensi

- Dataset
  
  <a href="https://data.amerigeoss.org" title="AmeriGEOSS Community Platform DataHub" target="_blank">
    <img src="https://user-images.githubusercontent.com/77439245/206162481-5b17dfc2-fc1e-4f0a-a183-8935999becbc.png" alt="AmeriGEOSS Community Platform DataHub" style="width: 250px">
  </a>
  
  AmeriGEOSS Community Platform DataHub  
  <a href="https://data.amerigeoss.org/dataset/wqi-parameter-scores-1994-2013-b0941" title="Water Quality Index Parameter Scores 1994-2013 Dataset" target="_blank">WQI Parameter Scores 1994-2013 Dataset</a>
  
- Language
  
  <a href="https://www.w3schools.com/html" title="HTML5" target=_blank>
    <img src="https://img.shields.io/badge/html5-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white" />
  </a> &nbsp;
  <a href="https://www.w3schools.com/css" title="CSS3" target=_blank>
    <img src="https://img.shields.io/badge/css3-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white" />
  </a> &nbsp;
  <a href="https://www.javascript.com" title="JavaScript" target=_blank>
    <img src="https://img.shields.io/badge/javascript-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black" />
  </a> &nbsp;
  <a href="https://www.python.org" title="Python" target=_blank>
    <img src="https://img.shields.io/badge/python-3670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54" />
  </a> &nbsp;
  
- Framework
  
  <a href="https://getbootstrap.com" title="Bootstrap" target=_blank>
    <img src="https://img.shields.io/badge/bootstrap-%237952B3.svg?&style=for-the-badge&logo=bootstrap&logoColor=white" />
  </a> &nbsp;
  <a href="https://flask.palletsprojects.com" title="Flask" target=_blank>
    <img src="https://img.shields.io/badge/flask-%23000000.svg?&style=for-the-badge&logo=flask&logoColor=white" />
  </a> &nbsp;
  
- Library
  
  <a href="https://jquery.com" title="jQuery" target=_blank>
    <img src="https://img.shields.io/badge/jquery-%230769AD.svg?&style=for-the-badge&logo=jquery&logoColor=white" />
  </a> &nbsp;
  <a href="https://pandas.pydata.org" title="Pandas" target=_blank>
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" />
  </a> &nbsp;
  <a href="https://numpy.org" title="NumPy" target=_blank>
    <img src="https://img.shields.io/badge/numpy-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" />
  </a> &nbsp;
  <a href="https://scikit-learn.org" title="scikit-learn" target=_blank>
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?&style=for-the-badge&logo=scikit-learn&logoColor=3499CD" />
  </a> &nbsp;
  <a href="https://matplotlib.org" title="Matplotlib" target=_blank>
    <img src="https://custom-icon-badges.demolab.com/badge/matplotlib-66baea.svg?style=for-the-badge&logo=matplotlib" />
  </a> &nbsp;
  <a href="https://seaborn.pydata.org" title="Seaborn" target=_blank>
    <img src="https://custom-icon-badges.demolab.com/badge/seaborn-white.svg?style=for-the-badge&logo=seaborn" />
  </a> &nbsp;
  <a href="https://docs.python.org/3/library/pickle.html" title="Pickle" target=_blank>
    <img src="https://img.shields.io/badge/pickle-%23ffffff.svg?style=for-the-badge&logo=pickle&logoColor=black" />
  </a> &nbsp;
  
- Icons and Images
  
  <a href="https://fontawesome.com" title="Font Awesome" target=_blank>
    <img src="https://img.shields.io/badge/font%20awesome-%23339AF0.svg?&style=for-the-badge&logo=font%20awesome&logoColor=white" />
  </a> &nbsp;
  
- Deployment
  
  <a href="https://railway.app" title="Railway App" target=_blank>
    <img src="https://custom-icon-badges.demolab.com/badge/railway-white.svg?style=for-the-badge&logo=railway-app" />
  </a> &nbsp;
  
- Academic Papers
  
  [1] H. Said, N. H. Matondang dan H. N. Irmanda, "Sistem Prediksi Kualitas Air Yang Dapat Dikonsumsi Dengan Menerapkan Algoritma K-Nearest Neighbor," *Seminar Nasional Mahasiswa Ilmu Komputer dan Aplikasinya (SENAMIKA)*, vol. 3, no. 1, pp. 158-168, Apr. 2022. Diakses: 12 Okt. 2022. [Online]. Tersedia pada: <a href="https://conference.upnvj.ac.id/index.php/senamika/article/view/2017" target=_blank>https://conference.upnvj.ac.id/index.php/senamika/article/view/2017</a>
  
  [2] M. H. D. Barang dan S. K. Saptomo, "Analisis Kualitas Air pada Jalur Distribusi Air Bersih di Gedung Baru Fakultas Ekonomi dan Manajemen Institut Pertanian Bogor," *Jurnal Teknik Sipil dan Lingkungan (J-SIL)*, vol. 4, no. 1, pp. 13-24, Apr. 2019. Diakses: 12 Okt. 2022. doi: 10.29244/jsil.4.1.13-24. [Online]. Tersedia pada: <a href="https://journal.ipb.ac.id/index.php/jsil/article/view/23735" target=_blank>https://journal.ipb.ac.id/index.php/jsil/article/view/23735</a>

### 6. Developers

Merdeka Belajar Kampus Merdeka 2022  
SIB Dicoding Cycle 3  
**C22-078 Capstone Team**  

- **M319X0851** - <a href="https://github.com/aNdr3W03" title="GitHub Andrew Benedictus Jamesie" target=_blank>Andrew Benedictus Jamesie</a>
- **M319Y0854** - <a href="https://github.com/chelizaaa" title="GitHub Cheliza Sriayu Simarsoit" target=_blank>Cheliza Sriayu Simarsoit</a>
- **M248X0512** - <a href="https://github.com/gilangaleyusta" title="GitHub A. Gilang Aleyusta Savada" target=_blank>A. Gilang Aleyusta Savada</a>
- **M182Y0310** - <a href="https://github.com/adstika20" title="GitHub Ades Tikaningsih" target=_blank>Ades Tikaningsih</a>
