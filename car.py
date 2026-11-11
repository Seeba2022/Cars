
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Car data model
class Car(BaseModel):
    id: int
    brand: str
    name: str
    model: int
    price: float
    onroad_price: float
    colours: list[str]


# Sample car database
cars = [
    {
        "id": 1,
        "brand": "Hyundai",
        "name": "Creta",
        "model": 2025,
        "price": 1200000,
        "onroad_price": 1400000,
        "colours": ["White", "Black", "Red", "Silver"]
    },
    {
        "id": 2,
        "brand": "Tata",
        "name": "Nexon",
        "model": 2025,
        "price": 900000,
        "onroad_price": 1050000,
        "colours": ["Blue", "White", "Red", "Grey"]
    },
    {
        "id": 3,
        "brand": "Maruti Suzuki",
        "name": "Swift",
        "model": 2025,
        "price": 650000,
        "onroad_price": 750000,
        "colours": ["Red", "White", "Blue", "Silver"]
    }
]


# Home API
@app.get("/")
def home():
    return {"message": "Welcome to Car Management API"}


# Get all cars
@app.get("/cars")
def get_cars():
    return cars


# Get car by ID
@app.get("/cars/{car_id}")
def get_car(car_id: int):
    for car in cars:
        if car["id"] == car_id:
            return car

    raise HTTPException(status_code=404, detail="Car not found")


# Add a new car
@app.post("/cars")
def add_car(car: Car):
    for existing_car in cars:
        if existing_car["id"] == car.id:
            raise HTTPException(status_code=400, detail="Car ID already exists")

    cars.append(car.model_dump())
    return {"message": "Car added successfully", "car": car}


# Delete a car
@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    for car in cars:
        if car["id"] == car_id:
            cars.remove(car)
            return {"message": "Car deleted successfully"}

    raise HTTPException(status_code=404, detail="Car not found")
