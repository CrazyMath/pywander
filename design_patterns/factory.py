import abc


class Foo:
    pass


class Bar:
    pass


"""
Factory design pattern
"""


class Factory:
    def create(self, object_type):
        if object_type == 'foo':
            return Foo()
        if object_type == 'bar':
            return Bar()
        raise ValueError(f'Factory can\'t create object with type: "{object_type}"')


factory = Factory()
foo = factory.create('foo')
bar = factory.create('bar')
print(foo)
print(bar)

"""
Abstract Factory design pattern
"""


class AbstractFactory(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create(self):
        raise NotImplementedError


class FooFactory(AbstractFactory):
    def create(self):
        return Foo()


class BarFactory(AbstractFactory):
    def create(self):
        return Bar()


foo = FooFactory().create()
bar = BarFactory().create()
print(foo)
print(bar)
