from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DataBaseCrud.Models.models import Product, Image
import json


class DataBaseCrud:
    engine = None
    session = None

    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:p@ssw0rd@localhost:3306/merida-optics')
        self.session = Session(self.engine)

    def insert(self, pk: int, data: int):
        """
        :param pk:
        :param data:
        :return:
        """
        product = self.session.query(Product).get(pk)
        product.stock += data
        self.session.commit()
        return self.show_all()

    def get_all(self):
        """
        :return:
        """
        return self.show_all()

    def remove(self, pk: int, data: int):
        """
        :param pk:
        :param data:
        :return:
        """
        data = int(data)
        product = self.session.query(Product).get(pk)

        if product is None or product.stock < data:
            return False

        product.stock -= data
        self.session.commit()
        return self.show_all()

    def show(self, pk: int):
        """
        :return:
        """
        product = self.session.query(Product).get(pk)
        if product is None:
            return False
        images = self.session.query(Image).filter(Image.product_id == product.id)
        return self.format(product, images)

    def show_all(self):
        """
        :return:
        """
        # return self.session.query(Product).all()
        data = list()
        products = self.session.query(Product).all()
        images = self.session.query(Image).all()
        for product in products:
            img = []
            for i in images:
                if i.product_id == product.id:
                    img.append(i.url)
            data.append({"id": product.id, "cod": product.cod, "description": product.description, "brand": product.brand,
                        "type": product.type,"price": product.price, "stock": product.stock, "discount": product.discount,
                        "gender": product.gender, "subtype": product.subtype, "color": product.color, "images": img})
        return data

    def format(self, product: Product, image: Image):
        img = []
        for i in image:
            img.append(i.url)
        return {"id": product.id, "cod": product.cod, "description": product.description, "brand": product.brand,
                "type": product.type,"price": product.price, "stock": product.stock, "discount": product.discount,
                "gender": product.gender, "subtype": product.subtype, "color": product.color, "images": img}

    def add_products(self, product):
        product_add = Product(cod=product['cod'], description=product['description'], brand=product['brand'],
                              type=product['type'], price=product['price'], stock=product['stock'],
                              discount=product['discount'], gender=product['gender'], subtype=product['subtype'],
                              color=product['color'])
        self.session.add(product_add)
        self.session.commit()
        for image in product['images']:
            image_add = Image(url=image, product_id=product_add.id)
            self.session.add(image_add)
            self.session.commit()
        return True


