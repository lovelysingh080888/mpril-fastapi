from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from app.services.workout import WorkoutService
from common.config.database import configure_database
from app.graphql.schemas.schema import WorkoutInput
from app.graphql.resolvers.mutation import Mutation
from app.graphql.resolvers.query import Query
from strawberry.fastapi import GraphQLRouter
import uvicorn
import strawberry

# Initializing instance
app = FastAPI(title="Workout APIs", version="1.0.0")


# Configure the database engine
@app.on_event("startup")
async def startup_event():
    configure = configure_database()
    app.mongodb_client = await configure()
 
    
# Configure the database engine
@app.on_event("shutdown")
async def shutdown():
    app.app.mongodb_client.close()
    
schema = strawberry.Schema(query = Query, mutation = Mutation)
graphql_app = GraphQLRouter(schema=schema)

app.include_router(graphql_app,prefix="/graphql")


origins = [
    "http://localhost",
    "http://localhost:3000", 
    "*"
]

# Add CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

  
# if __name__ == '__main__':
#     uvicorn.run("main.app", host="localhost",port="8080", reload=True)
 
    



      
