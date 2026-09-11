from app.models.customer import Customer
from app.schemas.customer import CustomerCreate
from app.repositories.customer_repository import CustomerRepository

class CustomerNotFoundError(Exception):
    pass

class CustomerService():
    def __init__(self, repository :CustomerRepository):
        self.repository = repository

    async def create_customer(self, data: CustomerCreate)-> Customer:
        customer = Customer(
            code = "Temp",
            name  = data.name,
            phone = data.phone,
            email = data.email,
        )

        customer = await self.repository.create(customer)

        customer.code = f"CUS-{customer.id:06d}"

        return customer

    async def get_customer(self, customer_id: int)-> Customer:
        customer = await self.repository.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundError

        return customer

    async def list_customer(self)-> list[Customer]:
        return await self.repository.get_all()

    