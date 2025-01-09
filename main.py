from typing import Union

from fastapi import FastAPI

app = FastAPI()




db={}
'''
CREATE
READ
UPDATE
DELETE
'''


#@app.get("/")
#def read_root():
#    return {"Hello": "World"}


@app.post("/items")
def create_items():
    text = "creado con exito"
    db[1] = text
    return "Creado con python"

@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
def read_item(item_id: int):
    #return {"item_id": item_id, "q": q}
    item = db.get(item_id)
    return {"item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int,new_text: str= ""):

    item = db.get(item_id)

    if not item:
        raise HTTPException(status_code=404,detail="Item not found")
   
    db[item_id] = new_text
    return {"item": item}



@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    db.pop(item_id)
    return {"item":item_id}