from fastapi import FastAPI
from pydantic import BaseModel
import math


app = FastAPI()
class SquareInput(BaseModel):
    side: float


@app.post("/area/square")
def calculate_square_area(data: SquareInput):

    area = data.side ** 2

    return {
        "side": data.side,
        "formula": "side²",
        "area": round(area, 2)
    }


class CircleInput(BaseModel):

    radius: float


@app.get("/")
def home():

    return {
        "message": "Welcome to my first FastAPI"
    }


@app.post("/area/circle")
def calculate_area(data: CircleInput):

    area = math.pi * (data.radius ** 2)

    return {
        "radius": data.radius,
        "formula": "π × r²",
        "area": round(area, 2)
    }
"""from crud import (
    save_calculation,
    get_all_calculations,
    get_calculation_by_id,
    update_calculation_by_id,
    delete_calculation_by_id
)


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class NumbersInput(BaseModel):
    a: float
    b: float


@app.get("/")
def home():
    return {
        "message": "Welcome to Calculator API"
    }


@app.post("/add")
def add_numbers(data: NumbersInput):
    result = data.a + data.b
    save_calculation (
       "addition",
       data.a,
       data.b,
       result
    ) 

    return {
        "operation": "addition",
        "a": data.a,
        "b": data.b,
        "result": result
    }


@app.post("/subtract")
def subtract_numbers(data: NumbersInput):
    result = data.a - data.b

    save_calculation(
        "subtraction",
        data.a,
        data.b,
        result
    )

    return {
        "operation": "subtraction",
        "a": data.a,
        "b": data.b,
        "result": result
    }

@app.post("/multiply")
def multiply_numbers(data: NumbersInput):
    result = data.a * data.b

    save_calculation(
        "multiplication",
        data.a,
        data.b,
        result
    )

    return {
        "operation": "multiplication",
        "a": data.a,
        "b": data.b,
        "result": result
    }


@app.post("/divide")
def divide_numbers(data: NumbersInput):
    if data.b == 0:
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed"
        )

    result = data.a / data.b

    save_calculation(
        "division",
        data.a,
        data.b,
        result
    )

    return {
        "operation": "division",
        "a": data.a,
        "b": data.b,
        "result": result
    }

@app.get("/calculations")
def read_calculations():

    return get_all_calculations()

@app.get("/calculations/{calculation_id}")
def read_calculation(calculation_id: int):

    calculation = get_calculation_by_id(calculation_id)

    if calculation is None:
        raise HTTPException(
            status_code=404,
            detail="Calculation not found"
        )

    return calculation

@app.put("/calculations/{calculation_id}")
def update_calculation(calculation_id: int, data: NumbersInput):
    result = data.a + data.b

    existing = get_calculation_by_id(calculation_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Calculation not found"
        )

    update_calculation_by_id(
        calculation_id,
        "addition",
        data.a,
        data.b,
        result
    )

    return {
        "message": "Calculation updated successfully",
        "id": calculation_id,
        "operation": "addition",
        "a": data.a,
        "b": data.b,
        "result": result
    }

@app.delete("/calculations/{calculation_id}")
def delete_calculation(calculation_id: int):

    existing = get_calculation_by_id(calculation_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Calculation not found"
        )

    delete_calculation_by_id(calculation_id)

    return {
        "message": "Calculation deleted successfully",
        "id": calculation_id
    }"""