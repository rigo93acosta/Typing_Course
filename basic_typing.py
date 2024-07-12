# Types of typing in Python
text: str = 'rigo'
print(text)

number: int = 10
percent: float = 0.50
connected: bool = False

def format_input(user_input: str):
    print(user_input.title())
          
format_input(text)
# format_input(number) # Error

## Union types -> No tiene limites de la
## cantidad de tipos que se pueden unir
var: str | int = 10

from typing import Union
var_1: Union[str, int] = 10

def func(user_input: str | int):
    print(user_input)

## List
elements: list[int] = [1, 2, 3, 4, 5]

names: list[str] = ['rigo', 'jose', 'luis']

mixed: list[int | str] = ['a', 1]

# Evitar el uso del typing en listas muy complejas como array
# dificulta la lectura del código

## Tuplas
coordinates: tuple[int, int] = (10, 20)
## Ellipsis
coordinates: tuple[int, ...] = (10, 20)

## Sets
my_set: set = {1, 2, 3}

letters: set[str] = {'a', 'b', 'c'}

mixed_set: set[str | int] = {'a', 1, 'b', 2}

## Dictionaries
## Typing dict[key, value]
my_dict: dict[str, int|str] = {'name': 'rigo', 'age': 20}

def print_dict(some_dict: dict[int, str]):
    for value in some_dict.values():
        print(value.title())

example: dict[int, str] = {1: 'rigo', 2: 'mary'}
print_dict(example)
# print_dict(my_dict) # Error no es un dict correcto para la funcion

## Optionals
person: str | None = None

from typing import Optional
# person_: Optional[str] = 'rigo'
person_: Optional[str] = None

def greet(name: str | None = None):
    if name is None:
        print('No one is here ...')
    else:
        print(f'Hello {name}')

greet(person_)

## Clases

class Fruit:
    def __init__(self, name: str, grams: float):
        self.name = name
        self.grams = grams

orange: Fruit = Fruit('Orange', 100.0)

def describe(fruit: Fruit):
    print(f'This is a {fruit.name}, weighs {fruit.grams} grams')

describe(orange)

# banana = 'Banana'
# describe(banana) # Error

## Clase hija de Fruit
class Apple(Fruit):
    ...

apple: Apple = Apple('Fuji Apple', 200.0)
describe(apple)


## Return types
def add_numbers(a: int, b: int) -> int:
    return a + b
    # return float(a + b) # Error concept typing

result = add_numbers(10, 20)
print(result)

def hack_nasa() -> None:
    print('Hacking NASA ...')

hack_nasa()

## Excelente idea por si algo no existe
def fetch_user(user_id: int) -> str | None:
    users: dict = {0: 'rigo', 1: 'mary'}
    return users.get(user_id)

print(fetch_user(5))

## External types
import requests
from requests import Response

def get_status(url: str) -> int:
    response: Response = requests.get(url) ## Hay que leer la documentacion
    stutus_code: int = response.status_code
    
    return response.status_code

def analyse_response(response: Response) -> None:
    print(response.content)


print(get_status('https://www.google.com'))
