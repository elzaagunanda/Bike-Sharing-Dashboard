import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set background color and text color
st.markdown("""
<style>
    .reportview-container {
        background: white;
        color: black;
    }
    .stButton>button {
        background-color: skyblue;
        color: white;
    }
    .center-text {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Judul aplikasi dan gambar header
st.title('Bike Sharing Dashboard', anchor='center')
st.image('sepeda.jpg', use_column_width='auto')  # Ganti dengan nama file gambar Anda

# Tulis artikel singkat
st.subheader('Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda', anchor='center')
st.write("""
    Data ini menunjukkan bagaimana kondisi cuaca mempengaruhi jumlah peminjaman sepeda.
    Dari analisis yang dilakukan, terlihat bahwa ada puncak peminjaman pada jam tertentu dalam sehari.
    Mari kita lihat lebih dalam.
""")

# Load dataset
df = pd.read_csv('hour.csv')  # Pastikan file hour.csv ada di folder yang sama

# Visualisasi rata-rata peminjaman sepeda berdasarkan cuaca
weather_labels = {
    0: 'Cerah',
    1: 'Berkabut + Berawan',
    2: 'Salju Ringan + Hujan',
    3: 'Hujan Lebat + Hujan Es',
    4: 'Kondisi Ekstrem'
}

average_rentals_by_weather = df.groupby('weathersit')['cnt'].mean().reset_index()
average_rentals_by_weather['weathersit'] = average_rentals_by_weather['weathersit'].map(weather_labels)

# Diagram Batang untuk Rata-Rata Peminjaman Sepeda Berdasarkan Kondisi Cuaca
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(average_rentals_by_weather['weathersit'], average_rentals_by_weather['cnt'], color='skyblue')
plt.title('Rata-Rata Peminjaman Sepeda Berdasarkan Kondisi Cuaca', fontsize=16)
plt.xlabel('Kondisi Cuaca', fontsize=14)
plt.ylabel('Rata-Rata Jumlah Peminjaman Sepeda', fontsize=14)
plt.xticks(rotation=15, fontsize=12)
plt.grid(axis='y')
st.pyplot(fig1)

# Analisis peminjaman sepeda berdasarkan jam
average_rentals_by_hour = df.groupby('hr')['cnt'].mean().reset_index()

# Diagram Batang untuk Rata-Rata Peminjaman Sepeda Berdasarkan Jam
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(average_rentals_by_hour['hr'], average_rentals_by_hour['cnt'], color='skyblue')
plt.title('Rata-Rata Peminjaman Sepeda Berdasarkan Jam', fontsize=16)
plt.xlabel('Jam dalam Sehari', fontsize=14)
plt.ylabel('Rata-Rata Jumlah Peminjaman Sepeda', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.grid(axis='y')
st.pyplot(fig2)

# Kesimpulan
st.write("### Kesimpulan:")
st.write("""
- **Kondisi cuaca cerah mendorong jumlah peminjaman sepeda yang lebih tinggi**, sementara kondisi cuaca ekstrem menyebabkan penurunan signifikan dalam jumlah peminjaman. 
- **Puncak peminjaman sepeda terjadi pada jam sibuk pagi (8-9 pagi) dan sore hari (5-7 sore)**, mengindikasikan tingginya permintaan saat jam pergi-pulang kerja.
""")

# Grafik peminjaman sepeda berdasarkan waktu
df['time_period'] = pd.cut(df['hr'], bins=[0, 6, 12, 18, 24], labels=['Night', 'Morning', 'Afternoon', 'Evening'])
time_cluster = df.groupby('time_period')['cnt'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(time_cluster['time_period'], time_cluster['cnt'], color='skyblue')
plt.title('Peminjaman Sepeda Berdasarkan Periode Waktu', fontsize=16)
plt.xlabel('Periode Waktu', fontsize=14)
plt.ylabel('Total Peminjaman Sepeda', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y')
st.pyplot(plt)

# Kesimpulan Clustering
st.write("### Conclusion Clustering Berdasarkan Jam Peminjaman:")
st.write("""
- **Night (Malam, jam 00:00 - 06:00):**
Jumlah peminjaman sepeda paling sedikit terjadi pada malam hari, wajar karena kebanyakan orang beristirahat.

- **Morning (Pagi, jam 06:00 - 12:00):**
Peminjaman meningkat saat pagi, terkait dengan aktivitas berangkat kerja atau sekolah.

- **Afternoon (Siang, jam 12:00 - 18:00):**
Siang hari menunjukkan aktivitas yang stabil, kemungkinan karena kegiatan istirahat atau rekreasi.

- **Evening (Sore, jam 18:00 - 24:00):**
Peminjaman kembali meningkat saat sore hari, berhubungan dengan aktivitas pulang kerja dan olahraga.

**Main Conclusion:**
Clustering menunjukkan puncak peminjaman sepeda terjadi di pagi dan sore hari, sementara malam hari mengalami penurunan signifikan. Hal ini sesuai dengan pola aktivitas harian masyarakat, yang dapat membantu penyedia layanan untuk menyesuaikan ketersediaan sepeda dan jam operasional layanan.
""")
