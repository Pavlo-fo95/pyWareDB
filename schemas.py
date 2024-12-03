from pydantic import BaseModel
from datetime import date

# Базовая схема товара
class ProductBase(BaseModel):
    name: str
    category: str
    quantity: int
    price: float
    supplier: str
    arrival_date: date

# Схема для создания товара
class ProductCreate(ProductBase):
    pass

# Схема для чтения товара
class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True