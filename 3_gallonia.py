def gallons(bensiini_maara):
    litra = bensiini_maara * 3.785
    return f"{bensiini_maara} on {litra:.2f} litraa"

cantidad = int(input("Anna bensiini määrä, negatiivinen määrä lopeta ohjelma: "))

while True:

    convertir = gallons(cantidad)
    print(convertir)
    cantidad = int(input("Anna bensiini määrä, negatiivinen määrä lopeta ohjelma: "))
    if cantidad < 0:
        break



