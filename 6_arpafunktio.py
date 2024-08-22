import random

def noppa():
    dado = random.randint(1, 6)
    return dado

while True:
    kuusi = noppa()
    print(kuusi)
    if kuusi == 6:
        break