from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.customer import Customer

class CustomerRepository():
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, customer: Customer)-> Customer:
        self.db.add(customer)

        await self.db.flush()
        await self.db.refresh(customer)

        return customer

    async def get_by_id(self, customer_id: int)-> Customer:
        stmt = select(Customer).where(
            Customer.id == customer_id
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all(self) -> list[Customer]:
        stmt = select(Customer).order_by(
            Customer.created_at.desc()
        )

        result = await self.db.execute(stmt)

        return list(result.scalars().all())
    


