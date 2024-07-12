from typing import Any, Final, Iterable, Sequence, Callable, Protocol

# Exercise 1
CONSTANT = 2


# Exercise 2
def get_repr(obj):
    return repr(obj)


my_repr = get_repr('I love typing!')
print(my_repr)

# Exercise 3
numbers = [20, 5, 30, 100]


def get_first_element(elements):
    return elements[0] if elements else -1


print(get_first_element(numbers))


# Exercise 4:
def say_hello(person, greeting):
    print(f'{greeting}, {person}!')


def greet(people, greeting, hello_func):
    for person in people:
        hello_func(person, greeting)


friends = ['Mario', 'Luigi', 'James']
greet(friends, 'Yo', say_hello)


# Exercise 5:
class Camera:
    def take_picture(self):
        ...

    def turn_on(self):
        ...

    def turn_off(self):
        ...


def automate_photo(camera):
    camera.turn_on()
    photo = camera.take_picture()
    camera.turn_off()

    return photo


class Canon:
    def __init__(self, name):
        self.name = name

    def take_picture(self):
        print(f'{self.name} took a picture!')
        return 'image.jpg'

    def turn_on(self):
        print(f'Turning on {self.name}.')

    def turn_off(self):
        print(f'Turning off {self.name}...')


my_camera = Canon('CanonDigital')
automate_photo(my_camera)
