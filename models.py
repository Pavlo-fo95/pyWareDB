from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

# Модель товара
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    category = Column(String, index=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    supplier = Column(String, nullable=True)
    arrival_date = Column(Date, nullable=False)