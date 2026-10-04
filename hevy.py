import requests

def getAllWorkouts():
    page = 1
    totalPages = 1

    while page <= totalPages:
        query = {"page":page}
        r = requests.get("https://api.hevyapp.com/v1/workouts?", params = query)
        print(r.json())

getAllWorkouts()