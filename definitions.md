What is an SQLAlchemy model?

An SQLAlchemy model is simply a Python class that represents a database table.

For example:

Python --------- MySQL                              Employee class ─────────→ employees table

This is called ORM.
ORM = Object Relational Mapping.

>> FastAPI → SQLAlchemy → MySQL .

>>  models/__init__.py 
It can be empty.
It tells Python that models can be treated as a package.

>>>  What is the difference between SQLAlchemy model and Pydantic schema?


"The SQLAlchemy model represents the database table and is used for database operations. The Pydantic schema validates the request and response data coming through the API."

-------------------------------
Interview answer for this whole lesson

If an interviewer asks:

"How did you create the Employee table using SQLAlchemy?"

You can say:

"I created an Employee SQLAlchemy model that inherits from Base. I defined the columns using SQLAlchemy 2.x Mapped and mapped_column, including the primary key and constraints. I imported the model in main.py so SQLAlchemy registers it in Base.metadata. During FastAPI startup, I use the async engine and connection.run_sync(Base.metadata.create_all) to create the missing tables in MySQL. I then verified the employees table using MySQL Workbench."

That's a good fresher-level interview answer.

Your Lesson 3 checkpoint

You should now have:

✅ database.py
       ↓
Async SQLAlchemy engine

✅ models/employee.py
       ↓
Employee model

✅ main.py
       ↓
Imports Employee
       ↓
Base.metadata.create_all()

✅ MySQL
       ↓
employee_management_db
       ↓
employees table
---------------------------------
Employee Management API — Table Creation Interview Questions
1. Basic interview questions

Q1. How did you create a table in your project?

Answer (Interviewee):

"First, I created an Employee model using SQLAlchemy. I defined the required columns, such as employee ID, name, department, and salary. Then, I imported the model into main.py and used Base.metadata.create_all() during application startup to create the table in MySQL."

Q2. What is a SQLAlchemy model?

Answer (Interviewee):

"A SQLAlchemy model is a Python class that represents a database table. Each class attribute represents a column in that table. I used the Employee model to define the structure of my employees table."

Q3. What is Base in SQLAlchemy?

Answer (Interviewee):

"Base is the common base class for my SQLAlchemy models. When I create a model by inheriting from Base, SQLAlchemy can register its table information in the metadata."

Q4. What is __tablename__?

Answer (Interviewee):

"__tablename__ specifies the name of the database table. In my Employee model, I used __tablename__ = 'employees', so SQLAlchemy maps the model to the employees table."

Q5. What is Base.metadata.create_all()?

Answer (Interviewee):

"It checks the registered SQLAlchemy models and creates their database tables if they do not already exist. I used it to create the employees table automatically when my application starts."

2. Questions about your code

Q6. Why did you import the Employee model into main.py?

Answer (Interviewee):

"I imported the Employee model so that Python executes the model definition and registers its table with Base.metadata. This allows create_all() to discover and create the employees table."

Q7. Why did you use lifespan?

Answer (Interviewee):

"I used lifespan to manage application startup and shutdown operations. During startup, I check the MySQL connection and create missing tables. During shutdown, I dispose of the database engine."

Q8. Why did you use async with engine.begin()?

Answer (Interviewee):

"I used async with engine.begin() to obtain an asynchronous database connection with a transaction context. I used this connection to execute a test query and run the table creation operation."

Q9. Why did you use connection.run_sync()?

Answer (Interviewee):

"The SQLAlchemy metadata table creation operation is synchronous, but my application uses an asynchronous engine. So I used connection.run_sync() to run Base.metadata.create_all() through the asynchronous connection."

Q10. Why did you use text("SELECT 1")?

Answer (Interviewee):

"I used SELECT 1 to check whether the database connection is working. It is a simple query that does not insert, update, or delete any employee data."

3. Questions about columns and data types

Q11. What is a primary key?

Answer (Interviewee):

"A primary key uniquely identifies each row in a table. In my project, employee_id is the primary key, so each employee has a unique identifier."

Q12. Why did you use mapped_column()?

Answer (Interviewee):

"I used mapped_column() in SQLAlchemy 2.x to define the database columns, including their data types and constraints, such as primary keys, nullability, and uniqueness."

Q13. What is the purpose of nullable=False?

Answer (Interviewee):

"It means the column cannot contain a NULL value. For example, I set nullable=False for the employee name because the name is required."

Q14. Why do you specify a length for String, such as String(100)?

Answer (Interviewee):

"It defines the maximum length of the string column. For example, String(100) maps to a VARCHAR(100) column in MySQL. Specifying a length also avoids the MySQL error about VARCHAR requiring a length."

Q15. What is the difference between Mapped and mapped_column()?

Answer (Interviewee):

"Mapped provides the Python type annotation for an ORM attribute, while mapped_column() defines its database column configuration. I use them together in the SQLAlchemy 2.x style."

4. Database verification and troubleshooting

Q16. How did you verify that the table was created successfully?

Answer (Interviewee):

"I started my FastAPI application and checked the startup messages. Then, I opened MySQL Workbench and ran SHOW TABLES to verify that the employees table existed. I used DESCRIBE employees to inspect the columns."

Q17. What happens if the table already exists?

Answer (Interviewee):

"create_all() normally leaves an existing table unchanged. It creates missing tables, but it does not automatically update existing columns or apply schema changes."

Q18. Does creating a table automatically insert employee records?

Answer (Interviewee):

"No. Table creation only creates the database structure. I need to execute INSERT statements or use SQLAlchemy to add employee records separately."

Q19. What is the difference between a model and a schema?

Answer (Interviewee):

"A model defines the database table structure using SQLAlchemy. A schema defines and validates the data that the API accepts or returns using Pydantic."

Q20. What would you use if the database schema changes later?

Answer (Interviewee):

"For learning, create_all() is useful for creating missing tables. For managing changes to existing tables in a real project, I would use Alembic migrations so schema changes can be tracked and applied safely."
-------------------
Remember these three points:

Employee model: defines the table and its columns.

Base.metadata.create_all(): creates missing tables registered with SQLAlchemy.

lifespan: manages startup and shutdown operations.