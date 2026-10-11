
from contextlib import asynccontextmanager
from fastapi import FastAPI ,HTTPException , status , Depends
from schemas.employee import EmployeeCreate, EmployeeResponse,EmployeeUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from database import get_db , Base, engine
from models.empTable import Employee

# Application startup and shutdown
@asynccontextmanager
async def lifespan(app:FastAPI):
    # application Startup
    async with engine.begin() as connection:
        await connection.execute(text("SELECT 1"))
         # Create database tables if they do not exist
        await connection.run_sync(
            Base.metadata.create_all
        )
    print("MySQL connection successful")
    print("Database tables checked/created!")
        # FastAPI starts serving requests after this point
    yield
    
    #shutdown
    await engine.dispose()
    print("Database engine disposed.")

# Create FastAPI application
app = FastAPI(
    title="Employee Management API",
    description="A beginner-friendly Employee Management System",
    version="1.0.0",
    lifespan=lifespan
)
# Temporary employee data
# Here, employees is a Python list containing dictionaries. Each dictionary represents one employee.
employees = [
    {
        "employee_id": 1,
        "name": "Lakshmi",
        "department": "IT",
        "salary": 45000
    },
    {
        "employee_id": 2,
        "name": "Ravi",
        "department": "HR",
        "salary": 35000
    },
    {
        "employee_id": 3,
        "name": "Priya",
        "department": "Finance",
        "salary": 50000
    }
]


@app.get("/")
async def home():
    return {
        "message": "Welcome to Employee Management API",
        "status": "Application is running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }
    
@app.get("/test-db")
async def test_database(
    db:AsyncSession=Depends(get_db)
):
    result =await db.execute(
        text("SELECT 1")
    )
    return{
        "message":"Database conneted  successfully",
        "result":result.scalar()
    }




@app.get("/employeedata/")
async def get_employees():
    return{
        "message":"retrive employees successfully",
        "total_employees":len(employees),
        "data":employees
    }
    
#filter the employees ---by departemnt 
@app.get("/employees/filter")
async def filter_employees(department:str):
    filtered_employees = [
        employee
        for employee in employees
            if employee["department"].lower()==department.strip().lower()
    ]
    return{
        "message":"Employye filtered successfully",
        "departement":department,
        "total_employees":len(filtered_employees),
        "data":filtered_employees
    }


#post api -- create  a new employee
@app.post("/employees/" ,response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
async def create_employee(employee:EmployeeCreate):
 #generate   the    next emp  ID
    new_id=max((item["employee_id"] for item in employees),
            default=0
            ) +1
 #create  the employee dictionary
    new_employee={
     "employee_id":new_id,
     "name":employee.name,
     "department":employee.department,
     "salary":employee.salary
 }
   # Add the employee to the temporary list
    employees.append(new_employee)

    # Return the newly created employee
    return  new_employee 


# Update an employee in the temporary list
@app.put("/employees/{employee_id}")
async def update_employee(
    employee_id:int,
    employee_data:EmployeeUpdate):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            employee["name"] =employee_data.name
            employee["age"]=employee_data.age
            employee["department"]=employee_data.department
            employee["salary"]=employee_data.salary
            # employee.update(employee_data.model_dump())
            return{
                "message":"Employee updated successfully",
                "data":employee
            }
    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )
    
# Delete an employee from the temporary list
@app.delete("/employees/{employee_id}")
async def delete_emp(employee_id:int):
    for index, employee in enumerate(employees):
       if employee["employee_id"]==employee_id:
           deleted_employee=employees.pop(index)
           return{
               "message":"employee deleted successfully",
               "data":deleted_employee
        
              }
    raise HTTPException(
        status_code=404,
        detail="employe not exist"
    )


# retrive one employee  based on ID :
@app.get("/employeedata/{employee_id}")
async def get_employee(employee_id:int):
    for employee in employees:
        if employee["employee_id"]==employee_id:
          return{
        "message":"retrive employeee data successfully",
        "data":employee
        
    }
    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )
