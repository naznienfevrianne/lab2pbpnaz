## Link Aplikasi Heroku
https://tugas2pbpnaz.herokuapp.com/katalog/

## Bagan request client ke aplikasi Django dan responnya
Bagan: https://drive.google.com/file/d/1Mq4rmP8rBd8kZGAUfaUVMxpldqBoHlL1/view?usp=sharing
Ketika terjadi HTTP request, urls.py akan memetakan (routing) request terhadap views yang bersesuaian. views.py akan mengakses models.py untuk mengambil data-data berisi instance objek dan merender template html yang akan ditampilkan di web page.

## Mengapa menggunakan virtual environment?
Untuk memisahkan project django dengan project yang lain, sehingga tidak terjadi overlapping.

## Bagaimana mengimplementasi poin2 yang diminta
1. Membuat fungsi pada views.py untuk mengambil model dan mereturn HTML
- Mengimport fungsi render dari django.shortcuts
- Mengimport class CatalogItem dari models
- Mendefinisikan function dengan parameter request
- Membuat variabel berisi semua data barang katalog (CatalogItem.objects.all)
- Membuat context (berupa dictionary) yang mempunyai key list_barang dengan value semua data barang katalog yang sudah diambil, key nama dengan nama saya dan key npm dengan NPM saya
- Membuat fungsi mereturn fungsi render dengan parameter request, katalog.html dan context (data yang diambil)

2. Membuat routing
Untuk menampilkan apa yang diminta di tugas2pbpnaz.herokuapp.com/katalog:
- Menambahkan path /katalog di project_django/urls.py pada array urlpatterns dan include(katalog.urls) -> routing ke aplikasi katalog
- Mengimport show_katalog dari katalog.views di katalog/urls.py dan menambahkan path ''  pada array urlpatternn da passing functions show_katalog

3. Memetakan data yang diambil ke HTML
- Data yang ada di variabel context pada parameter function render dapat digunakan dalam template HTML. 
- Di bawah nama, ditambahkan text bold <b> {{nama}} </b>, dimana nama yang merupakan key di dictionary context akan mereturn value yang bersesuaian. Begitupun juga dengan <b> {{npm}} </b>
- Untuk mengisi data pada tabel, kita akan mengiterasi setiap object di list_barang (yaitu semua objek di CatalogItems). Dan memanggil setiap attribute dari item tersebut untuk dimasukkan ke kolom tabel yang bersesuaian.

4. Melakukan deployment ke Heroku agar aplikasi dapat dilihat di internet
- Membuat aplikasi di herokuapp
- Membuat secrets dengan HEROKU_APP_NAME berisi nama aplikasi di heroku app dan HEROKU_API_KEY berisi API key account heroku.
- Add, push dan commit perubahan dalam folder ke repository Github, jika deployment berhasil, maka url aplikasi heroku ditambah /katalog akan menampilkan data nama, npm dan tabel data. 