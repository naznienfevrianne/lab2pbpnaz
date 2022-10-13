README Tugas 6
## Jelaskan perbedaan antara asynchronous programming dan synchronous programming
Asynchronous programming adalah approach programming yang tidak terikat pada protocol I/O. Secara singkatnya, asynchronous programming emlakukan pekerjaannya tanpa harus terikat dengan proses lain, sehingga proses dapat berjalan secara independent. Sementara itu, pada synchronous programming sebuah proses yang berjalan akan ditunggu sampai selesai tereksekusi sebelum berpindah ke proses selanjutnya.
## Jelaskan maksud dari paradigma Event-Driven Programming dan sebutkan salah satu contoh penerapannya pada tugas ini
Event-driven programming adalah sebuah paradigma dimana sebuah alur program ditentukan oleh sebuah event (seperti klik pada mouse, press pada keyboard, dsb).
Salah satu contoh event-driven programming pada program ini adalah ketika press button close di modal, menggunakan attribute onclick untuk getElementbyID. 
## Jelaskan penerapan asynchronous programming pada AJAX
Asynchronous programming pada AJAX membuat halaman web dapat diperbaharui secara asynchronous tanpa harus mereload seluruh halaman dengan transfer data ke server di balik layar. Ketika sebuah event terjadi di browser, maka objek XMLHttpRequest akan dibuat dan mengirimkan HttpRequest ke server lewat internet. Server kemudian memproses HTTPRequest, membuat sebuah respons dan mengirimkan data kembali ke browser lewat internet. Kemudian, browser akan memproses data yang dikirimkan menggunakan JavaScript dan memperbaharui halaman. 
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
### AJAX GET
1. Buat view baru untuk mengembalikan data task dalam bentuk json
Membuat view baru dengan parameter request, mengambil semua objek TaskToDoList dengan filter berdasarkan user. Kemudian mereturn HTTPResponse berupa database json yang sudah diserialize.
2. Buat path todolist/json yang mengarah ke views yang sudah dibuat.
Mengimport fungsi yang sudah dibuat sebelumnya ke urls.py, kemudian membuat path baru 'json/' yang mengarah ke fungsi yang sudah diimport
3. Lakukan pengembalian task menggunakan AJAX Get
Memasukkan script link ajax, dan membuat script untuk ajax get di todolist_ajax.html. Saya membuat fungsi bernama creatingTable() yang menerapkan ajax.get dari url todolist/json yang sudah dibuat sebelumnya. Pada halaman todolist_ajax.html saya mengiterasi setiap data dan menambahkan setiap atribut dari objek TaskToDoList ke kolom yang bersesuain pada tabel yang sudah saya siapkan sebelumnya. 
### AJAX POST
1. Menambahkan button add task untuk membuka modal berisi form untuk menambahkan task.
Menggunakan button dengan modal dari bootstrap. Di dalam modal, saya memodifikasi form agar sesuai dengan form penambahan task.
2. Membuat view baru untuk menambahkan task baru ke dalam database
Membuat views baru bernama add_task dengan login_required dan csrf_exempt. Mengambil input title dan description dengan method POST dan membuat objek TaskToDoList baru, kemudian save objek TaskToDoList baru tersebut. 
3. Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
Mengimport fungsi yang sebelumnya sudah dibuat ke urls.py, kemudian membuat path 'add/' yang mengarah ke fungsi yang sudah diimport
4. Menghubungkan form yang telah dibuat di modal ke path /todolist/add
Ketika button submit di form pada modal diklik, maka akan menjalankan fungsi creatingTable() dan melakukan AJAX Post dengan url yang mengacu ke todolist/add.