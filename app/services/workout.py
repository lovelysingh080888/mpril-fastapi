
from fastapi import HTTPException
from odmantic import ObjectId
from app.graphql.schemas.schema import  WorkoutInput, UpWorkoutInput, WorkoutType
from common.response.workout_response import CustomResponse, Success, Error
from app.models.workout_model import Workout
from common.config.database import configure_database
from datetime import datetime


class WorkoutService:
    
    # Create new Workout
    @staticmethod
    async def create_workout(data: WorkoutInput):
            try:
                configure = configure_database()
                engine = await configure()
                new_workout = Workout(date=data.date, title=data.title, details=data.details)
                d = await engine.save(new_workout)
                return WorkoutType(id=d.id, title=d.title, date=d.date, details=d.details)
            except Exception as e:
                print(e)
                raise HTTPException(status_code=500, detail=Error.INTERNAL_SERVER_ERROR.value)
 
 
    # Update Workout    
    @staticmethod
    async def update_workout(data: UpWorkoutInput) -> WorkoutType:
        try:
            configure = configure_database()
            engine = await configure()
            
            # Find the workout based on the provided ID
            workout = await engine.find_one(Workout, Workout.id==ObjectId(data.id))
            print(workout)
            # if workout is None:
            #     raise HTTPException(status_code=404, detail="Workout not found")

            # Update the fields of the workout document with the new data
            workout.title = data.title
            workout.date = data.date
            workout.details = data.details

            # Save the updated document
            updated_workout = await engine.save(workout)

            # Return the updated workout as a WorkoutType object
            return WorkoutType(
                id=updated_workout.id,
                title=updated_workout.title,
                date=updated_workout.date,
                details=updated_workout.details
            )

        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=Error.INTERNAL_SERVER_ERROR.value)
   
 
    # Find Workouts between date
    @staticmethod
    async def find_workouts_between_dates(start_date: str, end_date: str):
        try:
            configure = configure_database()
            engine = await configure()

            # Convert the string dates to datetime objects
            start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
            end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

            # Find all workout documents with dates between the given dates
            workouts = await engine.find(Workout, Workout.date >= start_datetime, Workout.date <= end_datetime)
            return [WorkoutType(id=workout.id,title=workout.title,details=workout.details,date=workout.date) for workout in workouts]
            
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=Error.INTERNAL_SERVER_ERROR.value)
       
    
    
    # Fetch all workouts 
    @staticmethod
    async def list_workouts_with_limit_offset(limit: int, offset: int):
        try:
            configure = configure_database()
            engine = await configure()

            # Find workout documents with pagination applied
            workouts = await engine.find(Workout, limit=limit, skip=offset)
            return [WorkoutType(id=workout.id,title=workout.title,details=workout.details,date=workout.date) for workout in workouts]

            
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=Error.INTERNAL_SERVER_ERROR.value)