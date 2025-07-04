from sqlalchemy.orm import Session

from auth.utils.auth_utils import get_password_hash
from bon.models.bon import Bon
from bon.schemas.bon import BonCreate


def get_bons(db: Session):
    return db.query(Bon).all()


def get_bon(db: Session, bon_id: int):
    return db.query(Bon).filter(Bon.id == bon_id).first()

def create_bon(db: Session, bon: BonCreate):
    db_bon = Bon(
        fournisseur=str(bon.fournisseur),
        contact=bon.contact,
        montant=bon.montant,
        paid=bon.paid,
        date=bon.date
    )
    db.add(db_bon)
    db.commit()
    db.refresh(db_bon)
    return db_bon

def delete_bon(db: Session, bon_id: int):
    db_bon = db.query(Bon).filter(Bon.id == bon_id).first()
    if db_bon:
        db.delete(db_bon)
        db.commit()
    return

def update_bon(db: Session, bon_id: int, bon_data: BonCreate):
    db_bon = db.query(Bon).filter(Bon.id == bon_id).first()
    if db_bon:
        db_bon.fournisseur = bon_data.fournisseur
        db_bon.contact = bon_data.contact
        db_bon.montant = bon_data.montant
        db_bon.paid = bon_data.paid
        db_bon.date = bon_data.date
        db.commit()
        db.refresh(db_bon)
    return db_bon

def get_bons_by_fournisseur(db: Session, fournisseur: str):
    return db.query(Bon).filter(Bon.fournisseur == fournisseur).all()


