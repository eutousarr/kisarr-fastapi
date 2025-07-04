from pydantic import BaseModel


class BonBase(BaseModel):
    fournisseur: str
    contact: str
    montant: int = 0
    paid: bool = False
    date: str  # ISO format date string


class BonCreate(BonBase):
    password: str


class BonSchema(BonBase):
    id: int

    class Config:
        from_attributes = True
