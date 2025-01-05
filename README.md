# 💬 Mental Health Prediction


[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mental-health-prediction-mkbocwxrryuor2k25caqnu.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
Domain Proyek
Proyek ini berada dalam domain kesehatan mental, dengan fokus pada prediksi kondisi mental berdasarkan dataset tertentu. Solusi ini mendukung pembuatan keputusan yang lebih baik dalam konteks kesehatan masyarakat dan organisasi.

Business Understanding
Problem Statements:
-Apa yang menjadi faktor utama yang memengaruhi kesehatan mental seseorang?
-Bagaimana cara memprediksi apakah seseorang mengalami masalah kesehatan mental berdasarkan data yang tersedia?

Goals:
-Mengidentifikasi pola dalam data yang dapat memberikan wawasan tentang kesehatan mental.
-Membangun model prediksi yang dapat memprediksi kondisi mental dengan akurasi tinggi.

Solution Statements:
-Melakukan eksplorasi data untuk memahami karakteristik fitur-fitur yang tersedia.
-Membuat pipeline preprocessing data yang sesuai.
-Mengembangkan dan mengevaluasi model machine learning untuk prediksi kesehatan mental.


Data Understanding
Fitur-Fitur pada Dataset
Dataset mencakup fitur-fitur berikut:

1.Age: Usia individu (numerik).
2.Gender: Jenis kelamin (kategori).
3.Workplace Environment: Informasi tentang kondisi tempat kerja (kategori).
4.Past Mental Health History: Riwayat kesehatan mental (biner).
5.Seeking Help: Apakah individu sedang mencari bantuan untuk kesehatan mental (biner).
6.Physical Health Issues: Apakah terdapat masalah kesehatan fisik (biner).

Eksplorasi Data Analysis (EDA):
1.Distribusi Usia: Mayoritas responden berada dalam rentang usia 20-40 tahun.
2.Proporsi Gender: Dataset memiliki distribusi gender yang sedikit tidak seimbang.
3.Korelasi Fitur: Fitur "Past Mental Health History" memiliki korelasi yang signifikan terhadap label target.

Hasil Analisa Data
-Individu dengan riwayat kesehatan mental sebelumnya cenderung lebih berisiko memiliki kondisi kesehatan mental saat ini.
-Faktor lingkungan kerja juga memiliki pengaruh signifikan.

*Data Preprocessing (Data Preparation):

-Handling Missing Values: Missing values pada fitur "Gender" diisi dengan modus.
-Feature Encoding: Menggunakan one-hot encoding untuk fitur kategori.
-Scaling: Fitur numerik distandarisasi menggunakan StandardScaler.

Modeling
Model yang digunakan:
-Logistic Regression
-Random Forest Classifier
-Support Vector Machine (SVM)
Pipeline dibuat untuk menyederhanakan proses pelatihan dan evaluasi model.


*Evaluation

-Metode Evaluasi: Accuracy, Precision, Recall, dan F1-Score.
-Contoh Hasil Evaluasi:
Logistic Regression: Accuracy = 78%
Random Forest: Accuracy = 85%
SVM: Accuracy = 82%

Random Forest memberikan kinerja terbaik dengan akurasi 85%.

Simulasi (Pengujian Model):
-Model diuji pada data uji dengan distribusi yang mirip dengan data pelatihan.
-Visualisasi ROC-AUC menunjukkan kemampuan model untuk memisahkan kelas positif dan negatif dengan baik (AUC = 0.87).


Kesimpulan
Solusi Efektif:
-Random Forest Classifier adalah solusi terbaik berdasarkan evaluasi yang dilakukan.

Perluasan Penelitian:
-Menambahkan data dari sumber lain untuk meningkatkan generalisasi model.
-Menggunakan teknik NLP untuk analisis data teks tambahan, jika tersedia.

Hasil Analisa Simulasi:
-Model menunjukkan hasil prediksi yang konsisten pada data uji.
-Peningkatan akurasi mungkin terjadi dengan tuning hyperparameter lebih lanjut.


Referensi:
Dokumentasi Scikit-learn: https://scikit-learn.org
Artikel tentang kesehatan mental: https://www.who.int/mental_health

