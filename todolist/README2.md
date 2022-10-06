README Tugas 5
Link website: tugas2pbpnaz.herokuapp.com/todolist/login

# Perbedaan inline, internal dan external CSS beserta kelebihan dan kekurangan
Internal: Menambahkan tag <style> dalam <head> di html. Inline CSS efektif untuk melakukan styling dalam single page. Namun, jika metode ini diimplementasikan di berbagai page, akan memakan waktu. 
External: Menghubungkan halaman web dengan file .css external yang telah dibuat di text editor. Karena berbeda dokumen, file HTML akan terlihat lebih nyaman dilihat. Selain itu, berbeda dengan inline HTML, external CSS dapat digunakan untuk berbagai page. 
Inline: Menambahkan style attribute untuk setiap tag HTML. Hal ini lebih rumit diimplementasikan karena pengembang web harus melakukan styling satu persatu untuk setiap tag. Namun, implementasi ini dapat dilakukan jika pengembang tidak punya akses terhadap file external css dan ingin memodifikasi beberapa tag HTML saja. 

# Jelaskan tag HTML5 yang kamu ketahui.
<a> -> hyperlink
<article> -> article
<body> -> body of the document
<footer> -> footer section
<form> -> form for user input

# Jelaskan tipe CSS selector yang kamu ketahui.
Elemen selector -> tag HTML sebagai selector diakses dengan nama elemen 
Id selector -> menambahkan id di tag html, dan diakses dengan #
Class selector -> menambahkan class di tag html, dan diakses dengan . 

# Mengimplementasi checklist
1. Kustomisasi template HTML pada Tugas 4
- Halaman login, register, create task
Menambahkan navbar, memberi warna pada page dengan CSS, dan menggunakan elemen-elemen dari bootstrap
- Todolist dengan cards
Menggunakan cards dari bootstrap di dalam for loop yang mengiterasi todolist
2. Responsive
- Menggunakan media query dan mengatur width untuk layar tertentu
