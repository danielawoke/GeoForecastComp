import strawberry
import typing
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# an object is made with this class, and we can mark it with strawberry as a type
@strawberry.type
class User:
    name: str
    word:int

@strawberry.type
class UserList:
    userList: typing.List[User]

lst = []
for i in range(0,100):
    lst.append(User(name = "okay"+str(i), word = i))

# this function is the resolver, it is what we use to then return what value we need
def allData() -> typing.List[User]:
    return lst
# This right here is is the selling point of graphQL, if you make these large, 
# deeply nested data strucutres that are defined by the schema
# you can easily make requests for the subdata contained inside of them with a request

@strawberry.type
class Query:
    last_user: typing.List[User] = strawberry.field(resolver=allData)
  


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


class Item(BaseModel):
    name: str
    


@app.post("/postRequest/")
async def create_item(item: Item):
    uri = "mongodb+srv://dawoke:Bluebear1%3F123@cluster0.oyu906n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return item.name


