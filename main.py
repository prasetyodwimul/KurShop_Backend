from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, get_db


# =========================================================
# CREATE TABLE
# =========================================================

models.Base.metadata.create_all(bind=engine)


# =========================================================
# FASTAPI
# =========================================================

app = FastAPI(
    title="KurShop API",
    version="1.0.0"
)


# =========================================================
# AUTH
# =========================================================

@app.post("/login", tags=["Auth"])
def login(
    request: schemas.Login,
    db: Session = Depends(get_db)
):
    user = crud.login_user(
        db,
        request.email,
        request.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Email atau password salah"
        )

    return {
        "message": "Login berhasil",
        "user": {
            "id": user.id,
            "nama": user.nama,
            "email": user.email,
            "role": user.role
        }
    }


# =========================================================
# USERS
# =========================================================

@app.get("/users",
         response_model=list[schemas.User],
         tags=["Users"])
def read_users(
    db: Session = Depends(get_db)
):
    return crud.get_users(db)


@app.get("/users/{user_id}",
         response_model=schemas.User,
         tags=["Users"])
def read_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = crud.get_user(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    return user


@app.post("/users",
          response_model=schemas.User,
          tags=["Users"])
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(
        db,
        user
    )


@app.put("/users/{user_id}",
         response_model=schemas.User,
         tags=["Users"])
def update_user(
    user_id: int,
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    db_user = crud.update_user(
        db,
        user_id,
        user
    )

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    return db_user


@app.delete("/users/{user_id}",
            tags=["Users"])
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    db_user = crud.delete_user(
        db,
        user_id
    )

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User tidak ditemukan"
        )

    return {
        "message": "User berhasil dihapus"
    }


# =========================================================
# KATEGORI
# =========================================================

@app.get("/kategori",
         response_model=list[schemas.Kategori],
         tags=["Kategori"])
def read_kategori(
    db: Session = Depends(get_db)
):
    return crud.get_kategori(db)


@app.get("/kategori/{kategori_id}",
         response_model=schemas.Kategori,
         tags=["Kategori"])
def read_kategori_by_id(
    kategori_id: int,
    db: Session = Depends(get_db)
):
    kategori = crud.get_kategori_by_id(
        db,
        kategori_id
    )

    if not kategori:
        raise HTTPException(
            status_code=404,
            detail="Kategori tidak ditemukan"
        )

    return kategori


@app.post("/kategori",
          response_model=schemas.Kategori,
          tags=["Kategori"])
def create_kategori(
    kategori: schemas.KategoriCreate,
    db: Session = Depends(get_db)
):
    return crud.create_kategori(
        db,
        kategori
    )


@app.put("/kategori/{kategori_id}",
         response_model=schemas.Kategori,
         tags=["Kategori"])
def update_kategori(
    kategori_id: int,
    kategori: schemas.KategoriCreate,
    db: Session = Depends(get_db)
):
    db_kategori = crud.update_kategori(
        db,
        kategori_id,
        kategori
    )

    if not db_kategori:
        raise HTTPException(
            status_code=404,
            detail="Kategori tidak ditemukan"
        )

    return db_kategori


@app.delete("/kategori/{kategori_id}",
            tags=["Kategori"])
def delete_kategori(
    kategori_id: int,
    db: Session = Depends(get_db)
):
    db_kategori = crud.delete_kategori(
        db,
        kategori_id
    )

    if not db_kategori:
        raise HTTPException(
            status_code=404,
            detail="Kategori tidak ditemukan"
        )

    return {
        "message": "Kategori berhasil dihapus"
    }


# =========================================================
# PRODUK
# =========================================================

@app.get("/produk",
         response_model=list[schemas.Produk],
         tags=["Produk"])
def read_produk(
    db: Session = Depends(get_db)
):
    return crud.get_produk(db)


@app.get("/produk/{produk_id}",
         response_model=schemas.Produk,
         tags=["Produk"])
def read_produk_by_id(
    produk_id: int,
    db: Session = Depends(get_db)
):
    produk = crud.get_produk_by_id(
        db,
        produk_id
    )

    if not produk:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return produk


@app.post("/produk",
          response_model=schemas.Produk,
          tags=["Produk"])
def create_produk(
    produk: schemas.ProdukCreate,
    db: Session = Depends(get_db)
):
    return crud.create_produk(
        db,
        produk
    )


@app.put("/produk/{produk_id}",
         response_model=schemas.Produk,
         tags=["Produk"])
def update_produk(
    produk_id: int,
    produk: schemas.ProdukCreate,
    db: Session = Depends(get_db)
):
    db_produk = crud.update_produk(
        db,
        produk_id,
        produk
    )

    if not db_produk:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return db_produk


@app.delete("/produk/{produk_id}",
            tags=["Produk"])
def delete_produk(
    produk_id: int,
    db: Session = Depends(get_db)
):
    db_produk = crud.delete_produk(
        db,
        produk_id
    )

    if not db_produk:
        raise HTTPException(
            status_code=404,
            detail="Produk tidak ditemukan"
        )

    return {
        "message": "Produk berhasil dihapus"
    }


# =========================================================
# CART
# =========================================================

@app.get("/cart",
         response_model=list[schemas.Cart],
         tags=["Cart"])
def read_cart(
    db: Session = Depends(get_db)
):
    return crud.get_carts(db)


@app.get("/cart/{cart_id}",
         response_model=schemas.Cart,
         tags=["Cart"])
def read_cart_by_id(
    cart_id: int,
    db: Session = Depends(get_db)
):
    cart = crud.get_cart_by_id(
        db,
        cart_id
    )

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart tidak ditemukan"
        )

    return cart


@app.post("/cart",
          response_model=schemas.Cart,
          tags=["Cart"])
def create_cart(
    cart: schemas.CartCreate,
    db: Session = Depends(get_db)
):
    return crud.create_cart(
        db,
        cart
    )


@app.delete("/cart/{cart_id}",
            tags=["Cart"])
def delete_cart(
    cart_id: int,
    db: Session = Depends(get_db)
):
    db_cart = crud.delete_cart(
        db,
        cart_id
    )

    if not db_cart:
        raise HTTPException(
            status_code=404,
            detail="Cart tidak ditemukan"
        )

    return {
        "message": "Cart berhasil dihapus"
    }


# =========================================================
# DETAIL CART
# =========================================================

@app.get("/detail-cart",
         response_model=list[schemas.DetailCart],
         tags=["Detail Cart"])
def read_detail_cart(
    db: Session = Depends(get_db)
):
    return crud.get_detail_cart(db)


@app.get("/detail-cart/{detail_id}",
         response_model=schemas.DetailCart,
         tags=["Detail Cart"])
def read_detail_cart_by_id(
    detail_id: int,
    db: Session = Depends(get_db)
):
    detail = crud.get_detail_cart_by_id(
        db,
        detail_id
    )

    if not detail:
        raise HTTPException(
            status_code=404,
            detail="Detail cart tidak ditemukan"
        )

    return detail


@app.post("/detail-cart",
          response_model=schemas.DetailCart,
          tags=["Detail Cart"])
def create_detail_cart(
    detail: schemas.DetailCartCreate,
    db: Session = Depends(get_db)
):
    return crud.create_detail_cart(
        db,
        detail
    )


@app.put("/detail-cart/{detail_id}",
         response_model=schemas.DetailCart,
         tags=["Detail Cart"])
def update_detail_cart(
    detail_id: int,
    detail: schemas.DetailCartCreate,
    db: Session = Depends(get_db)
):
    db_detail = crud.update_detail_cart(
        db,
        detail_id,
        detail
    )

    if not db_detail:
        raise HTTPException(
            status_code=404,
            detail="Detail cart tidak ditemukan"
        )

    return db_detail


@app.delete("/detail-cart/{detail_id}",
            tags=["Detail Cart"])
def delete_detail_cart(
    detail_id: int,
    db: Session = Depends(get_db)
):
    db_detail = crud.delete_detail_cart(
        db,
        detail_id
    )

    if not db_detail:
        raise HTTPException(
            status_code=404,
            detail="Detail cart tidak ditemukan"
        )

    return {
        "message": "Detail cart berhasil dihapus"
    }


# =========================================================
# TRANSAKSI
# =========================================================

@app.get("/transaksi",
         response_model=list[schemas.Transaksi],
         tags=["Transaksi"])
def read_transaksi(
    db: Session = Depends(get_db)
):
    return crud.get_transaksi(db)


@app.get("/transaksi/{transaksi_id}",
         response_model=schemas.Transaksi,
         tags=["Transaksi"])
def read_transaksi_by_id(
    transaksi_id: int,
    db: Session = Depends(get_db)
):
    transaksi = crud.get_transaksi_by_id(
        db,
        transaksi_id
    )

    if not transaksi:
        raise HTTPException(
            status_code=404,
            detail="Transaksi tidak ditemukan"
        )

    return transaksi


@app.post("/transaksi",
          response_model=schemas.Transaksi,
          tags=["Transaksi"])
def create_transaksi(
    transaksi: schemas.TransaksiCreate,
    db: Session = Depends(get_db)
):
    return crud.create_transaksi(
        db,
        transaksi
    )


@app.put("/transaksi/{transaksi_id}",
         response_model=schemas.Transaksi,
         tags=["Transaksi"])
def update_transaksi(
    transaksi_id: int,
    transaksi: schemas.TransaksiCreate,
    db: Session = Depends(get_db)
):
    db_transaksi = crud.update_transaksi(
        db,
        transaksi_id,
        transaksi
    )

    if not db_transaksi:
        raise HTTPException(
            status_code=404,
            detail="Transaksi tidak ditemukan"
        )

    return db_transaksi


@app.delete("/transaksi/{transaksi_id}",
            tags=["Transaksi"])
def delete_transaksi(
    transaksi_id: int,
    db: Session = Depends(get_db)
):
    db_transaksi = crud.delete_transaksi(
        db,
        transaksi_id
    )

    if not db_transaksi:
        raise HTTPException(
            status_code=404,
            detail="Transaksi tidak ditemukan"
        )

    return {
        "message": "Transaksi berhasil dihapus"
    }


# =========================================================
# DETAIL TRANSAKSI
# =========================================================

@app.get("/detail-transaksi",
         response_model=list[schemas.DetailTransaksi],
         tags=["Detail Transaksi"])
def read_detail_transaksi(
    db: Session = Depends(get_db)
):
    return crud.get_detail_transaksi(db)


@app.get("/detail-transaksi/{detail_id}",
         response_model=schemas.DetailTransaksi,
         tags=["Detail Transaksi"])
def read_detail_transaksi_by_id(
    detail_id: int,
    db: Session = Depends(get_db)
):
    detail = crud.get_detail_transaksi_by_id(
        db,
        detail_id
    )

    if not detail:
        raise HTTPException(
            status_code=404,
            detail="Detail transaksi tidak ditemukan"
        )

    return detail


@app.post("/detail-transaksi",
          response_model=schemas.DetailTransaksi,
          tags=["Detail Transaksi"])
def create_detail_transaksi(
    detail: schemas.DetailTransaksiCreate,
    db: Session = Depends(get_db)
):
    return crud.create_detail_transaksi(
        db,
        detail
    )


@app.put("/detail-transaksi/{detail_id}",
         response_model=schemas.DetailTransaksi,
         tags=["Detail Transaksi"])
def update_detail_transaksi(
    detail_id: int,
    detail: schemas.DetailTransaksiCreate,
    db: Session = Depends(get_db)
):
    db_detail = crud.update_detail_transaksi(
        db,
        detail_id,
        detail
    )

    if not db_detail:
        raise HTTPException(
            status_code=404,
            detail="Detail transaksi tidak ditemukan"
        )

    return db_detail


@app.delete("/detail-transaksi/{detail_id}",
            tags=["Detail Transaksi"])
def delete_detail_transaksi(
    detail_id: int,
    db: Session = Depends(get_db)
):
    db_detail = crud.delete_detail_transaksi(
        db,
        detail_id
    )

    if not db_detail:
        raise HTTPException(
            status_code=404,
            detail="Detail transaksi tidak ditemukan"
        )

    return {
        "message": "Detail transaksi berhasil dihapus"
    }