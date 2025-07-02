# 🌏 Nusantara Story: Menggali Narasi Budaya, Mengenal Potensi Wisata

## 📝 Deskripsi Proyek

**Nusantara Story** adalah aplikasi web open-source yang didesain untuk memberdayakan individu dan komunitas dalam menggali, merangkai, dan mempromosikan kekayaan narasi budaya serta potensi pariwisata lokal Indonesia secara efektif.

Dengan memanfaatkan teknologi **Artificial Intelligence (AI)**, aplikasi ini memfasilitasi pembuatan narasi yang memikat, analisis potensi promosi yang cerdas, dan ide pengembangan ekonomi lokal yang inovatif.  
Tujuan utamanya adalah meningkatkan visibilitas dan daya tarik warisan budaya serta destinasi pariwisata Indonesia — demi pelestarian budaya dan pertumbuhan ekonomi daerah.

---

## 📌 Latar Belakang

Indonesia kaya akan budaya, tradisi, dan destinasi wisata, namun masih menghadapi tantangan dalam mengekspos potensi ini secara optimal. Masalah seperti strategi promosi yang lemah dan keterbatasan teknik storytelling kerap menghambat pelaku budaya dan pariwisata lokal.

Berdasarkan survei Kemenparekraf, banyak pelaku usaha lokal butuh dukungan promosi dan pengembangan konten.
Oleh karena itu, disini **Nusantara Story** hadir sebagai solusi berbasis teknologi AI untuk:

- 🌐 Menjembatani akses promosi global  
- 🛡️ Mendukung pelestarian budaya  
- 💼 Mendorong ekonomi lokal berkelanjutan  

---

## ❗ Permasalahan yang Diselesaikan

- ✍️ **Kesulitan Merangkai Narasi Otentik**  
- 📉 **Kurangnya Analisis Promosi Efektif**  
- 💸 **Minimnya Ide Pengembangan Ekonomi Lokal Berkelanjutan**  
- 🚫 **Akses Terbatas Terhadap Teknologi Canggih**

---

## 🚀 Fitur Utama

- 📝 **Generate Narasi Budaya/Wisata**
  - Input: Nama Objek, Lokasi, Deskripsi Singkat
  - Opsi gaya narasi: 🎓 Edukasi, 📢 Promosi, 🧙 Cerita Rakyat, ✨ Puitis, 📰 Informatif, 💡 Inspiratif
  - 🎯 Fitur penyesuaian Bahasa yang disesuaikan dengan input Target Audiens (Inggris, Mandarin, Arab, Indonesia (Default), Jepang, Korea, Jerman, Prancis, dan Spanyol). Contoh Input: Wisatawan Asing (Output: Inggris), Mandarin Speakers (Output: Mandarin).

- 🧠 **Generate Analisis Potensi Promosi**
  - 📌 Analisis poin jual, 🎯 segmen wisatawan, 💰 ide monetisasi, 📢 strategi promosi, 🤝 potensi kolaborasi
  - Output dalam format JSON 🧾

- 📥 **Download PDF Output**  
- 🧑‍💻 **Antarmuka Pengguna Intuitif**  
- 📚 **Halaman Panduan, Contoh, & Tentang Pengembang**

---

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman**: Python  
- **Framework**: Streamlit `v1.46.1`

### Model AI/API:
- **Google Gemini-2.5 Flash API** – Generasi narasi & analisis promosi
- **IBM Granite 3.3-8b-Instruct** – Code generation & optimization

### Pustaka Python:
- `streamlit`
- `google-generativeai`
- `pandas`
- `reportlab` – Output PDF
- `json` – Parsing output JSON

### Styling:
- Custom CSS (eksternal & inline)

### Deployment:
- Streamlit Cloud

---

## 🤖 Penjelasan Dukungan AI

### 🧠 Google Gemini-2.5 Flash
- ✍️ **Narasi**: Instruction-based + Role-playing + Constraint Prompting  
- 📊 **Analisis Promosi**: Structured Output Prompting (JSON)

### 🛠️ IBM Granite 3.3-8b-Instruct

- 🔧 Menggunakan teknik **Code In-Context Learning** dengan menyisipkan segmen kode Python langsung ke dalam prompt.
- Teknik ini dikombinasikan dengan pendekatan **Instruction-based Prompting** dan **Goal-Oriented Prompting** untuk memandu model dalam:
  - Mereview dan mengoptimalkan kode (dari segi *readability*, *performance*, dan *best practices*)
  - Meregenerasi kode berdasarkan saran tertentu
  - Mengeksplorasi teknik optimasi seperti **batching**, **caching**, atau **parameter tuning**

📄 Implementasi model **IBM Granite 3.3-8b-Instruct** dapat dilihat pada notebook berikut:  
➡️ [IBMGranite_code_generation_Kholish_Fauzan.ipynb](https://github.com/Kholish-Fauzan/hacktiv8-project/blob/main/IBMGranite_code_generation_Kholish_Fauzan.ipynb).


---

## 📦 Panduan Instalasi dan Penggunaan

### 🔗 Akses Aplikasi Langsung

### 👉 [Nusantara Story / Deployment Link](https://nusantara-story.streamlit.app/)

---

### 🖥️ Jalankan Secara Lokal

#### 1. Prasyarat:
- Python `>=3.10` (disarankan `3.13.2`)
- pip

#### 2. Kloning Repositori

```bash
git clone https://github.com/Kholish-Fauzan/hacktiv8-project.git
cd hacktiv8-project
```


#### 3. Buat Virtual Environment (Opsional)

```bash
python -m venv venv
# Windows:
.env\Scriptsctivate
# macOS/Linux:
source venv/bin/activate
```

#### 4. Instal Dependensi

```bash
pip install -r requirements.txt
```

#### 5. Konfigurasi API Key

- Buat file `.env` di root folder:
```env
GOOGLE_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY_HERE"
```

- (Opsional) Tambahkan ini di awal `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

> Atau set manual di terminal setiap run

> Untuk Streamlit Cloud, gunakan **Secrets Management** di dashboard

#### 6. Jalankan Aplikasi

```bash
streamlit run app.py
```

Akses via browser di [http://localhost:8501](http://localhost:8501)

---

*This project is developed by **Ahmad Kholish Fauzan Shobiry** throughout the **Student Developer Initiavite** program from **HACKTIV8**.*