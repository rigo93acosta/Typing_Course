from typing import TypedDict, NotRequired, Required, Literal, TypeAlias, Callable, NewType
from typing import Generator, Iterator, Self

class Coordinate(TypedDict):
    x: float
    y: float
    label: str
    category: NotRequired[str]

def case_typed_dict():
    coordinate: Coordinate = {'x':20.0, 'y': 30.0, 'label': 'A', 'category': 'Finance'}
    print(coordinate)

    # Vote = TypedDict('Vote', {'for': int, 'against': int})
    Vote = TypedDict('Vote', 
                     {'for': int, 
                      'against': int,
                      'topic': Required[str]},
                     total=False)
    
    vote: Vote = {'for': 10, 'against': 5}
    print(vote)

def case_literal() -> None:
    Mode = Literal['r', 'w', 'a']
    
    def read_file(file: str, mode: Mode) -> None:
        print(f'Reading {file} in "{mode}" mode.')

    read_file('data.txt', 'r')

def case_typeAlias() -> None:

    OptionalStr: TypeAlias = str | None

    Mode: TypeAlias = Literal['r', 'w', 'a']
    Printer: TypeAlias = Callable[[str], str]

    FruitType: TypeAlias = 'Fruit'

    class Fruit:
        def __init__(self, name: str) -> None:
            self.name = name    

        def fruit_method(self) -> FruitType:
            return self

def case_newType() -> None:
    
    # UserId: TypeAlias = int
    UserId = NewType('UserId', int)

    def get_user(userid: UserId) -> str | None:
        users: dict = {0: 'Mario', 1: 'Luigi'}
        return users.get(userid)
    
    # Con NewType, el tipo de dato es más restrictivo
    # print(get_user(0))
    # print(get_user(False)) 
    print(get_user(UserId(0)))

def case_self() -> None:
    
    class File:
        def __init__(self, filepath: str) -> None:
            self.filepath = filepath

        @classmethod
        def create_file(cls, name: str, ext: str) -> Self:
            return cls(f'{name}.{ext}')
        
        def __enter__(self) -> Self:
            print(f'Opening "{self.filepath}"...')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb) -> None:
            print(f'Closing "{self.filepath}"...')
    
    file: File = File.create_file('data', 'txt')
    print(file.filepath)

    with File('data.txt') as f:
        print(f.filepath)

def case_generator():
    def generate() -> Generator[int, None, str]:
        for i in range(3):
            yield i

    return 'SOME_VALUE'

    numbers = generate()
    print(next(numbers))
    print(next(numbers))

if __name__ == '__main__':
    case_typed_dict()
    case_literal()
    case_typeAlias()
    case_newType()
    case_self()
    case_generator()