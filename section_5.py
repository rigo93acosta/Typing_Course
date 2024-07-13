from typing import override, TypedDict, Unpack

class Computer:
    def __init__(self, name: str) -> None:
        self.name = name

    def turn_on(self) -> None:
        print(f'{self.name} is turning on.')

    def turn_off(self) -> None:
        print(f'{self.name} is turning off.')

class Windows(Computer):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    @override
    def turn_on(self) -> None:
        print(f'Turning on my awesome Windows computer!')

class Item(TypedDict):
    name: str
    value: float

def case_unpack() -> None:

    def info(name: str, /, **kwargs: Unpack[Item]) -> None: # Add / to make sure that the name is a positional argument
        print(name, kwargs, sep=': ')
    
    info(name='Laptop', value=100)


if __name__ == '__main__':
    # computer: Windows = Windows('Windows')
    # computer.turn_on()

    case_unpack()