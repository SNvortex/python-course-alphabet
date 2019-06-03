"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

import homework
import json
import pickle
import ruamel.yaml as yaml


# convert to json


def encode_cesar_to_json():
    json.dumps(homework.cesar_1)


def encode_garage_to_json():
    json.dumps(homework.garage_1)


def encode_car_to_json():
    json.dumps(homework.car_1)


# convert from json


def decode_cesar_from_json():
    cesar_1 = json.loads(homework.cesar_1)
    return cesar_1


def decode_garage_from_json():
    garage_1 = json.loads(homework.garage_1)
    return garage_1


def decode_car_from_json():
    car_1 = json.loads(homework.car_1)
    return car_1


# save to .json


def create_cesar_json():
    with open('cesar.json', 'w') as file:
        json.dump(homework.cesar_1, file)


def create_car_json():
    with open('car.json', 'w') as file:
        json.dump(homework.car_1, file)


def create_garage_json():
    with open('garage.json', 'w') as file:
        json.dump(homework.garage_1, file)


# load from .json

def load_cesar_json():
    with open('cesar.json', 'r') as file:
        cesar_from_json = json.load(file)
        return cesar_from_json


def load_car_json():
    with open('car.json', 'r') as file:
        car_from_json = json.load(file)
        return car_from_json


def load_garage_json():
    with open('garage.json', 'r') as file:
        garage_from_json = json.load(file)
        return garage_from_json


# convert to pickle


def encode_cesar_to_pickle():
    pickle.dumps(homework.cesar_1)


def encode_garage_to_pickle():
    pickle.dumps(homework.garage_1)


def encode_car_to_pickle():
    pickle.dumps(homework.car_1)


# convert from pickle


def decode_cesar_from_pickle():
    cesar_1 = pickle.loads(homework.cesar_1)
    return cesar_1


def decode_garage_from_pickle():
    garage_1 = pickle.loads(homework.garage_1)
    return garage_1


def decode_car_from_pickle():
    car_1 = pickle.loads(homework.car_1)
    return car_1


# save to .txt


def create_cesar_pickle():
    with open('cesar.txt', 'wb') as file:
        pickle.dump(homework.cesar_1, file)


def create_car_pickle():
    with open('car.txt', 'wb') as file:
        pickle.dump(homework.car_1, file)


def create_garage_pickle():
    with open('garage.txt', 'wb') as file:
        pickle.dump(homework.garage_1, file)


# load from .txt

def load_cesar_pickle():
    with open('cesar.txt', 'rb') as file:
        cesar_from_pickle = pickle.load(file)
        return cesar_from_pickle


def load_car_pickle():
    with open('car.txt', 'rb') as file:
        car_from_pickle = pickle.load(file)
        return car_from_pickle


def load_garage_pickle():
    with open('garage.txt', 'rb') as file:
        garage_from_pickle = pickle.load(file)
        return garage_from_pickle


# save to .yaml


def create_cesar_yaml():
    with open('cesar.yaml', 'w') as file:
        yaml.dump(homework.cesar_1, file)


def create_car_yaml():
    with open('car.yaml', 'w') as file:
        yaml.dump(homework.car_1, file)


def create_garage_yaml():
    with open('garage.yaml', 'w') as file:
        yaml.dump(homework.garage_1, file)


# load from .yaml

def load_cesar_yaml():
    with open('cesar.yaml', 'r') as file:
        cesar_from_yaml = yaml.load(file)
        return cesar_from_yaml


def load_car_yaml():
    with open('car.yaml', 'r') as file:
        car_from_yaml = yaml.load(file)
        return car_from_yaml


def load_garage_yaml():
    with open('garage.yaml', 'r') as file:
        garage_from_yaml = yaml.load(file)
        return garage_from_yaml


# convert to yaml


def encode_cesar_to_yaml():
    yaml.dump(homework.cesar_1)


def encode_garage_to_yaml():
    yaml.dump(homework.garage_1)


def encode_car_to_yaml():
    yaml.dump(homework.car_1)


# convert from yaml


def decode_cesar_from_yaml():
    cesar_1 = yaml.load(homework.cesar_1)
    return cesar_1


def decode_garage_from_yaml():
    garage_1 = yaml.load(homework.garage_1)
    return garage_1


def decode_car_from_yaml():
    car_1 = yaml.load(homework.car_1)
    return car_1
