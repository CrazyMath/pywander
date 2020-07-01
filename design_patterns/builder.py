from abc import ABCMeta, abstractmethod

"""
Builder design pattern
"""
class Director(metaclass=ABCMeta):

    def __init__(self):
        self._builder = None

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_object(self):
        return self._builder.get_constructed_object()


class Builder:

    def __init__(self):
        self.constructed_object = None

    def get_constructed_object(self):
        return self.constructed_object


class Product:

    def __init__(self):
        pass


class ConcreteBuilder(Builder):
    pass


class ConcreteDirector(Director):
    pass


"""
Example of usage builder pattern
"""
class Site:
    def __init__(self):
        self.parts = []

    def __repr__(self):
        return f'Site consists from next parts: "{self.parts}"'


class Designer(Builder):
    def __init__(self):
        self.constructed_object = Site()

    def add_login_page(self):
        self.constructed_object.parts.append('Login page')

    def add_product_page(self):
        self.constructed_object.parts.append('Product page')

    def add_cart_page(self):
        self.constructed_object.parts.append('Cart page')


class ProjectManager(Director):

    def set_builder(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.add_login_page()
        self._builder.add_product_page()
        self._builder.add_cart_page()


project_manager = ProjectManager()
designer = Designer()

project_manager.set_builder(designer)
project_manager.construct()

final_product = project_manager.get_constructed_object()

print(final_product)
