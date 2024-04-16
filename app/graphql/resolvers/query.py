import strawberry
from typing import List
from app.graphql.schemas.schema import WorkoutType
from app.services.workout import WorkoutService

@strawberry.type
class Query:
    
    @strawberry.field    
    async def get_workouts(self, limit:int, offset:int) -> List[WorkoutType]:
        return await WorkoutService.list_workouts_with_limit_offset(limit=limit, offset=offset)
    
    
    @strawberry.field    
    async def get_workouts_date_between(self, start_date:str, end_date:str) -> List[WorkoutType]:
        return await WorkoutService.find_workouts_between_dates(start_date=start_date, end_date=end_date)
    

        