
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import String, Text, Integer, DateTime
# from datetime import datetime
# from .database import Base

# class Draft(Base):
#     __tablename__ = 'drafts'
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     topic: Mapped[str | None] = mapped_column(String(255), nullable=True)
#     keywords: Mapped[str | None] = mapped_column(String(255), nullable=True)
#     tone: Mapped[str | None] = mapped_column(String(50), nullable=True)
#     audience: Mapped[str | None] = mapped_column(String(255), nullable=True)
#     word_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
#     content: Mapped[str] = mapped_column(Text, nullable=False)
#     status: Mapped[str] = mapped_column(String(50), default='draft')
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# app/models.py
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import String, Text, Integer, DateTime, func
# from datetime import datetime
# from .database import Base  # or from .db import Base, if you renamed it

# class Draft(Base):
#     __tablename__ = 'drafts'

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     topic: Mapped[str | None] = mapped_column(String(255), nullable=True)
#     keywords: Mapped[str | None] = mapped_column(String(255), nullable=True)
#     tone: Mapped[str | None] = mapped_column(String(50), nullable=True)
#     audience: Mapped[str | None] = mapped_column(String(255), nullable=True)
#     word_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
#     content: Mapped[str] = mapped_column(Text, nullable=False)
#     status: Mapped[str] = mapped_column(String(50), default='draft', nullable=False)

#     # Prefer DB-side defaults; MySQL returns naive datetime but consistent
#     created_at: Mapped[datetime] = mapped_column(
#         DateTime,
#         nullable=False,
#         server_default=func.now()
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime,
#         nullable=False,
#         server_default=func.now(),
#         server_onupdate=func.now()
#     )

# app/models.py
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Integer, DateTime, func
from datetime import datetime
from .database import Base

class Draft(Base):
    __tablename__ = 'drafts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    topic: Mapped[str | None] = mapped_column(String(255), nullable=True)
    keywords: Mapped[str | None] = mapped_column(String(255), nullable=True)
    tone: Mapped[str | None] = mapped_column(String(50), nullable=True)
    audience: Mapped[str | None] = mapped_column(String(255), nullable=True)
    word_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default='draft', nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), server_onupdate=func.now()
    )
