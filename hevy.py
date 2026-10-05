import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HEVY_API_KEY")

def getAllWorkouts():
    page = 1
    totalPages = 1
    headers = {"api-key": api_key}
    workouts = []

    while page <= totalPages:
        query = {"page":page, "pageSize":10}
        r = requests.get("https://api.hevyapp.com/v1/workouts", params = query, headers=headers, timeout=10 )
        r.raise_for_status()
        rJSON = r.json()

        totalPages = rJSON['page_count']
        page+= 1
        workouts.extend(rJSON["workouts"])

    return workouts
