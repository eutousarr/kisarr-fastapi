from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer, String, Boolean, DateTime
from core.database import Base
from datetime import datetime, timezone

# -*- coding: utf-8 -*-
class Bon(Base):
    __tablename__ = "bons"

    id = mapped_column(Integer, primary_key=True)
    fournisseur = mapped_column(String(100), nullable=False)
    contact = mapped_column(String(64), nullable=False)
    montant = mapped_column(Integer, default=0, nullable=False)
    paid = mapped_column(Boolean, default=False)
    date = mapped_column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    produits = relationship("Produit", back_populates="bon", cascade="all, delete-orphan")


class Produit(Base):
    __tablename__ = "produits"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), nullable=False)
    description = mapped_column(String(255), nullable=True)
    price = mapped_column(Integer, nullable=False)
    quantity = mapped_column(Integer, default=1, nullable=False)
    bon_id = mapped_column(ForeignKey("bons.id"))
    bon = relationship("Bon", back_populates="produits")