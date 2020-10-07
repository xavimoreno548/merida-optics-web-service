from sqlalchemy import create_engine
from base import Base
from models import Product, Image

engine = create_engine('mysql+mysqlconnector://root:p@ssw0rd@localhost:3306/merida-optics')
Base.metadata.create_all(engine)

