import math
def pizza_hinta(koko, hinta):
    pinta_ala = koko * math.pi
    precio_cm2 = hinta / pinta_ala
    return f"{precio_cm2:.2f} euroa per cm2"

while True:
    diametro_1 = int(input("Anna pizza 1 koko (cm): "))
    diametro_2 = int(input("Anna pizza 2 koko (cm): "))
    precio_1 = int(input("Anna pizza 1 hinta (euroa): "))
    precio_2 = int(input("Anna pizza 2 hinta (euroa): "))
    calcular = pizza_hinta(diametro_1, precio_1)
    calcular_2 = pizza_hinta(diametro_2, precio_2)
    print(f"Pizza 1 hinta on: {calcular}")
    print(f"Pizza 2 hinta on: {calcular_2}")
    if calcular > calcular_2:

        print("\nPizza 1 on halvempi")
        break
    else:
        #print(calcular_2(diametro_2, precio_2))
        print(f"\nPizza 2 on halvempi")
        break