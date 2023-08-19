# Laporan Proyek Sistem Rekomendasi - Paramita Citra Indah Mulia

## Project Overview

**Latar Belakang:**

Dalam era digital saat ini, konsumen dihadapkan pada berbagai pilihan ketika ingin menonton film. Dengan ribuan film yang tersedia di berbagai platform streaming, menemukan film yang sesuai dengan selera pribadi bisa menjadi tugas yang menantang. Di sisi lain, genre film sering menjadi faktor utama yang mempengaruhi keputusan seseorang dalam memilih film untuk ditonton. Mengingat pentingnya genre dalam preferensi penonton, ada kebutuhan untuk sistem rekomendasi yang dapat memberikan saran film berdasarkan genre yang disukai oleh pengguna. Sistem rekomendasi yang efektif dapat membantu konsumen dalam memilih film yang sesuai dengan preferensinya, meningkatkan pengalaman menonton, dan memaksimalkan kepuasan konsumen.

## Business Understanding

### **Problem Statements:**

Berdasarkan pada latar belakang di atas, permasalahan pada proyek ini adalah sebagai berikut:

- Bagaimana cara menyediakan rekomendasi film yang sesuai dengan selera pengguna berdasarkan genre film yang telah ditonton sebelumnya?
- Bagaimana memastikan bahwa rekomendasi yang diberikan relevan dengan preferensi pengguna?

### **Goals:**

Tujuan dari proyek ini adalah sebagai berikut:

- Mengembangkan sistem rekomendasi film berbasis genre yang dapat memberikan saran film kepada pengguna sesuai dengan preferensi genre mereka.
- Meningkatkan kepuasan pengguna dengan memberikan rekomendasi film yang lebih sesuai dengan selera genre mereka sehingga dapat memicu peningkatan keterlibatan pengguna dan pendapatan bagi platform streaming.

### **Solution Statements:**

Untuk mencapai tujuan tersebut, akan digunakan pendekatan Content-Based Filtering. Dengan pendekatan ini, sistem akan membandingkan genre dari film yang telah ditonton pengguna dengan genre film lainnya untuk menemukan kesamaan konten. Film dengan kesamaan konten yang tinggi akan direkomendasikan kepada pengguna. Dengan demikian, rekomendasi yang diberikan akan lebih sesuai dengan selera dan preferensi pengguna berdasarkan film yang telah mereka tonton sebelumnya.

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

   > Dari 4803 data, sebanyak 4505 film menggunakan Bahasa Inggris.

2. Genre Film:

   > Genre film terbanyak pada dataset ini adalah drama, komedi, drama-romance, comedy-romance, dan comedy-drama.

3. Negara Asal Film:

   > Dari keseluruhan data, sebanyak 2977 film diproduksi oleh United States of America.

4. Budget, Revenue, dan Durasi Film:
   **Statistik data numerik :**

|       | budget       | id            | popularity  | revenue      | runtime     | vote_average | vote_count   |
| ----- | ------------ | ------------- | ----------- | ------------ | ----------- | ------------ | ------------ |
| count | 4.803000e+03 | 4803.000000   | 4803.000000 | 4.803000e+03 | 4801.000000 | 4803.000000  | 4803.000000  |
| mean  | 2.904504e+07 | 57165.484281  | 21.492301   | 8.226064e+07 | 106.875859  | 6.092172     | 690.217989   |
| std   | 4.072239e+07 | 88694.614033  | 31.816650   | 1.628571e+08 | 22.611935   | 1.194612     | 1234.585891  |
| min   | 0.000000e+00 | 5.000000      | 0.000000    | 0.000000e+00 | 0.000000    | 0.000000     | 0.000000     |
| 25%   | 7.900000e+05 | 9014.500000   | 4.668070    | 0.000000e+00 | 94.000000   | 5.600000     | 54.000000    |
| 50%   | 1.500000e+07 | 14629.000000  | 12.921594   | 1.917000e+07 | 103.000000  | 6.200000     | 235.000000   |
| 75%   | 4.000000e+07 | 58610.500000  | 28.313505   | 9.291719e+07 | 118.000000  | 6.800000     | 737.000000   |
| max   | 3.800000e+08 | 459488.000000 | 875.581305  | 2.787965e+09 | 338.000000  | 10.000000    | 13752.000000 |

> - Budget terbesar untuk pembuatan film pada dataset ini adalah 380 juta dolar
> - Penghasilan terbesar dari film sebesar 2.7 miliar dolar
> - Durasi film terpanjang yaitu 338 menit

## Data Preparation

1. Membuat dataframe baru yang berisi 'id', 'title', 'genres'
2. Mengubah format genre menjadi lebih mudah dipahami dengan hanya mengambil nama genre saja.

   semula seperti ini:

   > [{"id": 18, "name": "Drama"}, {"id": 10749, "name": "Romance"}]

   menjadi seperti ini:

   > drama-romance

3. Cek duplikasi dan missing value namun hasilnya nol
4. Pembobotan kata dengan TF-IDF
   > Didapatkan ada 22 genre yaitu : 'action', 'adventure', 'animation', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'fiction', 'foreign','history', 'horror', 'movie', 'music', 'mystery', 'romance', 'science', 'thriller', 'tv', 'war', 'western'.

## Modeling

Pada sistem rekomendasi ini digunakan cosine similarity untuk menghitung derajat kesamaan (similarity degree) antar film, dengan cara seperti berikut:

1. Menghitung Dot Product: Setelah memiliki dua vektor hasil TF-IDF, langkah berikutnya adalah menghitung dot product (produk titik) dari kedua vektor tersebut.
2. Menghitung Magnitude: Magnitude (atau panjang) dari masing-masing vektor dihitung. Ini adalah akar kuadrat dari jumlah kuadrat dari setiap komponen vektor.
3. Menghitung Cosine Similarity: Dengan dot product dan magnitude yang telah dihitung, cosine similarity dapat dihitung dengan rumus:

   $$
   \text{cosinus}(A) = \frac{\text{sisi ketetanggaan}}{\text{sisi miring}}
   $$

Hasil dari perhitungan ini adalah nilai antara -1 dan 1. Nilai yang mendekati 1 menunjukkan bahwa kedua vektor memiliki arah yang sangat mirip, sehingga mereka sangat serupa. Sebaliknya, nilai yang mendekati -1 menunjukkan bahwa kedua vektor berada dalam arah yang berlawanan, sehingga mereka sangat tidak mirip. Nilai 0 menunjukkan bahwa kedua vektor ortogonal atau tidak memiliki kesamaan.

Dalam konteks sistem rekomendasi, item yang memiliki cosine similarity yang tinggi dengan item yang disukai oleh pengguna akan direkomendasikan, karena mereka dianggap memiliki konten yang serupa atau relevan.

Matriks similarity dari 10 film sampel:

| title                                              | Herbie Fully Loaded | Bright Lights, Big City | Death to Smoochy | Diner    | Twister  |
| -------------------------------------------------- | ------------------- | ----------------------- | ---------------- | -------- | -------- |
| Ant-Man                                            | 0.209272            | 0.000000                | 0.000000         | 0.000000 | 0.574570 |
| Twilight                                           | 0.762923            | 0.318288                | 0.120329         | 0.207233 | 0.486848 |
| Zoolander                                          | 0.314989            | 0.000000                | 0.440710         | 0.759003 | 0.000000 |
| The Alamo                                          | 0.000000            | 0.000000                | 0.000000         | 0.000000 | 0.000000 |
| Masked and Anonymous                               | 0.000000            | 0.378293                | 0.143013         | 0.246301 | 0.160530 |
| Enter the Dangerous Mind                           | 0.000000            | 0.000000                | 0.506231         | 0.000000 | 0.000000 |
| Beerfest                                           | 0.314989            | 0.000000                | 0.440710         | 0.759003 | 0.000000 |
| Soldier                                            | 0.000000            | 0.000000                | 0.000000         | 0.000000 | 0.210629 |
| Harold & Kumar Go to White Castle                  | 0.537932            | 0.000000                | 0.258060         | 0.444438 | 0.555155 |
| A Nightmare on Elm Street Part 2: Freddy's Revenge | 0.000000            | 0.000000                | 0.000000         | 0.000000 | 0.000000 |

Dapat diketahui kesamaan terbesar ada pada Twilight dan Herbie Fully Loaded dengan nilai 0.76

Hasil Rekomendasi untuk Film dengan Genre yang sama dengan The Avengers:

| title                              | genres                           |
| ---------------------------------- | -------------------------------- |
| The Hunger Games: Catching Fire    | adventure-action-science fiction |
| Ant-Man                            | science fiction-action-adventure |
| Independence Day: Resurgence       | action-adventure-science fiction |
| Captain America: The First Avenger | action-adventure-science fiction |
| Star Trek Into Darkness            | action-adventure-science fiction |

## Evaluation

Metrik evaluasi yang digunakan adalah Precision dengan formula :

    >Precision = #of recommendation that are relevant/#of item we recommend

Dari hasil rekomendasi di atas, diketahui bahwa The Avengers termasuk ke dalam kategori science fiction-action-adventure. Dari 5 item yang direkomendasikan, 5 item memiliki kategori yang sama. Artinya, precision sistem sebesar 5/5 atau 100%.

Sistem rekomendasi film berbasis genre dengan pendekatan content-based filtering ini dapat dievaluasi secara real-time dengan pengguna yang berinteraksi dengannya melalui beberapa metode seperti adanya umpan balik langsung contohnya setelah pengguna menerima rekomendasi film, sistem dapat meminta mereka untuk memberikan peringkat atau umpan balik tentang relevansi rekomendasi tersebut.

Sistem ini juga dapat dilakukan peningkatan dengan cara penggabungan pendekatan content-based filtering dengan teknik lain seperti collaborative filtering untuk meningkatkan kualitas rekomendasi.
