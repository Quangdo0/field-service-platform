from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.repositories.customer_repository import CustomerRepository
from app.services.customer_service import CustomerService, CustomerNotFoundError
from app.core.database import get_db
router = APIRouter(
    prefix = "/customers",
    tags = ["Customers"],
)

@router.post("", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED,)
async def create_customer(data: CustomerCreate, db: AsyncSession = Depends(get_db)):
    repository = CustomerRepository(db)
    service = CustomerService(repository)

    customer = await service.create_customer(data)

    await db.commit()
    await db.refresh(customer)

    return customer

@router.get("", response_model = list[CustomerResponse],)
async def list_customers(db: AsyncSession = Depends(get_db)):
    repository = CustomerRepository(db)
    service = CustomerService(repository)

    return await service.list_customer()

@router.get("/{customer_id}", response_model = CustomerResponse,)
async def get_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    repository = CustomerRepository(db)
    service = CustomerService(repository)

    try:
        return await service.get_customer(customer_id)

    except CustomerNotFoundError:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Customers not found",
        )

    

    






