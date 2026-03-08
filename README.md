# Tugas Machine Learning - Pertemuan 2: Eksplorasi dan Visualisasi Data

Repositori ini berisi hasil pengerjaan tugas Praktikum/Mata Kuliah Machine Learning Pertemuan 2. Fokus utama dari tugas ini adalah melakukan pemuatan data, eksplorasi, dan memvisualisasikan *insight* menggunakan Python.

## Deskripsi Dataset
Dataset yang digunakan adalah `tips.csv`, yang mencatat data transaksi di sebuah restoran, meliputi total tagihan (`total_bill`), jumlah tip (`tip`), jenis kelamin pelanggan (`sex`), status perokok (`smoker`), hari (`day`), waktu makan (`time`), dan ukuran rombongan (`size`).

## Insight dan Visualisasi
Berdasarkan eksplorasi dataset tersebut, terdapat 3 model visualisasi utama yang dikembangkan:

1. **Pie Chart (Persentase Gender)**
   Visualisasi komposisi persentase antara pelanggan laki-laki dan perempuan yang memberikan tip.
2. **Bar Chart (Rata-rata Tip per Hari)**
   Menganalisis rata-rata besaran tip yang diberikan pelanggan pada hari-hari tertentu (Kamis, Jumat, Sabtu, Minggu) untuk melihat tren hari apa yang paling menghasilkan banyak tip.
3. **Scatter Plot (Korelasi Tagihan vs Tip)**
   Melihat hubungan antara besaran total tagihan dengan jumlah tip yang diberikan pelanggan untuk menemukan pola korelasi (apakah tagihan yang lebih besar berbanding lurus dengan tip yang lebih besar).

## Teknologi yang Digunakan
* **Bahasa:** Python 3.14.3
* **Data Manipulation:** Pandas
* **Data Visualization:** Matplotlib
* **Environment:** Virtual Environment (`venv`), VS Code Jupyter Interactive Window

## Cara Menjalankan Kode
Proyek ini dikembangkan di dalam *virtual environment* yang terisolasi. Untuk menjalankannya di mesin lokal, ikuti langkah-langkah berikut:

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/Rakel8/machine-learning-week1.git
   cd machine-learning-week1
   ```

2. **Buat dan aktifkan Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Eksekusi Visualisasi:**
   Buka file `latihan/visualisasi_tips.py` menggunakan Visual Studio Code yang sudah terinstal ekstensi **Jupyter**. Eksekusi program per blok menggunakan fitur Interactive Window dengan mengklik `Run Cell` atau menekan `Shift + Enter` pada setiap blok `# %%`.
