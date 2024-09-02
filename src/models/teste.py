from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
class Base(DeclarativeBase):
    pass 
class Teste(Base):
    __tablename__ = "tabelinha"
    Id: Mapped[int] = mapped_column(primary_key=True)
    vartext: Mapped[str] = mapped_column(String(60))

    def __repr__(self) -> str:
        return f"Teste:{self.vartext}"