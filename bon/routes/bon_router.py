from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from auth.services.auth_service import get_current_active_user
from core.database import get_db
from bon.models.bon import Bon
from bon.schemas.bon import BonSchema, BonCreate
from bon.services.bon_service import get_bons, create_bon, get_bon, delete_bon, update_bon, get_bons_by_fournisseur

bon_router = APIRouter(
    prefix='/bons',
    tags=['Bons']
)


@bon_router.get('/', response_model=list[BonSchema])
def bon_list(db: Session = Depends(get_db)):
    db_bons = get_bons(db)

    return db_bons

@bon_router.get('/{bon_id}', response_model=BonSchema)
def bon_detail(bon_id: int, db: Session = Depends(get_db)):
    db_bon = get_bon(db, bon_id)
    if db_bon is None:
        raise HTTPException(status_code=404, detail="Bon not found")

    return db_bon

@bon_router.delete('/{bon_id}')
def bon_delete(bon_id: int, db: Session = Depends(get_db)):
    db_bon = get_bon(db, bon_id)
    if db_bon is None:
        raise HTTPException(status_code=404, detail="Bon not found")

    delete_bon(db, db_bon.id)
    return {"message": "Bon deleted"}

@bon_router.post("/", response_model=BonSchema)
def bon_post(bon: BonCreate, db: Session = Depends(get_db)):
    return create_bon(db, bon)

@bon_router.put("/{bon_id}", response_model=BonSchema)
def bon_update(bon_id: int, bon_data: BonCreate, db: Session = Depends(get_db)):
    db_bon = update_bon(db, bon_id, bon_data)
    if db_bon is None:
        raise HTTPException(status_code=404, detail="Bon not found")
    return db_bon

@bon_router.get('/{fournisseur}', response_model=list[BonSchema])
def get_bons_by_fournisseur_route(fournisseur: str, db: Session = Depends(get_db)):
    db_bons = get_bons_by_fournisseur(db, fournisseur)
    if not db_bons:
        raise HTTPException(status_code=404, detail="No bons found for this fournisseur")
    
    return db_bons
