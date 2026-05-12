from sqlalchemy.orm import Session
import models
import schemas


# =========================================================
# USERS
# =========================================================

def get_users(db: Session):
    return db.query(models.User).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        nama=user.nama,
        email=user.email,
        password=user.password,
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(
    db: Session,
    user_id: int,
    user: schemas.UserCreate
):
    db_user = get_user(db, user_id)

    if db_user:
        db_user.nama = user.nama
        db_user.email = user.email
        db_user.password = user.password
        db_user.role = user.role

        db.commit()
        db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)

    if db_user:
        db.delete(db_user)
        db.commit()

    return db_user


# =========================================================
# KATEGORI
# =========================================================

def get_kategori(db: Session):
    return db.query(models.Kategori).all()


def get_kategori_by_id(
    db: Session,
    kategori_id: int
):
    return db.query(models.Kategori).filter(
        models.Kategori.id == kategori_id
    ).first()


def create_kategori(
    db: Session,
    kategori: schemas.KategoriCreate
):
    db_kategori = models.Kategori(
        nama=kategori.nama
    )

    db.add(db_kategori)
    db.commit()
    db.refresh(db_kategori)

    return db_kategori


def update_kategori(
    db: Session,
    kategori_id: int,
    kategori: schemas.KategoriCreate
):
    db_kategori = get_kategori_by_id(
        db,
        kategori_id
    )

    if db_kategori:
        db_kategori.nama = kategori.nama

        db.commit()
        db.refresh(db_kategori)

    return db_kategori


def delete_kategori(
    db: Session,
    kategori_id: int
):
    db_kategori = get_kategori_by_id(
        db,
        kategori_id
    )

    if db_kategori:
        db.delete(db_kategori)
        db.commit()

    return db_kategori


# =========================================================
# PRODUK
# =========================================================

def get_produk(db: Session):
    return db.query(models.Produk).all()


def get_produk_by_id(
    db: Session,
    produk_id: int
):
    return db.query(models.Produk).filter(
        models.Produk.id == produk_id
    ).first()


def create_produk(
    db: Session,
    produk: schemas.ProdukCreate
):
    db_produk = models.Produk(
        nama=produk.nama,
        deskripsi=produk.deskripsi,
        harga=produk.harga,
        stok=produk.stok,
        foto=produk.foto,
        id_kategori=produk.id_kategori
    )

    db.add(db_produk)
    db.commit()
    db.refresh(db_produk)

    return db_produk


def update_produk(
    db: Session,
    produk_id: int,
    produk: schemas.ProdukCreate
):
    db_produk = get_produk_by_id(
        db,
        produk_id
    )

    if db_produk:
        db_produk.nama = produk.nama
        db_produk.deskripsi = produk.deskripsi
        db_produk.harga = produk.harga
        db_produk.stok = produk.stok
        db_produk.foto = produk.foto
        db_produk.id_kategori = produk.id_kategori

        db.commit()
        db.refresh(db_produk)

    return db_produk


def delete_produk(
    db: Session,
    produk_id: int
):
    db_produk = get_produk_by_id(
        db,
        produk_id
    )

    if db_produk:
        db.delete(db_produk)
        db.commit()

    return db_produk


# =========================================================
# CART
# =========================================================

def get_carts(db: Session):
    return db.query(models.Cart).all()


def get_cart_by_id(
    db: Session,
    cart_id: int
):
    return db.query(models.Cart).filter(
        models.Cart.id == cart_id
    ).first()


def create_cart(
    db: Session,
    cart: schemas.CartCreate
):
    db_cart = models.Cart(
        id_user=cart.id_user
    )

    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)

    return db_cart


def delete_cart(
    db: Session,
    cart_id: int
):
    db_cart = get_cart_by_id(
        db,
        cart_id
    )

    if db_cart:
        db.delete(db_cart)
        db.commit()

    return db_cart


# =========================================================
# DETAIL CART
# =========================================================

def get_detail_cart(db: Session):
    return db.query(models.DetailCart).all()


def get_detail_cart_by_id(
    db: Session,
    detail_id: int
):
    return db.query(models.DetailCart).filter(
        models.DetailCart.id == detail_id
    ).first()


def create_detail_cart(
    db: Session,
    detail: schemas.DetailCartCreate
):
    subtotal = detail.jumlah * detail.harga

    db_detail = models.DetailCart(
        id_cart=detail.id_cart,
        id_produk=detail.id_produk,
        jumlah=detail.jumlah,
        subtotal=subtotal
    )

    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)

    return db_detail


def update_detail_cart(
    db: Session,
    detail_id: int,
    detail: schemas.DetailCartCreate
):
    db_detail = get_detail_cart_by_id(
        db,
        detail_id
    )

    if db_detail:
        subtotal = detail.jumlah * detail.harga

        db_detail.id_cart = detail.id_cart
        db_detail.id_produk = detail.id_produk
        db_detail.jumlah = detail.jumlah
        db_detail.subtotal = subtotal

        db.commit()
        db.refresh(db_detail)

    return db_detail


def delete_detail_cart(
    db: Session,
    detail_id: int
):
    db_detail = get_detail_cart_by_id(
        db,
        detail_id
    )

    if db_detail:
        db.delete(db_detail)
        db.commit()

    return db_detail


# =========================================================
# TRANSAKSI
# =========================================================

def get_transaksi(db: Session):
    return db.query(models.Transaksi).all()


def get_transaksi_by_id(
    db: Session,
    transaksi_id: int
):
    return db.query(models.Transaksi).filter(
        models.Transaksi.id == transaksi_id
    ).first()


def create_transaksi(
    db: Session,
    transaksi: schemas.TransaksiCreate
):
    db_transaksi = models.Transaksi(
        id_user=transaksi.id_user,
        total_harga=transaksi.total_harga,
        tanggal_transaksi=transaksi.tanggal_transaksi,
        status=transaksi.status
    )

    db.add(db_transaksi)
    db.commit()
    db.refresh(db_transaksi)

    return db_transaksi


def update_transaksi(
    db: Session,
    transaksi_id: int,
    transaksi: schemas.TransaksiCreate
):
    db_transaksi = get_transaksi_by_id(
        db,
        transaksi_id
    )

    if db_transaksi:
        db_transaksi.id_user = transaksi.id_user
        db_transaksi.total_harga = transaksi.total_harga
        db_transaksi.tanggal_transaksi = transaksi.tanggal_transaksi
        db_transaksi.status = transaksi.status

        db.commit()
        db.refresh(db_transaksi)

    return db_transaksi


def delete_transaksi(
    db: Session,
    transaksi_id: int
):
    db_transaksi = get_transaksi_by_id(
        db,
        transaksi_id
    )

    if db_transaksi:
        db.delete(db_transaksi)
        db.commit()

    return db_transaksi


# =========================================================
# DETAIL TRANSAKSI
# =========================================================

def get_detail_transaksi(db: Session):
    return db.query(models.DetailTransaksi).all()


def get_detail_transaksi_by_id(
    db: Session,
    detail_id: int
):
    return db.query(models.DetailTransaksi).filter(
        models.DetailTransaksi.id == detail_id
    ).first()


def create_detail_transaksi(
    db: Session,
    detail: schemas.DetailTransaksiCreate
):
    subtotal = detail.jumlah * detail.harga

    db_detail = models.DetailTransaksi(
        id_transaksi=detail.id_transaksi,
        id_produk=detail.id_produk,
        jumlah=detail.jumlah,
        subtotal=subtotal
    )

    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)

    return db_detail


def update_detail_transaksi(
    db: Session,
    detail_id: int,
    detail: schemas.DetailTransaksiCreate
):
    db_detail = get_detail_transaksi_by_id(
        db,
        detail_id
    )

    if db_detail:
        subtotal = detail.jumlah * detail.harga

        db_detail.id_transaksi = detail.id_transaksi
        db_detail.id_produk = detail.id_produk
        db_detail.jumlah = detail.jumlah
        db_detail.subtotal = subtotal

        db.commit()
        db.refresh(db_detail)

    return db_detail


def delete_detail_transaksi(
    db: Session,
    detail_id: int
):
    db_detail = get_detail_transaksi_by_id(
        db,
        detail_id
    )

    if db_detail:
        db.delete(db_detail)
        db.commit()

    return db_detail

# =========================================================
# LOGIN
# =========================================================

def login_user(
    db: Session,
    email: str,
    password: str
):
    return db.query(models.User).filter(
        models.User.email == email,
        models.User.password == password
    ).first()