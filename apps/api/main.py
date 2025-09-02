from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/models/{model_name}")
async def get_model(model_name: models.ModelName):
    if model_name is models.ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/api/posts/{post_id}")
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post:
        return {"id": post.id, "title": post.title}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
    
@app.post("/api/posts/")
async def create_post(post_info: models.PostInfo, db: Session = Depends(get_db)):
    post = models.Post(title=post_info.title)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.put("/api/posts/{post_id}")
async def update_post(post_id: int, post_info: models.PostInfo, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter_by(id=post_id)
    post = query.first
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    query.update(post_info.model_dump(), synchronize_session=False)
    db.commit()
    db.refresh(post)
    return post

