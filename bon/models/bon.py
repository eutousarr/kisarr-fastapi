from typing import List
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer, String, Boolean, DateTime
from core.database import Base
from datetime import datetime, timezone

# -*- coding: utf-8 -*-
class Bon(Base):
    __tablename__ = "bons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fournisseur: Mapped[str] = mapped_column(String(100), nullable=False)
    contact: Mapped[str] = mapped_column(String(64), nullable=False)
    montant: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    paid: Mapped[bool] = mapped_column(Boolean, default=False)
    date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    produits: Mapped[List["Produit"]] = relationship(back_populates="bon", cascade="all, delete-orphan")


class Produit(Base):
    __tablename__ = "produits"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), nullable=False)
    description = mapped_column(String(255), nullable=True)
    price = mapped_column(Integer, nullable=False)
    quantity = mapped_column(Integer, default=1, nullable=False)
    bon_id: Mapped[int] = mapped_column(ForeignKey("bons.id"))
    bon: Mapped["Bon"] = relationship(back_populates="produits")