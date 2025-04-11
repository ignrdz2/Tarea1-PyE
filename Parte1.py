def main():
    print("s")

if __name__ == "__main__":
    main()
    
import random

def monty_hall_game():
    # Definir las tres puertas
    doors = [1, 2, 3]
    # Colocar el auto detrás de una puerta al azar
    car_door = random.choice(doors)
    
    # Solicitar al usuario que escoja una puerta
    while True:
        try:
            initial_choice = int(input("Elige una puerta (1, 2 o 3): "))
            if initial_choice in doors:
                break
            else:
                print("Por favor, ingresa un número válido (1, 2 o 3).")
        except ValueError:
            print("Entrada no válida. Ingresa un número (1, 2 o 3).")
    
    print(f"\nHas elegido la puerta: {initial_choice}")
    
    # El presentador abre una puerta que no sea la elegida por el usuario ni la que oculta el auto.
    possible_reveals = [door for door in doors if door != initial_choice and door != car_door]
    host_reveal = random.choice(possible_reveals)
    print(f"El presentador abre la puerta {host_reveal}, revelando una cabra.")
    
    # Preguntar al usuario si desea cambiar de puerta
    while True:
        change = input("¿Deseas cambiar tu elección? (s/n): ").strip().lower()
        if change in ['s', 'n']:
            break
        else:
            print("Por favor, ingresa 's' para sí o 'n' para no.")
    
    # Determinar la elección final según la respuesta
    if change == 's':
        # La nueva elección es la única puerta que queda cerrada
        final_choice = [door for door in doors if door not in (initial_choice, host_reveal)][0]
        print(f"\nCambias tu elección. La nueva puerta elegida es: {final_choice}")
    else:
        final_choice = initial_choice
        print(f"\nTe quedas con tu elección inicial: la puerta {final_choice}")
    
    # Comprobar si el usuario gana
    if final_choice == car_door:
        print(f"¡Felicidades! Ganaste el auto, que estaba detrás de la puerta {car_door}.")
    else:
        print(f"Lo siento, no ganaste el auto. El auto estaba detrás de la puerta {car_door}.")

# Ejecutar el juego de forma interactiva
if __name__ == "__main__":
    monty_hall_game()
