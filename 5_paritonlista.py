def pariton(numerot: list):
    for item in numerot:
        if item % 2 != 0:
            numerot.remove(item)
    return numerot

