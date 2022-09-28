README Tugas 4
Halaman tabel task: http://tugas2pbpnaz.herokuapp.com/todolist 
Halaman login: http://tugas2pbpnaz.herokuapp.com/todolist/login
Halaman registrasi akun: http://tugas2pbpnaz.herokuapp.com/todolist/register
Halaman pembuatan task: http://tugas2pbpnaz.herokuapp.com/todolist/create-task 
Halaman logout: http://tugas2pbpnaz.herokuapp.com/todolist/logout

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF token adalah sebuah token random yang bertujuan untuk menghindari Cross Site Request Forgery attack. Token ini bersifat unik tiap user session dan merupakan nilai random yang sulit ditebak. Jika tidak ada potongan kode tersebut, form tidak terproteksi dari CSRF karena attacker tidak perlu menebak token untuk menjebak user dalam mengirim valid request.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti) {{ form.as_table }}? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Kita dapat membuat elemen form secara tabel. Gambaran besar dalam membuat form adalah dalam blok <form> kita membuat label, input dan tombol submit secara manual. 

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML
Pertama saya membuat class form TaskForm yang merupakan ModelForm. Kemudian saya membuat attribute untuk TaskForm tersebut, yaitu title dan description yang merupakan charField dan date yang otomatis di-set dengan tanggal submit input ke form. Kemudian di dalam class TaskForm saya membuat class di dalamnya yaitu, class Meta. Dimana di dalam class Meta saya membuat attribute model yang bernilai model TaskToDoList yang sudah dibuat sebelumnya, dan fields berupa array berisi string-string nama attribute di TaskToDoList.

Kemudian pada views.py, saya mengimport TaskForm yang sudah saya buat. Setelah itu, saya membuat function create_task dengan parameter request. Jika request method adalah POST, saya akan membuat TaskForm dengan parameter request.POST tersebut. Jika form valid, saya akan membuat menyimpan input ke database. Kemudian fungsi tersebut akan return fungsi render dengan parameter request, create_task.html dan context yang berupa dictionary berisi form tersebut. 

Di HTML create_task.html saya akan membuat form. Dalam blok form saya menggunakan csrf token dan form.as_p dalam membuat form secara otomatis. Kemudian saya juga akan membuat button yang akan mengembalikan user ke halaman. 

Di HTML show_todolist saya akan membuat tabel berisi creation date, title dan description. Untuk menampilkan task sesuai user yang menginputnya saya menggunakan blok if user == task.user.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist yang diminta
1. Membuat aplikasi baru todolist
Menjalankan cmd python manage.py startapp mywatchlist, menambahkan 'todolist' di INSTALLED_APPS pada settings.py di folder project_django

2. Menambahkan path todolist
- Menambahkan path /todolist di project_django/urls.py pada array urlpatterns dan include(todolist.urls) 

3. Membuat model task dengan atribut yang ditentukan
Membuat class FilmWatchlist dan mengimport models dari django.db di models.py di folder todolist. Kemudian melakukan migrations lewat cmd.

4. Mengimplementasi form registrasi, login dan logout
Membuat fungsi untuk registrasi, login dan logout. 
Fungsi untuk register -> menerima parameter request, membuat instance user creation form, save data dari form, redirect ke login dan render dengan parameter request, register.html dan context yang berupa dictionary berisi form.
Fungsi untuk login -> menerima parameter request, get username dan password, kemudian authenticate user berdasarkan username dan password. Jika user ditemukan, maka login berasil dan akan menuju halaman todolist. Kemudian akan dilakukan render dengan parameter request, login.html dan context yang berupa dictionary berisi form. Jika user tidak ditemukan, akan memberikan message.
Fungsi untuk logout -> menerima parameter request, menjalankan fungsi logout, menuju halaman login dan mendelete cookie last_login

5. Memuat halaman todolist dengan username pengguna, tombol tambah task baru, tombol logout dan tabel berisi tanggal pembuatan task, judul task dan deskripsi task
- Menampilkan username dengan {{user}}
- Membuat tabel untuk tanggal, deskripsi dan judul task. Mengiterasi setiap list_task dan memeriksa apakah user yang sedang login sama dengan user yang merupakan attribute task, jika sama, maka task akan ditampilkan.
- Membuat tombol logout dengan <button> dan href ke halaman logout
- Membuat halaman tombol tambah task baru dengan <button> dan href ke halaman create-task

6. Membuat halaman form untuk pembuatan task. Data yang diinput hanya judul task dan deskripsi task.
Pertama saya membuat class form TaskForm yang merupakan ModelForm. Kemudian saya membuat attribute untuk TaskForm tersebut, yaitu title dan description yang merupakan charField dan date yang otomatis di-set dengan tanggal submit input ke form. Kemudian di dalam class TaskForm saya membuat class di dalamnya yaitu, class Meta. Dimana di dalam class Meta saya membuat attribute model yang bernilai model TaskToDoList yang sudah dibuat sebelumnya, dan fields berupa array berisi string-string nama attribute di TaskToDoList.

Kemudian pada views.py, saya mengimport TaskForm yang sudah saya buat. Setelah itu, saya membuat function create_task dengan parameter request. Jika request method adalah POST, saya akan membuat TaskForm dengan parameter request.POST tersebut. Jika form valid, saya akan membuat menyimpan input ke database. Kemudian fungsi tersebut akan return fungsi render dengan parameter request, create_task.html dan context yang berupa dictionary berisi form tersebut.

Di HTML create_task.html saya akan membuat form. Dalam blok form saya menggunakan csrf token dan form.as_p dalam membuat form secara otomatis. Kemudian saya juga akan membuat button yang akan mengembalikan user ke halaman. 


7. Membuat routing sehingga beberapa fungsi yang sudah ditentukan dapat diakses melalui URL
- Mengimport fungsi2 di views.py dan membuat routing untuk masing2 fungsi, yaitu login, register, logout dan create-task di urls.py pada folder todolist

8. Melakukan deployment ke Heroku
Melakukan git add, git commit dan git push, jika deployment berhasil maka website sudah dapat digunakan.

9. Membuat dua akun pengguna dan tiga dummy data task pada akun masing-masing di situs web heroku. 
Membuat dua akun pengguna lewat register di website. Kemudian login di setiap akun dan menambahkan data lewat page create-task