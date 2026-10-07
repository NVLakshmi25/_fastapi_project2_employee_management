Chapter 3: Connect FastAPI to MySQL Workbench using SQLAlchemy :::
python -m pip install sqlalchemy asyncmy
python -m pip show sqlalchemy
python -m pip show asyncmy.

>>> Create database.py and connect FastAPI to MySQL.
>>>  Now we'll create database.py, which manages the connection between FastAPI and MySQL.

Concept ----  Purpose
SQLAlchemy Engine ----- Manages connections to the database
Database URL----- Specifies the database server, username, password, and database name 
 Async driver (asyncmy) ---- Allows asynchronous communication with MySQL
AsyncSession---  Provides a session for performing database operations
Base---- Provides the foundation for defining SQLAlchemy models
lifespan ---  Manages application startup and shutdown tasks

-----------------------
Although your code works with the values directly in Python, I don't recommend keeping the password inside the Python file.

python -m pip install python-dotenv

python -m pip install greenlet.

>>> But SQLAlchemy's async functionality also needs greenlet for some of its internal async/sync bridging.
Your code contains:

from sqlalchemy.ext.asyncio import AsyncSession

So SQLAlchemy loads its asyncio module and checks for greenlet.

>>>>  python -m pip install fastapi uvicorn[standard] sqlalchemy[asyncio] asyncmy python-dotenv .

-------------------------
mysql — database type

asyncmy — asynchronous MySQL driver

username and password — MySQL credentials

localhost — database server on your computer

3306 — common MySQL port

employee_management_db — database name.

If your password contains special characters such as @, /, or :, it must be URL-encoded. We'll handle that safely when we introduce a proper settings configuration.
------------------------
os.getenv() reads a setting from the environment. The second argument is the fallback value if that setting hasn't been provided.

For example, if your MySQL username is root, the code uses root unless DB_USER is set differently.
----------------------
The engine is SQLAlchemy's database connection manager.

echo=True logs generated SQL statements in the terminal, which is useful while learning. Turn it off in production to avoid logging sensitive query information.

pool_pre_ping=True checks pooled connections before using them, helping detect stale connections.

Creating the engine configures the connection manager; it doesn't necessarily establish a live connection immediately.
-------------------------
A session is used to perform database work, such as adding, retrieving, updating, and deleting employee records.

expire_on_commit=False lets us continue accessing loaded object attributes after committing a transaction, without automatically expiring them.
---------------------
Later, our SQLAlchemy models—such as Employee and Department—will inherit from Base.

This gives SQLAlchemy a shared registry of models and their table definitions.
---------------

When FastAPI starts → check whether MySQL is reachable.
When FastAPI stops → clean up the database engine.

What is contextlib?

contextlib is a Python module that provides tools for working with resources.

For example:

database connections
files
network connections
locks

Here we use:

asynccontextmanager

because our application uses async/await.
It allows us to create a function with two sections:

STARTUP
   ↓
yield
   ↓
SHUTDOWN

For FastAPI, this is useful for application startup and shutdown.
-----------------------
SQLAlchemy's text() allows us to provide raw SQL text to SQLAlchemy.

means:

"SQLAlchemy, treat SELECT 1 as an SQL statement."
text("SELECT 1")

Why SELECT 1?

Because we don't want to modify the database.

We simply want to ask MySQL:

"Can you execute a basic SQL query?"

If MySQL responds successfully, our connection is working.
The engine is responsible for communicating with MySQL.
we are bringing that database engine into main.py.
from database import engine   -----   main.py
---------------------
FastAPI
   ↓
SQLAlchemy
   ↓
asyncmy
   ↓
MySQL
-----------------
lifespan=lifespan ::
It tells FastAPI:

"Use my lifespan() function when starting and shutting down the application."
--------------------
"I use .env for database configuration. I load those values using load_dotenv() and os.getenv(). I build a mysql+asyncmy connection URL and create an async SQLAlchemy engine. Then I create an AsyncSession factory. Through get_db() and FastAPI's Depends(), each API endpoint gets a database session. I use await for database operations because the project uses asynchronous SQLAlchemy. I currently use SELECT 1 to verify that FastAPI can successfully connect to MySQL."
----------------


