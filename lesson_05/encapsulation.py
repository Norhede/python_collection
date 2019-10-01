class Car:
    def __init__(self, make, model, bhp, mph):
        self.__make = make
        self.__model = model
        self.__bhp = bhp
        self.__mph = mph

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, make):
        self.__make = make

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def bhp(self):
        return self.__bhp

    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp

    @property
    def mph(self):
        return self.__mph

    @mph.setter
    def mph(self, mph):
        self.__mph = mph


car1 = Car("Hello", "World!", 42, True)
print(car1.make)
print(car1.model)
print(car1.bhp)
print(car1.mph)

