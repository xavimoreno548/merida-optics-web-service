from sqlalchemy import String, DateTime, Column, Integer, Float, ForeignKey
from DataBaseCrud.Models.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    cod = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    brand = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    discount = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    subtype = Column(String(30), nullable=False)
    color = Column(String(30), nullable=False)
    image = relationship('Image', backref='products')
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())