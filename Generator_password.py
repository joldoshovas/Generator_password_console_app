import random
import string
from urllib import response
adjectives = ['sleepy', 'slow', 'hot', 'cold', 'big', 'red', 'orange', 'yellow', 'green', 'blue', 'old', 'white', 'free', 'brave']
nouns = ['apple', 'dinosaur', 'ball', 'cat', 'goat', 'dragon', 'car', 'duck', 'panda']
print('Добро пожаловать!')
while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
        password = adjective + noun + str(number) + special_char
        print('Новый пароль: %s' % password )
    response = input('Сгенерировать новый пароль? Введите д или н:')
    if response == 'н':
        break
