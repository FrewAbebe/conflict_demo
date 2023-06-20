<<<<<<< HEAD
def hello_world(state):
    print(f'Hello World {state}!')


def main():
    hello_world('New York')
=======
def hello_world(city):
    print(f'Hello World {city}!')


def main():
    hello_world('NYC')
>>>>>>> 62f6a5ac52bd51c481c5cabfc74263d079a59708
def hello_world(city, state):
    print(f'Hello World {city}, {state}!')


def main():
    hello_world('NYC', 'New York')

main()
