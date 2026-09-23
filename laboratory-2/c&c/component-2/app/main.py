import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema import schema
from app.db import init_db

app = FastAPI()

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.on_event("startup")
async def startup_db():
    await init_db()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
