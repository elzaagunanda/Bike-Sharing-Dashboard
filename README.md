# Bike Sharing Dashboard 🚴‍♂️✨

Proyek ini adalah dashboard interaktif untuk analisis data peminjaman sepeda berdasarkan dataset **Bike Sharing**. Dashboard ini memvisualisasikan berbagai informasi penting, seperti pengaruh cuaca terhadap peminjaman sepeda, jam-jam sibuk peminjaman sepeda, serta kluster waktu peminjaman.

## Fitur Utama:

- Visualisasi peminjaman sepeda berdasarkan kondisi cuaca.
- Analisis jam sibuk peminjaman sepeda.
- Clustering peminjaman berdasarkan jam dalam sehari.
- Interaktif dengan tampilan yang ramah pengguna.

---

## **Setup Environment** - **Anaconda** 🐍

Ikuti langkah-langkah berikut untuk mengatur lingkungan pengembangan menggunakan **Anaconda**:

1. Buat dan aktifkan environment dengan Python 3.9:
    ```bash
    conda create --name bike-sharing-dashboard python=3.9
    conda activate bike-sharing-dashboard
    ```

2. Install semua dependensi yang tercantum di dalam `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

---

## **Setup Environment** - **Shell/Terminal** 💻

Jika tidak menggunakan **Anaconda**, Anda dapat menggunakan **Shell/Terminal** untuk mengatur environment Anda:

1. Buat direktori proyek:
    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    ```

2. Inisialisasi environment menggunakan `pipenv`:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Install semua dependensi yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```

---

## **Menjalankan Aplikasi Streamlit** 🚀

Setelah environment siap, Anda dapat menjalankan aplikasi Streamlit menggunakan perintah berikut:

```bash
streamlit run app.py
```

Aplikasi Streamlit Anda akan berjalan pada local server, biasanya di alamat: **http://localhost:8501**. Anda dapat membuka dashboard melalui browser dan melihat hasil analisis serta visualisasi yang sudah dibuat.

---

## **Struktur Proyek** 📁

Berikut adalah struktur direktori proyek untuk referensi:

```
submission
├───dashboard
|    ├───hour.csv
|    └───bike_sharing_dashboard.py
|    └───sepeda.jpg
├───data
|    └───hur.csv
├───Proyek Analisis Data.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

---

## **Kesimpulan dan Insight** 🔍

1. **Pengaruh Kondisi Cuaca**:
   - Kondisi cuaca cerah mendorong jumlah peminjaman sepeda yang lebih tinggi, sementara kondisi cuaca ekstrem menyebabkan penurunan signifikan dalam jumlah peminjaman.
   
2. **Jam Sibuk Peminjaman**:
   - Puncak peminjaman sepeda terjadi pada jam sibuk pagi (8-9 pagi) dan sore hari (5-7 sore), mengindikasikan tingginya permintaan saat jam pergi-pulang kerja.
   
3. **Clustering Berdasarkan Jam Peminjaman**:
   - Clustering menunjukkan bahwa puncak peminjaman terjadi di pagi dan sore hari, sedangkan malam hari mengalami penurunan peminjaman.

---

## **Tautan Dashboard** 🔗

Akses dashboard secara online melalui tautan berikut: https://bike-sharing-dashboard-dzdnm9sa2rc4lrujmmmnq2.streamlit.app/

---
