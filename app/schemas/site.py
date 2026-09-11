from datetime import datetime

from pydantic import BaseModel, ConfigDict

class SiteCreate(BaseModel):
    name : str
    address: str

class SiteResponse(BaseModel):
    id: int
    name: str
    customer_id: int
    address: str
    created_at: datetime
    updated_at: datetime

model_config = ConfigDict(
    from_attributes=True
)