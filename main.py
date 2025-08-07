from fastapi import FastAPI

# Creación de una aplicación FastAPI
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hola Mundo"}
