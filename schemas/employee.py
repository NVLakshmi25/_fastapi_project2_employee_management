from  pydantic import BaseModel, Field

# Schema for creating an employee
class EmployeeCreate(BaseModel):
    name: str=Field(min_length=2, max_length=100)
    department:str=Field(min_length=2, max_length=50)
    salary:float=Field(gt=0, le=10000000)
 
 # Schema for the employee API response
class EmployeeResponse(BaseModel):
    employee_id:int
    name:str
    department:str
    salary:float 
    
     
class EmployeeUpdate(BaseModel):
    name:str
    age:int
    department:str
    salary:float
    
