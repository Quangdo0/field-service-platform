from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.site import Site

class SiteRepository():
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, site: Site)-> Site:
        self.db.add(Site)

        await self.db.flush()
        await self.db.refresh(site)

        return site

    async def get_by_id(self, site_id: int)-> Site | None:

        stmt = select(Site).where(
            Site.id == site_id
        )

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_customer_id(self, customer_id)-> list[Site]:
        stmt = select(Site).where(
            Site.customer_id == customer_id
        )

        result = await self.db.execute(stmt)

        return list(result.scalars().all())
