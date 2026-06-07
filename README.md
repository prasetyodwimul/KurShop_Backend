Iya, kepisah karena di dalam README ada kode blok lagi pakai ```sehingga tampilannya pecah. Ini versi **satu canvas kode utuh**, aman buat langsung copy paste ke`README.md`.

````md
# 🛒 KurShop Android App

KurShop adalah aplikasi mobile sederhana berbasis Android untuk proses belanja online. Aplikasi ini dibuat menggunakan **Android Studio** dengan bahasa **Kotlin** dan terhubung ke backend melalui **REST API** menggunakan **Retrofit**.

Aplikasi ini memiliki dua jenis pengguna, yaitu **User** dan **Admin**. User dapat melihat produk, menambahkan produk ke keranjang, melakukan checkout, melihat invoice, serta melihat riwayat transaksi. Admin dapat mengelola produk, kategori, user, transaksi, dan melihat laporan pendapatan.

---

## 🔗 Repository Backend

Backend KurShop dibuat menggunakan Python dan tersedia pada repository berikut:

```bash
https://github.com/prasetyodwimul/KurShop_Backend
```

---

## 📱 Tampilan Aplikasi

> Tambahkan screenshot aplikasi pada bagian ini.

### Halaman Login

![Login](docs/login.png)

### Dashboard User

![Dashboard User](docs/dashboard-user.png)

### Keranjang Belanja

![Cart](docs/cart.png)

### Invoice Transaksi

![Invoice](docs/invoice.png)

### Dashboard Admin

![Dashboard Admin](docs/dashboard-admin.png)

---

## 🚀 Fitur Aplikasi

### 👤 Fitur User

- Login dan register akun
- Menampilkan daftar produk
- Mencari produk berdasarkan nama atau deskripsi
- Filter produk berdasarkan kategori
- Melihat detail produk
- Menambahkan produk ke keranjang
- Mengubah jumlah produk pada keranjang
- Checkout pesanan
- Menampilkan invoice atau struk transaksi
- Melihat riwayat transaksi
- Membatalkan pesanan dengan status pending
- Badge jumlah item pada keranjang
- Loading state dan empty state

---

### 🛠️ Fitur Admin

- Dashboard admin
- Menampilkan jumlah produk, transaksi, dan user
- Menambah produk
- Mengedit produk
- Menghapus produk
- Mencari produk pada halaman admin
- Menampilkan status stok produk
- Mengelola kategori
- Melihat daftar user
- Melihat daftar transaksi
- Filter transaksi berdasarkan status
- Update status transaksi
- Melihat detail transaksi
- Menampilkan total pendapatan dari transaksi selesai
- Loading state dan empty state

---

## 🧰 Teknologi yang Digunakan

- Android Studio
- Kotlin
- XML Layout
- Retrofit
- RecyclerView
- Material Components
- REST API
- Python Backend
- Database

---

## 🏗️ Struktur Project

```text
app/
├── java/com/example/kurshop/
│   ├── adapter/
│   ├── api/
│   ├── model/
│   ├── ui/admin/
│   ├── AdminDashboardActivity.kt
│   ├── UserDashboardActivity.kt
│   ├── LoginActivity.kt
│   ├── RegisterActivity.kt
│   ├── CartActivity.kt
│   ├── CheckoutActivity.kt
│   ├── InvoiceActivity.kt
│   └── RiwayatTransaksiActivity.kt
│
└── res/
    ├── layout/
    ├── drawable/
    ├── menu/
    └── values/
```

---

## 🔌 Integrasi API

Aplikasi Android KurShop terhubung dengan backend menggunakan Retrofit. Backend berfungsi untuk mengelola data produk, kategori, user, transaksi, detail transaksi, upload foto, dan update stok.

Base URL API diatur pada file:

```text
RetrofitClient.kt
```

Contoh konfigurasi:

```kotlin
private const val BASE_URL = "http://192.168.x.x:8000/"
```

Pastikan alamat IP backend sudah sesuai dengan server yang sedang dijalankan.

---

## ⚙️ Cara Menjalankan Project

### 1. Clone Repository Android

```bash
git clone https://github.com/username/KurShop_Android.git
```

> Ganti `username/KurShop_Android` dengan repository Android kamu.

---

### 2. Buka Project di Android Studio

Buka Android Studio, lalu pilih:

```text
Open Project > Pilih folder KurShop Android
```

---

### 3. Jalankan Backend

Clone dan jalankan backend dari repository berikut:

```bash
git clone https://github.com/prasetyodwimul/KurShop_Backend
```

Lalu jalankan backend sesuai instruksi pada repository backend.

---

### 4. Sesuaikan Base URL

Ubah alamat backend pada file `RetrofitClient.kt`.

Contoh jika menggunakan jaringan WiFi lokal:

```kotlin
private const val BASE_URL = "http://192.168.1.10:8000/"
```

Jika menggunakan emulator Android, sesuaikan alamat server dengan konfigurasi jaringan yang digunakan.

---

### 5. Jalankan Aplikasi

Klik tombol **Run** pada Android Studio, lalu pilih emulator atau perangkat Android.

---

## 🔄 Alur Penggunaan User

```text
Login / Register
        ↓
Dashboard User
        ↓
Pilih Produk
        ↓
Tambah ke Keranjang
        ↓
Checkout
        ↓
Invoice
        ↓
Riwayat Transaksi
```

---

## 🔄 Alur Penggunaan Admin

```text
Login Admin
        ↓
Dashboard Admin
        ↓
Kelola Produk / Kategori / User
        ↓
Kelola Transaksi
        ↓
Update Status Transaksi
        ↓
Lihat Laporan Pendapatan
```

---

## 📦 Data yang Dikelola

Aplikasi KurShop mengelola beberapa data utama, yaitu:

- User
- Produk
- Kategori
- Transaksi
- Detail Transaksi
- Stok Produk
- Foto Produk

---

## 🧪 Pengujian Fitur

Beberapa fitur yang dapat diuji:

| No  | Fitur                   | Status   |
| --- | ----------------------- | -------- |
| 1   | Login User              | Berjalan |
| 2   | Register User           | Berjalan |
| 3   | Menampilkan Produk      | Berjalan |
| 4   | Search Produk           | Berjalan |
| 5   | Filter Kategori         | Berjalan |
| 6   | Tambah ke Keranjang     | Berjalan |
| 7   | Checkout                | Berjalan |
| 8   | Invoice                 | Berjalan |
| 9   | Riwayat Transaksi       | Berjalan |
| 10  | Dashboard Admin         | Berjalan |
| 11  | CRUD Produk             | Berjalan |
| 12  | Filter Transaksi        | Berjalan |
| 13  | Update Status Transaksi | Berjalan |

---

## ⚠️ Catatan Penting

- Backend harus dijalankan terlebih dahulu sebelum aplikasi Android digunakan.
- Pastikan perangkat Android dan laptop berada dalam jaringan yang sama jika menggunakan IP lokal.
- Jika gambar produk tidak muncul, cek URL gambar dan folder upload pada backend.
- Jika API tidak terbaca, cek kembali konfigurasi `BASE_URL`.
- Jika menggunakan emulator, pastikan alamat server sesuai dengan konfigurasi emulator.

---

## 📌 Pengembangan Selanjutnya

Beberapa fitur yang dapat dikembangkan ke depannya:

- Payment gateway
- Share invoice ke WhatsApp
- Cetak invoice ke PDF
- Edit profil user
- Grafik pendapatan admin
- Produk terlaris
- Autentikasi menggunakan token
- Notifikasi status pesanan

---

## 👨‍💻 Pengembang

**Nama:** Bilal Rizky | M. Farrel Krisnanegara | M. Pasya Pramudya | M. Rendy Breventa | Mutia Saladina | Prasetyo Dwi Mulyono  
**Project:** KurShop Android App  
**Backend:** KurShop Backend  
**Repository Backend:** https://github.com/prasetyodwimul/KurShop_Backend

---

## 📄 Lisensi

Project ini dibuat untuk kebutuhan pembelajaran dan praktikum pengembangan aplikasi mobile.
````
