# Laporan Proyek Sistem Rekomendasi - Paramita Citra Indah Mulia

## Project Overview

**Latar Belakang:**

Dalam era digital saat ini, konsumen dihadapkan pada berbagai pilihan ketika ingin menonton film. Dengan ribuan film yang tersedia di berbagai platform streaming, menemukan film yang sesuai dengan selera pribadi bisa menjadi tugas yang menantang. Oleh karena itu, sistem rekomendasi film menjadi sangat penting untuk membantu konsumen dalam memilih film yang sesuai dengan preferensinya, meningkatkan pengalaman menonton, dan memaksimalkan kepuasan konsumen.



## Business Understanding
### **Problem Statements:**
Berdasarkan pada latar belakang di atas, permasalahan pada proyek ini adalah sebagai berikut:
- Bagaimana cara menyediakan rekomendasi film yang sesuai dengan selera pengguna berdasarkan deskripsi film yang telah ditonton sebelumnya?
- Bagaimana memastikan bahwa rekomendasi yang diberikan relevan dengan preferensi pengguna?
    
### **Goals:**
Tujuan dari proyek ini adalah sebagai berikut:
- Mengembangkan model yang dapat mengklasifikasikan kualitas udara di Jakarta berdasarkan parameter yang diukur.
- Membandingkan dua metode machine learning untuk menentukan metode terbaik dalam klasifikasi kualitas udara.
    
### **Solution Statements:**
- Klasifikasi menggunakan Algoritma dua algoritma machine learning yaitu Random Forest dan KNeighbors
- Model dengan akurasi tertinggi dari data latih adalah model terbaik yang akan digunakan untuk klasifikasi. 



## Data Understanding
Data yang digunakan adalah dataset tmdb_5000_movies dari tmdb-movie-metadata yang diperoleh dari Kaggle (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) . Data ini terdiri dari 4803 data dengan 20 variabel yaitu:

```markdown
1. budget - biaya produksi film
2. genre - genre film : Action, Comedy, Thriller, dll.
3. homepage - link film
4. id - id film
5. keywords - Kata kunci atau tag yang terkait dengan film.
6. original_language - Bahasa pembuatan film.
7. original_title - Judul film sebelum diterjemahkan atau diadaptasi.
8. overview - Deskripsi singkat film.
9. popularity - Kuantitas numerik yang menentukan popularitas film.
10. production_companies - Rumah produksi film.
11. production_countries - Negara tempat film diproduksi.
12. release_date - tanggal rilis.
13. revenue - penghasilan dari film
14. runtime - durasi film
15. spoken_language - bahasa dalam film
16. status - "Released" atau "Rumored".
17. tagline - tagline film
18. title - judul film
19. ote_average - rating rata-rata
20. vote_count - jumlah vote
```


**Univariate EDA**
1. Jumlah bahasa asli di film
   ![gambar](https://github.com/yocimm/movie_recommendation/blob/main/language_image.png?raw=true)

   >Dari 4803 data, sebanyak 4505 film menggunakan Bahasa Inggris.

2. Genre Film:
   ![gambar](https://github.com/yocimm/air_pollution_classification/blob/main/gambar/5_stasiun.png?raw=true)

   >Genre film terbanyak pada dataset ini adalah drama, komedi, drama-romance, comedy-romance, dan comedy-drama.

3. Negara Asal Film:
   ![gambar](https://github.com/yocimm/air_pollution_classification/blob/main/gambar/titik_critical.png?raw=true)
   >Dari keseluruhan data, sebanyak 2977 film diproduksi oleh United States of America.

4. Budget, Revenue, dan Durasi Film:
   ![gambar](?raw-true)
   >* Budget terbesar untuk pembuatan film pada dataset ini adalah 380 juta dolar
   >* Penghasilan terbesar dari film sebesar 2.7 miliar dolar
   >* Durasi film terpanjang yaitu 338 menit


## Data Preparation
1. Membuat dataframe baru yang berisi 'id', 'title', 'overview'
2. Cek duplikasi dan missing value namun hasilnya nol
3. Cleaning text 'overview' :
   - Mengubah ke huruf kecil
   - Menghapus URL
   - Menghapus tanda baca dan angka
   - Menghapus spasi ekstra
   - Menghapus stopwords dan stemming 
4. Pembobotan dengan TF-IDF
5. Menghitung derajat kesamaan (similarity degree) antar film dengan teknik cosine similarity

## Modeling
Pemodelan pada proyek ini menggunakan 2 algoritma machine learning yaitu K-Nearest Neighbor Classifier dan Random Forest Classifier.
  - **KNN** dengan jumlah neighbors yang optimal adalah sebanyak 3. 
  - **Random Forest** dengan jumlah estimator diatur sebanyak 100.

## Evaluation
Metrik evaluasi yang digunakan adalah Confusion matrix dan Classification report.

1. Confusion Matrix
    
    ![kelas](?raw=true)
    ![kelas](?raw=true)
       
    > Dari data test dilakukan prediksi pada kedua model kemudian dibandingkan dengan nilai aktual dan disajikan pada matrik di atas.
    > Dengan RandomForest didapati 2 kesalahan seharusnya kategori SEDANG, namun dikategorikan BAIK.
    > Sementara dengan KNN didapati 3 kesalahan seharusnya kategori SEDANG, namun dikategorikan BAIK, 4 kesalahan seharusnya kategori TIDAK SEHAT, namun dikategorikan SEDANG, dan 4 kesalahan seharusnya kategori SEDANG, namun dikategorikan TIDAK SEHAT.

3. Classification Report

    ![kelas](?raw=true)
        
  **Random Forest**
  - Precision: Proporsi dari prediksi positif yang benar-benar positif.
  Untuk Kelas 0, dari semua prediksi yang diberi label sebagai Kelas 0, 90% dari mereka benar-benar adalah Kelas 0.
  Untuk Kelas 1, dari semua prediksi yang diberi label sebagai Kelas 1, 100% dari mereka benar-benar adalah Kelas 1.
  Untuk Kelas 2, dari semua prediksi yang diberi label sebagai Kelas 2, 100% dari mereka benar-benar adalah Kelas 2.

  - Recall (Sensitivitas): Proporsi dari observasi positif yang benar-benar diprediksi dengan benar. 
  Untuk Kelas 0, dari semua observasi yang sebenarnya adalah Kelas 0, 100% dari mereka diprediksi dengan benar oleh model.
  Untuk Kelas 1, dari semua observasi yang sebenarnya adalah Kelas 1, 96% dari mereka diprediksi dengan benar oleh model.
  Untuk Kelas 2, dari semua observasi yang sebenarnya adalah Kelas 2, 100% dari mereka diprediksi dengan benar oleh model.
  - 
  - F1-Score: Rata-rata harmonik dari precision dan recall. Memberikan kesimbangan antara precision dan recall. 
  Untuk Kelas 0, F1-Score adalah 0.95.
  Untuk Kelas 1, F1-Score adalah 0.98.
  Untuk Kelas 2, F1-Score adalah 1.00.

  **KNN**
    - Precision: Proporsi dari prediksi positif yang benar-benar positif.
  Untuk Kelas 0, dari semua prediksi yang diberi label sebagai Kelas 0, 86% dari mereka benar-benar adalah Kelas 0.
  Untuk Kelas 1, dari semua prediksi yang diberi label sebagai Kelas 1, 91% dari mereka benar-benar adalah Kelas 1.
  Untuk Kelas 2, dari semua prediksi yang diberi label sebagai Kelas 2, 90% dari mereka benar-benar adalah Kelas 2.

  - Recall (Sensitivitas): Proporsi dari observasi positif yang benar-benar diprediksi dengan benar. 
  Untuk Kelas 0, dari semua observasi yang sebenarnya adalah Kelas 0, 100% dari mereka diprediksi dengan benar oleh model.
  Untuk Kelas 1, dari semua observasi yang sebenarnya adalah Kelas 1, 86% dari mereka diprediksi dengan benar oleh model.
  Untuk Kelas 2, dari semua observasi yang sebenarnya adalah Kelas 2, 90% dari mereka diprediksi dengan benar oleh model.
  - 
  - F1-Score: Rata-rata harmonik dari precision dan recall. Memberikan kesimbangan antara precision dan recall. 
  Untuk Kelas 0, F1-Score adalah 0.93.
  Untuk Kelas 1, F1-Score adalah 0.89.
  Untuk Kelas 2, F1-Score adalah 0.90.

Berdasarkan hasil evaluasi yang telah dilakukan, Random Forest memiliki performa lebih baik daripada KNN dalam melakukan klasifikasi indeks udara di Jakarta.
