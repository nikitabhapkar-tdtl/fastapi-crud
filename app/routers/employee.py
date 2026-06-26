from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.dependencies import get_db
from app.schemas import EmployeeCreate, Employee
from app import crud

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


# Create Employee
@router.post("/", response_model=Employee)
def create(employee: EmployeeCreate, db: Session = Depends(get_db)):

    return crud.create_employee(db, employee)


# Get All Employees
@router.get("/", response_model=list[Employee])
def get_all(db: Session = Depends(get_db)):

    return crud.get_all(db)


# Get Employee By ID
@router.get("/{id}", response_model=Employee)
def get_one(id: int, db: Session = Depends(get_db)):

    employee = crud.get_by_id(db, id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")

    return employee


# Update Employee
@router.put("/{id}", response_model=Employee)
def update(id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):

    updated_employee = crud.update_employee(db, id, employee)

    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")

    return updated_employee


# Delete Employee
@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):

    deleted_employee = crud.delete_employee(db, id)

    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")

    return {"message": "Employee Deleted Successfully"}