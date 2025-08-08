from typing import Union

from fastapi import FastAPI

from models.item_model import Item

# Creación de una aplicación FastAPI
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hola Mundo"}


# Tipos de parámetros:
#  - Parámetro de ruta: {item_id} /
#  - Parámetro de consulta(opcional) ?, &: q
# http://localhost:8000/items/1000?q=mouse
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# http://localhost:8000/calculadora?operando_1=3&operando_2=4
@app.get("/calculadora")
def calcular(operando_1: float, operando_2: float):
    return {"suma": operando_1 + operando_2}


# http://localhost:8000/items/101
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}
