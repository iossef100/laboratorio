from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    nome = "Iossef"
    return {"message": f" Hello World {nome}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}