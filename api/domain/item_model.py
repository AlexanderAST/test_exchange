from sqlalchemy import Column, Integer, String
from api.database import Base


class ItemModel(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)