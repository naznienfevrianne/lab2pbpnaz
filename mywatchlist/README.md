README Tugas 3
HTML: http://tugas2pbpnaz.herokuapp.com/mywatchlist/html
JSON: https://tugas2pbpnaz.herokuapp.com/mywatchlist/json/
XML: https://tugas2pbpnaz.herokuapp.com/mywatchlist/xml/

1. Perbedaan JSON XML HTML
JSON adalah bagian dari syntax JavaScript untuk merepresentasikan sebuah objek, sementara XML merupakan markup language seperti HTML yang menggunakan tag structure untuk merepresentasikan item data. 
Sementara itu, walaupun HTML dan XML memiliki struktur yang serupa, HTML lebih sering digunakan untuk menampilkan data dan XML lebih sering diguunakan untuk menyimpan data. 
HTML juga tidak membawa data, HTML hanya menampilkannya, sementara JSON dan XML membawa data ke/dari database. 
2. Mengapa data delivery diperlukan dalam mengimplementasikan sebuah platform
Data delivery diimplementasikan dalam platform untuk menampilkan sebuah data dalam format yang berbeda-beda. Misal database di JSON ingin ditampilkan di website dalam format CSS, HTML maupun XML tanpa membuat file data format CSS, HTML maupun XML terlebih dahulu, maka data delivery dibutuhkan dalam implementasi tersebut. 
3. Bagaimana mengimplementasikan checklist di atas
- Membuat aplikasi baru bernama mywatchlist di proyek django tugas 2
Menjalankan cmd python manage.py startapp mywatchlist, menambahkan 'mywatchlist' di INSTALLED_APPS pada settings.py di folder project_django
- Menambahkan model mywatchlist
Menambahkan class FilmWatchlist dan mengimport mengimport models dari django.db di models.py di folder mywatchlist
- Menambahkan minimal 10 data untuk objek mywatchlist
Membuat file json berisi data film di dalam folder fixtures di folder mywatchlist
- Fitur untuk menyajikan data dalam tiga format
Membuat fungsi di views.py untuk menampilkan data dalam XML, JSON dan HTML
- Routing untuk menampilkan data dalam tiap format yang diminta.
Menambahkan path mywatchlist/ di urls.py pada folder project_django parameter fungsi di views.py yang bersesuaian
Menambahkan path html/ di urls.py pada folder mywatchlist dengan parameter fungsi di views.py yang bersesuaian
Menambahkan path json/ di urls.py pada folder mywatchlist parameter fungsi di views.py yang bersesuaian
- Deployment di heroku
Makemigrations, migrate dan loaddata di cmd. Kemudian melakukan git add, git commit dan git push. Jika deployment berhasil 
3. POSTMAN
HTML
https://drive.google.com/file/d/1mEpeqqg5Q1JomubE-tb2NqPrx7hW5TqX/view?usp=sharing
JSON
https://drive.google.com/file/d/1w9CpEhdcfA6_aLRWdmKcdKMBK7MtcPTG/view?usp=sharing
XML
https://drive.google.com/file/d/1NPIBUd4LwgkEygKz5eCUbfFwwpUOrE_n/view?usp=sharing
