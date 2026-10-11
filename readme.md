So SQLAlchemy acts as the bridge between:

Python
   ↕
Database

>>>  We need this because an employee has a joining date.

>>  Python attribute name is a string and SQLAlchemy should create a database column for it.

>>> Base is the parent class for our SQLAlchemy models.

>>> Think:

engine.connect()
    ↓
Get a connection

engine.begin()
    ↓
Get a connection + transaction context.

>>  Base.metadata

Contains your registered model information:

------------
Think:

Client
  ↓
Pydantic Schema
  ↓
FastAPI
  ↓
SQLAlchemy Model
  ↓
MySQL

We'll connect these in the CRUD lesson.
-------------------
What you should understand before moving on

Make sure these 8 points are clear:

1. Model
class Employee(Base):

Python class representing a database table.

2. Table name
__tablename__ = "employees"

Tells SQLAlchemy the MySQL table name.

3. Column
name: Mapped[str] = mapped_column(String(100))

Python attribute → database column.

4. Primary key
primary_key=True

Uniquely identifies each row.

5. Base.metadata

Contains information about the tables registered with SQLAlchemy.

6. create_all()

Creates missing tables.

7. run_sync()

Allows synchronous create_all() to run through the async SQLAlchemy connection.

8. get_db()

Will later provide an AsyncSession to your CRUD endpoints.
--------------------
How does yield work here?

AsyncSessionLocal() creates a database session.

yield session provides that session to the API endpoint.

After the endpoint finishes, FastAPI cleans up the dependency, and the async with block closes the session.
--------------------------
If an interviewer asks, “Which is better in FastAPI: lifespan or @app.on_event?”

You can answer:

"Lifespan is the recommended approach in modern FastAPI. It allows me to manage startup and shutdown operations in one function. In my Employee Management API, I use lifespan to check the MySQL connection and create missing tables during startup, and dispose of the database engine during shutdown. I use yield in my database dependency separately to provide and clean up database sessions for API requests."
----------------------------------
Important: These are two different uses of yield.

yield in lifespan separates startup work from shutdown work.

yield session in get_db() provides a database session to an API endpoint and allows the session to be cleaned up afterward.

You can use both in the same application.
-------------------