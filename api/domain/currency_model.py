from sqlalchemy import Column, Integer, String
from api.database import Base


class CurrencyModel(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, index=True)
    last_update = Column(String)
    base = Column(String, nullable=False)
    rub = Column(String, nullable=False)
    eur = Column(String, nullable=False)
    usd = Column(String, nullable=False)
    jpy = Column(String, nullable=False)