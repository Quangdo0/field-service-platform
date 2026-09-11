from app.models.site import Site
from app.repositories.site_repository import SiteRepository
from app.schemas.site import SiteCreate

class SiteNotFoundError(Exception):
    pass

class SiteService():
    def __init__(self, repository: SiteRepository):
        self.repository = repository

    async def create_site(self, data: SiteCreate) -> Site:
        


