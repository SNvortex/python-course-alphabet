"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


from constants import *
import uuid
import random


class Cesar:
    register_id = None

    def __init__(self, name):
        self.name = str(name)
        self.garages = []
        self.register_id = str(uuid.uuid4())

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        cars_count = 0
        for garage in self.garages:
            cars_count += len(garage.cars)
        return cars_count

    def hit_hat(self):
        return sum([garage.hit_hat() for garage in self.garages])

    def add_car(self, car, garage = None):
        if garage in self.garages:
            garage.add_car(car)
        elif not garage in self.garages:
            for other_garage in self.garages:
                if max(other_garage.free_places()):
                    other_garage.add_car(car)
        else:
            return "There's no free places for a new car"

    def __eq__(self, other):
        return self.hit_hat == other.hit_hat

    def __lt__(self, other):
        return self.hit_hat < other.hit_hat

    def __gt__(self, other):
        return self.hit_hat > other.hit_hat


class Car:

    def __init__(self, price, mileage):
        self.price = float(price)
        self.type = random.choice(CARS_TYPES)
        self.producer = random.choice(CARS_PRODUCER)
        self.number = str(uuid.uuid4())
        self.mileage = float(mileage)

    def __str__(self):
        return f"""price: {self.price}
        type: {self.type}
        producer: {self.producer}
        number: {self.number}
        mileage: {self.mileage}"""

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def number_change(self):
        self.number = str(uuid.uuid4())
        return self.number


class Garage:
    def __init__(self):
        self.town = random.choice(TOWNS)
        self.cars = []
        self.places = int()
        self.owner = Cesar.register_id
        self.car = Car
        self.free_places = self.places - len(self.cars)

    def add_car(self):
        if self.free_places > 0:
            self.cars.append(self.car)

    def remove_car(self):
        self.cars.remove(self.car)

    def hit_hat(self):
        all_cars_price = 0
        for self.price in self.cars:
            all_cars_price += self.price
        return all_cars_price

