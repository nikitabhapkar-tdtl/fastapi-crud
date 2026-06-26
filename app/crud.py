from sqlalchemy.orm import Session

from app.models import Employee
from app.schemas import EmployeeCreate


# Create Employee
def create_employee(db: Session, employee: EmployeeCreate):

    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


# Get All Employees
def get_all(db: Session):

    return db.query(Employee).all()


# Get Employee By ID
def get_by_id(db: Session, emp_id: int):

    return db.query(Employee).filter(Employee.id == emp_id).first()


# Update Employee
def update_employee(db: Session, emp_id: int, data: EmployeeCreate):

    employee = get_by_id(db, emp_id)

    if employee is None:
        return None

    employee.name = data.name
    employee.email = data.email
    employee.department = data.department

    db.commit()
    db.refresh(employee)

    return employee


# Delete Employee
def delete_employee(db: Session, emp_id: int):

    employee = get_by_id(db, emp_id)

    if employee is None:
        return None

    db.delete(employee)
    db.commit()

    return employee