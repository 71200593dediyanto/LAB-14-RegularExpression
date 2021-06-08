# Dedi Yanto
# 71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# Regular Expression


'''
suatu hari Gita sedang sign-up ke suatu platforrm media sosial, dan gita tertarik dengan mekanisme pembuatan password
di platform tersebut. sejak saat itu Gita ingin membuat program untuk mencari pola bagaimana  pengecekan password
yang mirip seperti aplikasi tersebut. Gita ingin pola pengecekan password tersebut adalah sebagai berikut:
1. password akan di golongkan very strong jika password terdiri dari,minimal 8 karakter, huruf besar dan huruf kecil, angka, dan karakter special seperti *,#, dll.
2. password akan di golongkan strong jika salah satu pada pilihan 1 tidak terlaksana
3. password akan di golongkan strong jika password terdiri dari, di atas sama dengan 10 karakter, huruf dan angka.
4. password akan di golongkan weak jika password terdiri dari, 8-9 karakter, huruf dan angka.
5. password akan invalid input jika panjang password tidak masuk dalam rentang 8-18 karakter
6. password tidak boleh diisikan dengan spasi

Bantulah gita untuk mewujudkan harapan untuk membuat program pengecekan password seperti diatas dengan menggunakan Regular Expression
'''


'''

Input:
password ?

Proses:
1. 
8 - 18 char
h kecil & h besar
angka 0-9
*#% ... dll
very strong
2. 
strong
3. 
char >= 10 
huruf atau angka
!= symbol
4.
8-9 char
huruf atau angka
!= symbol
5. 8 - 18 char
6. pass tidak boleh " " 


Output:

verystorng
strong
strong
weak
invalid password input

'''

# Source Code

import re
password = input("Silahkan Masukkan Password : ")

if re.match('\S''{8,18}$',password):
    if re.search('[A-Z]',password) and re.search('[a-z]',password) and re.search('[0-9]',password) and re.search('\W',password):
        print('Password Very Strong')
    elif re.search('[0-9a-zA-Z]+',password) and not(re.search('\W',password)):
        if re.match('\S{10,18}$',password):
            print("Password Strong")
        elif re.match('\S{8,9}$',password):
            print("Password Weak")
    elif re.search('A-Z',password) or re.search('[a-z]',password) or re.search('[0-9]',password) or re.search('\W',password):
        print("Password Strong")
else:
    print("Invalid Password Input")