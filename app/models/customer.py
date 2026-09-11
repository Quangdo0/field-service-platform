from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(
        primary_key = True
    )

    code: Mapped[str] = mapped_column(
        String(50),
        unique = True,
        index = True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        index=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        server_default= func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone= True),
        server_default= func.now(),
        onupdate=func.now(),
    )