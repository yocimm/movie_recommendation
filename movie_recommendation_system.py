# -*- coding: utf-8 -*-
"""movie_recommendation_system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yX8CYhLN2EuAxrFY7ezNGbh9PqjJJb7h

# Proyek Recommendation System : Movie Recommendation-Content Based Filtering


*   Nama : Paramita Citra Indah Mulia
*   Email : paramitamulia@gmail.com

# Import Library yang Dibutuhkan
"""

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import matplotlib.pyplot as plt
import seaborn as sns

"""# Data Understanding"""

# Upload API Files from Kaggle
from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d tmdb/tmdb-movie-metadata

!unzip tmdb-movie-metadata.zip

df = pd.read_csv('/content/tmdb_5000_movies.csv')

df.head(3)

df.info()

"""* budget - biaya produksi film
* genre - genre film : Action, Comedy, Thriller, dll.
* homepage - link film
* id - id film
* keywords - Kata kunci atau tag yang terkait dengan film.
* original_language - Bahasa pembuatan film.
* original_title - Judul film sebelum diterjemahkan atau diadaptasi.
* overview - Deskripsi singkat film.
* popularity - Kuantitas numerik yang menentukan popularitas film.
* production_companies - Rumah produksi film.
* production_countries - Negara tempat film diproduksi.
* release_date - tanggal rilis.
* revenue - penghasilan dari film
* runtime - durasi film
* spoken_language - bahasa dalam film
* status - "Released" atau "Rumored".
* tagline - tagline film
* title - judul film
* ote_average - rating rata-rata
* vote_count - jumlah vote

# Univariate EDA
"""

language_counts = df['original_language'].value_counts()

# Mengambil 5 nilai tertinggi
top_languages = language_counts.head(5)

# Membuat bar plot
ax = sns.barplot(x=top_languages.index, y=top_languages.values)
plt.title('Top 5 Original Languages')
plt.ylabel('Count')
plt.xlabel('Language')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

plt.show()

"""Dari 4803 data, sebanyak 4505 film menggunakan Bahasa Inggris."""

genre = df['genres'].value_counts()
genre

"""Genre film terbanyak pada dataset ini adalah drama, komedi, drama-romance, comedy-romance, dan comedy-drama."""

df['production_countries'].value_counts()

"""Dari keseluruhan data, sebanyak 2977 film diproduksi oleh United States of America."""

df.describe()

"""* Budget terbesar untuk pembuatan film pada dataset ini adalah 380 juta dolar
* Penghasilan terbesar dari film sebesar 2.7 miliar dolar
* Durasi film terpanjang yaitu 338 menit

# Data Preparation
"""

#membuat dataframe baru
df2 = df[['id', 'title', 'genres']]
df2.head()

import ast

def extract_names(row):
    # Mengubah string menjadi list of dictionaries
    row_list = ast.literal_eval(row)

    # Mengambil nilai "name" dari setiap dictionary dan mengubahnya menjadi lowercase
    names = [item['name'].lower() for item in row_list]

    # Menggabungkan semua nama dengan "-"
    return '-'.join(names)

# Menggunakan fungsi apply untuk mengubah kolom
df2['genres'] = df2['genres'].apply(extract_names)

df2.head(3)

df2['id'].duplicated().sum()

"""tidak ada duplikasi data"""

df2.isnull().sum()

"""tidak ada missing value

**Pembobotan Kata**
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data cuisine
tf.fit(df2['genres'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(df2['genres'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""Nilai 4800 merupakan ukuran data dan 22 merupakan matrik  genres."""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

"""**Cosine Similarity**

menghitung derajat kesamaan (similarity degree) antar film dengan teknik cosine similarity
"""

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa title
cosine_sim_df = pd.DataFrame(cosine_sim, index=df['title'], columns=df['title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap film
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Kesamaan terbesar ada pada Twilight dan Herbie Fully Loaded dengan nilai 0.76

**Mendapatkan Rekomendasi**
"""

def recommendations(title, similarity_data=cosine_sim_df, items=df[['title', 'genres']], k=5):
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,title].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop title film agar judul film yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(title, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

"""**Rekomendasi Film Mirip The Avengers**"""

df2[df2.title.eq('The Avengers')]

# Mendapatkan rekomendasi restoran yang mirip dengan KFC
recommendations('The Avengers')

"""Dari hasil rekomendasi di atas, diketahui bahwa The Avengers termasuk ke dalam kategori science fiction-action-adventure. Dari 5 item yang direkomendasikan, 5 item memiliki kategori yang sama. Artinya, precision sistem sebesar 5/5 atau 100%."""