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

example: dict[int, str] = {1: 'rigo', 2: 'jose'}
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




