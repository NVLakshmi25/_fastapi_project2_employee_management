from datetime import date

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Employee(Base):
    __tablename__ ="employees"
    employee_id:Mapped[int]=mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    name:Mapped[str]=mapped_column(
        String(255),
       
    )
    email:Mapped[str | None]=mapped_column(
        String(255),
        unique=True,
        nullable=True
    )
    phone:Mapped[int |None]=mapped_column(
        String(20),
        nullable=True
        
    )
    age:Mapped[int | None] =mapped_column(
        Integer,
        nullable=True
        
    )
    city:Mapped[str |None]=mapped_column(
        String(100),
        nullable=True    
    )
    job_title:Mapped[str]=mapped_column(
        String(100),
        nullable=True
    )
    department:Mapped[str]=mapped_column(
        String(50),
        nullable=False
        
    )
    salary:Mapped[float]=mapped_column(
        Float,
        nullable=False
    )
    joining_date:Mapped[date| None] =mapped_column(
        Date,
        nullable=True
    )





