import random


# 1. Función que simula el problema del cumpleaños
def simulacion_cumple(m):
    dias = [random.randint(1, 365) for _ in range(m)]
    return len(dias) != len(set(dias))  # Retorna booleano


# 2. Ejecutar la función multiples veces
def realizar_simulacion(m, n):
    victorias = sum(simulacion_cumple(m) for _ in range(n))
    derrotas = n - victorias
    return victorias, derrotas  # Devuelve la cantidad de victorias y derrotas


# 3. Calcular la probabilidad empirica
def prob_empirica(victorias, total):
    return victorias / total


# 4. Calcular la probabilidad teorica
def prob_teorica(m):
    if m > 365:
        return 1.0  # si hay mas personas que dias entonces seguro hay coincidencia
    p_sin = 1.0
    for i in range(m):
        p_sin *= (365 - i) / 365
    return 1 - p_sin


def main():
    valores_m = [10, 20, 30, 40, 50]
    repeticiones = [1000, 10000, 100000]

    # Para cada valor de m se ejecuta la simulación con sus respectivas repeticiones
    for m in valores_m:
        print(f"\n" + "-" * 25 + f" Resultados para m = {m} " + "-" * 25)
        p_teorica = prob_teorica(m)
        print(f"Probabilidad teórica de coincidencia: {p_teorica: .4f}")

        for n in repeticiones:
            victorias, derrotas = realizar_simulacion(m, n)
            p_empirica = prob_empirica(victorias, n)
            print(
                f"Simulaciones: {n} -> Victorias: {victorias} | Derrotas: {derrotas}"
                f" | Prob. empírica: {p_empirica: .4f}")


if __name__ == "__main__":
    main()
