import strawberry
from common.response.workout_response import CustomResponse, Success, Error
from app.services.workout import WorkoutService
from app.graphql.schemas.schema import WorkoutType, WorkoutInput, UpWorkoutInput

@strawberry.type
class Mutation:
    
    @strawberry.mutation 
    async def create_workout(self, data:WorkoutInput) ->WorkoutType :
          return await WorkoutService.create_workout(data=data)
  
    @strawberry.mutation   
    async def update_workout(self, data:UpWorkoutInput) -> WorkoutType:
        return await WorkoutService.update_workout(data=data)