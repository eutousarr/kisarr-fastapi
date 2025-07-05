from datetime import datetime
from pydantic import BaseModel


class BonBase(BaseModel):
    fournisseur: str
    contact: str
    montant: int = 0
    paid: bool = False

class BonCreate(BonBase):
    pass


class BonSchema(BonBase):
    id: int
    date: datetime | None = None  # Optional, as it can be null
    user_id: int | None = None  # Optional, as it can be null   
    

    class Config:
        from_attributes = True
