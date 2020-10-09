
class Car:
    def model(self, models):
        if models < 2000:
            self.model = 2000
        elif models > 2018:
            self.model = 2018
        else:
            self.model = models


car_a = Car()
car_a.model(20)
print(car_a.model)


# -------------------------------------------------------
# создаем класс Car
class Car:

    # создаем конструктор класса Car
    def __init__(self, model):
        # Инициализация свойств.
        self.model = model

    # создаем свойство модели.
    @property
    def model(self):
        return self.__model

    # Сеттер для создания свойств.
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)

car_a = Car(2088)
print(car_a.getCarModel())
