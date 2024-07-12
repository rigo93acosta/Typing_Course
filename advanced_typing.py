from typing import Any, Final, Iterable, Sequence, Callable, Protocol
from sys import getsizeof
from datetime import datetime

class Printer(Protocol):
    def print(self, megazine: str) -> None:
        ...
    
    def copy(self, megazine: str, copies: int) -> None:
        ...

class LazerPrinter:
    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version

    def print(self, megazine: str) -> None:
        print(f'{self.name} ({self.version}) is printing: "{megazine}".')
    
    def copy(self, megazine: str, copies: int) -> None:
        print(f'{self.name} ({self.version}) is making {copies} of: "{megazine}".')

def list_elements(elements: Iterable) -> None:
    for i, element in enumerate(elements, start=1):
        print(i, element, sep=': ')

def display_size(user_input: Any) -> None:
    print(f'{user_input} -> {getsizeof(user_input)} bytes')

def get_first_element(sequence: Sequence[int]) -> int:
    return sequence[0] if sequence else -1

def get_time() -> str:
    return f'{datetime.now():%H:%M:%S}'

def repeat(func: Callable, amount: int) -> None:
    for i in range(amount):
        print(f'{i + 1}: {func()}')

def print_int(text: str, print_func: Callable[[str], None]) -> None:
    '''
    @print_func: Callable[[str], None] -> Función que recibe un string y no retorna nada
    '''
    print_func(text)

def loud_print(text: str) -> None:
    print(f'{text.upper()}!')

def silent_print(text: str) -> None:
    print(f'({text.lower()})')

def get_leters(text: str) -> list[str]:
    return list(text)

def case_any() -> None:
    display_size([1,2,3])
    display_size('hello')
    display_size(1)
    display_size(None)
    display_size(1.0)

def case_final() -> None:
    CONSTANT: Final[str] = 'I am a constant'
    print(CONSTANT * 2)
    CONSTANT = 'Hello world'
    PI: Final[float] = 3.14159
    print(PI * 2)
    PI = 3.14

def case_iterables() -> None:
    people: list[str] = ['Mario', 'Luigi', 'Peach']
    list_elements(people)
    # list_elements(10) # Warning no es lo esperado
    numbers: list[int] = [1, 2, 3]
    list_elements(numbers)

def case_sequences() -> None:
    sample_set: set[int] = {1, 2, 3}
    sample_list: list[int] = [1, 2, 3]
    print(get_first_element(sample_list))
    # print(get_first_element(sample_set)) # Error de tipo pues unordered collection

def case_callable() -> None:
    repeat(get_time, 3)
    # repeat('hello', 3) # Error de tipo pues no es callable
    print_int('Hello', loud_print)
    print_int('Hello', silent_print)
    print_int("Hello", get_leters)

def case_protocol() -> None:
    lp: Printer = LazerPrinter('Lazer Printer', version=1)
    
    def print_megazine(printer: Printer, megazine: str) -> None:
        printer.print(megazine)
        print('Performing extra logic...')
        printer.copy(megazine, 5)
        print('Shutting down printer...')

    print_megazine(lp, 'Python Times')

if __name__ == '__main__':
    # case_any() 
    # case_final()
    # case_iterables()
    # case_sequences()
    # case_callable()
    case_protocol()