from datetime import datetime
from fastapi import HTTPException

def parse_dates(start_date: str, end_date: str):
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        return start_date, end_date
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Please provide dates in YYYY-MM-DD format.")
