class SingletonMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class PersonalizableSingleton(metaclass=SingletonMetaClass):

    def __init__(self, attribute):
        self.attribute = attribute


if __name__ == "__main__":

    first_singleton = PersonalizableSingleton("ATRIBUTO 1")
    second_singleton = PersonalizableSingleton("ATRIBUTO 2")

    print(first_singleton is second_singleton)
