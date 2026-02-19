from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}

# TODO: Implement CRUD endpoints for items
# TODO: Add request validation and response models