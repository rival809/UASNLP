# Indodax Apps Review on Google Play Store Scraping and Text Analytics (Sentiment Analysis)

Project ini dibuat untuk memenuhi tugas akhir mata kuliah NLP pada Universitas Pendidikan Indonesia Kampus Purwakarta
</br>
Project Team :

- Muhammad Felmi Adhiarahman
- Rival Ramadhan

</br>

Project ini merupakan Sentiment Analysis yang mencakup :

- Scraping data dari Google Play Store
- Sampling Data
- Sentiment Analysis

</br>

Dokumentasi penggunaan project dapat dilihat pada konten dibawah ini :

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Content</summary>
  <ol>
    <li><a href="#about">About The Project</a></li>
      <ul>
        <li><a href="#bg">Background</a></li>
        <li><a href="#pps">Purpose</a></li>
      </ul>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#objective">Objective</a></li>
    <li><a href="#projectstructure">Project Structure</a></li>
    <li><a href="#metrics">Metrics</a></li>
    <li><a href="#evaluation">Evaluation</a></li>
  </ol>
</details>
</br>
</br>
</br>

</hr>

<h1 id="about">1. About Project</h1>
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Logo_Indodax.png" alt="Logo Indodax"/>
  <h2 id="bg">Background</h2>
    <div><p align="justify">Belakangan ini Cryptocurrency sedang banyak digemari di kalangan masyarakat Indonesia dengan tujuan yang bermacam - macam, ada yang hanya sekedar menabung sebagai media berinvestasi, hingga juga pencarian keuntungan dalam jangka waktu yang cepat (scalping). Untuk melakukan pembelian crypto, masyarakat tentunya diharuskan menggunakan suatu exchange atau aplikasi tempat menjual belikan crypto yang tentunya harus sudah memiliki izin secara resmi dari OJK Indonesia. Salah satu exchange terkenal dan mudah untuk digunakan yakni Indodax. Namun siapa sangka bahwa exchanger resmi sekalipun masih memiliki beberapa kekurangan sehingga menimbulkan pro dan kontra yang terjadi di masyarakat. Maka dari itu sentiment analisis dilakukan untuk melakukan pengukuran sentiment dari opini masyarakat yang tersebar dalam review google playstore.</p></div>

  </br>

  <h2 id="pps">Purpose</h2>
    Project ini dibuat untuk memenuhi tugas akhir mata kuliah NLP. Project ini berfungsi sebagai acuan untuk melihat seberapa besar sentimen yang dihasilkan berdasarkan opini masyarakat yang diambil dari review pada suatu aplikasi di Google Play Store. Pada kasus kali ini, kami mengambil aplikasi Indodax karena merupakan aplikasi exchanger cryptocurrency yang saat ini paling banyak digunakan oleh masyarakat di Indonesia. Namun tentunya aplikasi yang ingin dilihat sentimennya, dapat kita ubah sesuai dengan keinginan.

</br>
<h1 id="getting-started">2. Getting Started</h1>
  <h2 id="pre">Prerequisites</h2>
    Bahasa yang digunakan dalam melakukan pembuatan project ini merupakan  Python v.3.9.7  yang dibangun diatas virtual environment Anaconda. Library dan dependency yang dibutuhkan dapat di lihat pada [requirements.txt](https://github.com/rival809/UASNLP/blob/master/requirements.txt)
  </br>
  </br>
  <h2 id="tools">Tools</h2>
    Tools yang digunakan dalam melakukan pembuatan project ini antara lain :

    - Visual Studio Code / Google Colaboratory
      Merupakan IDE yang digunakan untuk melakukan penulisan code menggunakan bahasa python

    - Google Spreadsheet
      Digunakan sebagai tools untuk melakukan cleaning data, dan data labeling secara manual

    - Anaconda
      Digunakan sebagai package manager yang berfungsi untuk membangun sebuah virtual environtment

</br>

  <h2 id="install">Installation</h2>
    Hal yang harus dipersiapkan untuk menjalankan project ini yaitu :
    
    1. Melakukan instalasi IDE Visual Studio Code sebagai tools yang akan digunakan dalam melakukan pembuatan code. Jika tidak maka bisa menggunakan Google Colab secara online
    2. Download / Clone project ini ke dalam local storage pada PC anda
    3. Buka folder menggunakan IDE Visual Studio Code
    4. Atur kernel menggunakan virtual environtment bawaan yang sudah terintegrasi dengan Anaconda
    5. Buka terminal dalam Visual Studio Code dan lakukan instalasi requirements dengan command 
      `pip install -r requirements.txt`

  <h2 id="usage">Usage</h2>
    Berikut merupakan panduan penjelasan untuk menjalankan project ini, terdapat beberapa tahapan yang harus dilakukan dimulai dari melakukan penarikan data, pembersihan data, sampling data, labeling data, preprocessing data, dan penarikan kesimpulan / sentimen analisis. Tahapan tersebut antara lain adalah :

    A. Melakukan penarikan data
      1. Cari aplikasi pada Google Play Store yang akan ditarik datanya, lalu copy application package dari aplikasi tersebut
      2. Buka file scraping.py atau nptebook NLP_Google_Play_Review_Data_Scraper.ipnyb pada folder src
      3. Apabila ingin mengganti atau menambahkan aplikasi yang akan di ambil datanya, silahkan tambahkan application package yang sudah didapat pada parameter yang sudah disediakan > app_packages
      4. Jalankan script tersebut sampai data berhasil tersimpan ke dalam folder output dengan format file csv

    B. Melakukan preprocessing data
      1. Buka file NLP_Sentimen_Analisis.ipynb
      2. Jalankan proses Load Data, dan juga Preprocessing data
      3. Hidupkan baris code yang berfungsi untuk menyimpan data yang telah dibersihkan ke dalam bentuk csv
      4. Ambil data pada column "Content" dan simpan dalam format file txt

    C. Melakukan sampling data
      1. Untuk melakukan sampling data pastikan data hasil scraping sudah sesuai rename dengan format Data Scraper - Indodax.csv dan simpan di folder data
      2. Lalu jalankan sampling.py atau buka notebook NLP_Sampling_Data.ipnyb untuk melakukan sampling
      3. Untuk mengatur jumlah sample yang diambil, silahkan buka samplng.py dengan text editor dan atur pada parameter BANYAK_SAMPLE_DATA.
      4. Secara default sampling menggunakan method `sample` dari library `pandas` sebanyak 700 data.

    D. Melakukan labeling data
      1. Buka file hasil dari sampling data dalam format csv menggunakan excel maupun Google Spreadsheet
      2. Pada column sentiment, silahkan berikan label sentiment secara manual berdasarkan terkaan anda dengan nilai yang telah ditentukan.
      (0 = Negatif, 1 = Netral, 2 = Positif.)
      3. Simpan file tersebut ke dalam bentuk csv

    E. Melakukan sentimen analisis
      1. Buka kembali file NLP_Sentimen_Analisis.ipynb
      2. Lanjutkan running baris kode setelah proses preprocessing
      3. Tunggu hingga proses selesai
      4. Akurasi dari beberapa model akan muncul
      5. Gunakan model dengan akurasi tertinggi untuk melakukan sentimen analisis
      4. Output berupa hasil sentimen, dan Trained model akan tersimpan

<h1 id="objective">3. Objective</h1>

    1. Sistem dapat menarik data sesuai dengan aplikasi yang telah didefinisikan.
    2. Sistem dapat melakukan pengukuran akurasi berdasarkan berbagai classifier.
    2. Sistem dapat menampilkan sentimen review aplikasi yang diberikan.

<br/>

<h1 id="projectstructure">4. Project Structure</h1>
  <ol>
    <li>Data</li>
      Data yang digunakan merupakan data hasil scrapping menggunakan file NLP_Google_Play_Review_Data_Scraper.ipynb dan atau scraping.py
      Untuk menentukan aplikasi yang akan ditarik datanya maka perlu dikonfigurasikan nama package aplikasi sesuai dengan yang diinginkan. Untuk merubahnya hanya perlu mengganti baris kode pada baris berikut ini

      app_packages = [
    'id.co.bitcoin',
      ]

Data yang diperoleh dari hasil scraping merupakan file dalam format .csv yang berjumlah sekitar 1200 data.
Setelah data berhasil kita dapatkan, lalu tahapan selanjutnya yaitu cleaning data, yang dapat kita lakukan dengan menjalankan fungsi text preprocessing yang mencakup text cleaning dengan regex, stemmer, stopword, tokenizer, dan juga vectorization.

  <li>Model</li>
    Pemodelan dilakukan menggunakan beberapa classifier dari metode machine learning dengan pembagian dataset untuk data train sebanyak 80% dan data test sebanyak 20% yang menghasilkan akurasi berikut ini :

    Akurasi dari Decision Tree Classifier :  50%
    Akurasi dari Logistic Regression :  64%
    Akurasi dari Random Forest Classifier :  64%
    Akurasi dari SVM :  65%
    Akurasi dari Naive Bayes :  66%

Model dengan akurasi yang paling tinggi lalu akan digunakan untuk menentukan sentiment analisis pada tahap selanjutnya

  <li>Output</li>
  Tahapan selanjutnya adalah prediction, dimana model yang telah difitting tadi lalu digunakan sebagai acuan untuk melakukan prediksi, sehingga dihasilkan sentimen sebagai berikut :

  <img src="output\hasil_sentimen.png" alt="Hasil sentimen"/>

Hasil prediksi sentimen yang didapatkan untuk review aplikasi Indodax adalah :

    Positif = (404) 33,7%
    Netral = (539) 45%
    Negatif = (256) 21,3%

  <li>Parameter</li>
  <li>Source</li>
  Berisi notebook projek
  </ol>

<br/>

<h1 id="metrics">5. Metrics</h1>
  <div><p align="justify">1. Accuracy.</p></div>
    Metric atau pengukuran yang kami gunakan dalam project ini yaitu akurasi. Accuracy didefinisikan sebagai tingkat kedekatan antara nilai prediksi dengan nilai aktual. Dikarenakan dalam project ini sangat diperlukan tingkat prediksi yang baik demi mendapatkan hasil prediksi yang tepat, maka tentunya akurasi merupakan metrik yang cocok untuk digunakan.
<br/>

<h1 id="evaluation">6. Evaluation</h1>
<div><p align="justify">Data yang diperoleh dari hasil scraping merupakan file dalam format .csv yang berjumlah sekitar 1200 data dan 700 digunakan sebagai data sampling</div>
