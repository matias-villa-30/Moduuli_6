import random

def noppa(y):
    dado = random.randint(1, y)
    return dado


y = int(input("Anna arvo: "))

while True:
    dado = noppa(y)
    print(dado)
    if dado == y:
        break