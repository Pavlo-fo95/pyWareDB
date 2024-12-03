from fastapi import FastAPI
from database import Base, engine
from routers import product_router

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

# Создание приложения FastAPI
app = FastAPI(title="Warehouse Inventory API", version="1.0.0")

# Подключение маршрутизатора
app.include_router(product_router, prefix="/products", tags=["Products"])