import random

# Simula una única partida
def jugar_una_vez(cambiar):
    puertas = [1, 2, 3]
    auto = random.choice(puertas)
    eleccion = random.choice(puertas)

    # El presentador abre una puerta con cabra (ni la elegida ni donde está el auto)
    abiertas = [p for p in puertas if p != eleccion and p != auto]
    abierta = random.choice(abiertas)

    if cambiar:
        # Cambio a la puerta que no elegí ni abrió el presentador
        final = [p for p in puertas if p != eleccion and p != abierta][0]
    else:
        final = eleccion

    return final == auto  # Devuelvo True si gané

# Corre varias simulaciones y muestra los resultados
def simular(cambiar):
    print("\nEstrategia:", "Cambiar" if cambiar else "No cambiar")
    for rep in [1000, 10000, 100000]:
        ganadas = 0
        for _ in range(rep):
            if jugar_una_vez(cambiar):
                ganadas += 1
        perdidas = rep - ganadas
        frecuencia = ganadas / rep
        print("Juegos:", rep, "| Ganadas:", ganadas, "| Perdidas:", perdidas, "| Éxito:", round(frecuencia, 4))

# Versión para jugar como usuario
def jugar_interactivo():
    puertas = [1, 2, 3]
    auto = random.choice(puertas)

    while True:
        try:
            eleccion = int(input("Elegí una puerta (1, 2 o 3): "))
            if eleccion in puertas:
                break
            else:
                print("Debe ser 1, 2 o 3.")
        except:
            print("Entrada inválida.")

    posibles = [p for p in puertas if p != eleccion and p != auto]
    abierta = random.choice(posibles)

    print("El presentador abre la puerta", abierta, "y hay una cabra.")

    cambiar = input("¿Querés cambiar de puerta? (s/n): ").strip().lower() == 's'

    if cambiar:
        eleccion = [p for p in puertas if p != eleccion and p != abierta][0]

    if eleccion == auto:
        print("¡Ganaste el auto!")
    else:
        print("No ganaste. El auto estaba en la puerta", auto)

# Menú
def main():
    print("Problema de Monty Hall")
    print("1. Jugar como participante")
    print("2. Simular muchas partidas")
    print("3. Salir")

    while True:
        op = input("\nElegí una opción (1-3): ").strip()
        if op == '1':
            jugar_interactivo()
        elif op == '2':
            simular(True)
            simular(False)
        elif op == '3':
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
