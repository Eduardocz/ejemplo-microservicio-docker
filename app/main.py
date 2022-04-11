from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {'products': ['Kobe Bryant jersey',
                        'LeBron James jersey',
                        'Rajon Rondo jersey',
                        'Dwayne Wade jersey']}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}