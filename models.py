from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from database import Base


# =========================================================
# USERS
# =========================================================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    role = Column(String(20))

    cart = relationship("Cart", back_populates="user")
    transaksi = relationship("Transaksi", back_populates="user")


# =========================================================
# KATEGORI
# =========================================================

class Kategori(Base):
    __tablename__ = "kategori"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(100))

    produk = relationship("Produk", back_populates="kategori")


# =========================================================
# PRODUK
# =========================================================

class Produk(Base):
    __tablename__ = "produk"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String(100))
    deskripsi = Column(Text)
    harga = Column(Integer)
    stok = Column(Integer)
    foto = Column(String(255))

    id_kategori = Column(Integer, ForeignKey("kategori.id"))

    kategori = relationship("Kategori", back_populates="produk")

    detail_cart = relationship(
        "DetailCart",
        back_populates="produk"
    )

    detail_transaksi = relationship(
        "DetailTransaksi",
        back_populates="produk"
    )


# =========================================================
# CART
# =========================================================

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)

    id_user = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="cart")

    detail_cart = relationship(
        "DetailCart",
        back_populates="cart"
    )


# =========================================================
# DETAIL CART
# =========================================================

class DetailCart(Base):
    __tablename__ = "detail_cart"

    id = Column(Integer, primary_key=True, index=True)

    id_cart = Column(Integer, ForeignKey("cart.id"))
    id_produk = Column(Integer, ForeignKey("produk.id"))

    jumlah = Column(Integer)
    subtotal = Column(Integer)

    cart = relationship(
        "Cart",
        back_populates="detail_cart"
    )

    produk = relationship(
        "Produk",
        back_populates="detail_cart"
    )


# =========================================================
# TRANSAKSI
# =========================================================

class Transaksi(Base):
    __tablename__ = "transaksi"

    id = Column(Integer, primary_key=True, index=True)

    id_user = Column(Integer, ForeignKey("users.id"))

    total_harga = Column(Integer)

    tanggal_transaksi = Column(DateTime)

    status = Column(String(50))

    user = relationship(
        "User",
        back_populates="transaksi"
    )

    detail_transaksi = relationship(
        "DetailTransaksi",
        back_populates="transaksi"
    )


# =========================================================
# DETAIL TRANSAKSI
# =========================================================

class DetailTransaksi(Base):
    __tablename__ = "detail_transaksi"

    id = Column(Integer, primary_key=True, index=True)

    id_transaksi = Column(
        Integer,
        ForeignKey("transaksi.id")
    )

    id_produk = Column(
        Integer,
        ForeignKey("produk.id")
    )

    jumlah = Column(Integer)

    subtotal = Column(Integer)

    transaksi = relationship(
        "Transaksi",
        back_populates="detail_transaksi"
    )

    produk = relationship(
        "Produk",
        back_populates="detail_transaksi"
    )