import strawberry
from typing import List
from app.db import get_collection
from bson.objectid import ObjectId

@strawberry.type
class Item:
    id: str
    name: str
    description: str

@strawberry.type
class Query:
    @strawberry.field
    async def items(self) -> List[Item]:
        collection = get_collection()
        results = await collection.find().to_list(100)
        return [Item(id=str(r["_id"]), name=r["name"], description=r["description"]) for r in results]

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_item(self, name: str, description: str) -> Item:
        collection = get_collection()
        result = await collection.insert_one({"name": name, "description": description})
        return Item(id=str(result.inserted_id), name=name, description=description)

schema = strawberry.Schema(query=Query, mutation=Mutation)
