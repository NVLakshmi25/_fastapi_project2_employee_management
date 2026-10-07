from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Application startup
    async with engine.connect() as connection:
        await connection.execute(text("SELECT 1"))
        print("MySQL database connection successful!")

    yield

    # Application shutdown
    await engine.dispose()
    print("Database engine disposed.")
    --------------------------------------
    app = FastAPI(
    title="Employee Management API",
    description="Learn FastAPI by building an Employee Management System",
    version="1.0.0",
    lifespan=lifespan
)
-------------------------------