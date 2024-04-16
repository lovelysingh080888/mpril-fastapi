import strawberry
from datetime import datetime 
# Created schema for workout output 
@strawberry.type    
class WorkoutType:
    id:str
    title:str
    details:str  
    date:str  
    
@strawberry.input    
class WorkoutInput:
    title:str
    details:str  
    date:str  
    
@strawberry.input    
class UpWorkoutInput:
    id:str
    title:str
    details:str  
    date:str      