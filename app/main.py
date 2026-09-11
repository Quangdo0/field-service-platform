from fastapi import FastAPI
from app.api.routes.customers import router as customers_router
app = FastAPI(
    title = "Field Service Platform",
    version = "0.1.0",
)

app.include_router(
    customers_router,
    prefix = "/api/v1",
)



@app.get("/")
async def root():
    return {
        "message": "Field Service Platform API"
    }


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }