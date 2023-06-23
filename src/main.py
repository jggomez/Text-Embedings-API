from fastapi import FastAPI
import uvicorn
from apis import router

def create_app():
    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
