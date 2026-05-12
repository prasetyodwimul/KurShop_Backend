from pydantic import BaseModel
from datetime import datetime


# =========================================================
# USERS
# =========================================================

class UserBase(BaseModel):
    nama: str
    email: str
    password: str
    role: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# =========================================================
# KATEGORI
# =========================================================

class KategoriBase(BaseModel):
    nama: str


class KategoriCreate(KategoriBase):
    pass


class Kategori(KategoriBase):
    id: int

    class Config:
        from_attributes = True


# =========================================================
# PRODUK
# =========================================================

class ProdukBase(BaseModel):
    nama: str
    deskripsi: str
    harga: int
    stok: int
    foto: str
    id_kategori: int


class ProdukCreate(ProdukBase):
    pass


class Produk(ProdukBase):
    id: int

    class Config:
        from_attributes = True


# =========================================================
# CART
# =========================================================

class CartBase(BaseModel):
    id_user: int


class CartCreate(CartBase):
    pass


class Cart(CartBase):
    id: int

    class Config:
        from_attributes = True


# =========================================================
# DETAIL CART
# =========================================================

class DetailCartBase(BaseModel):
    id_cart: int
    id_produk: int
    jumlah: int


class DetailCartCreate(DetailCartBase):
    harga: int


class DetailCart(DetailCartBase):
    id: int
    subtotal: int

    class Config:
        from_attributes = True


# =========================================================
# TRANSAKSI
# =========================================================

class TransaksiBase(BaseModel):
    id_user: int
    total_harga: int
    tanggal_transaksi: datetime
    status: str


class TransaksiCreate(TransaksiBase):
    pass


class Transaksi(TransaksiBase):
    id: int

    class Config:
        from_attributes = True


# =========================================================
# DETAIL TRANSAKSI
# =========================================================

class DetailTransaksiBase(BaseModel):
    id_transaksi: int
    id_produk: int
    jumlah: int


class DetailTransaksiCreate(DetailTransaksiBase):
    harga: int


class DetailTransaksi(DetailTransaksiBase):
    id: int
    subtotal: int

    class Config:
        from_attributes = True

# =========================================================
# LOGIN
# =========================================================

class Login(BaseModel):
    email: str
    password: str