import random, math


def simulacion_cumple(m):
    dias = [random.randint(1, 365) for _ in range(m)]
    return len(dias) != len(set(dias))


def realizar_simulacion(m, n):
    victorias = sum(simulacion_cumple(m) for _ in range(n))
    derrotas = n - victorias
    return victorias, derrotas


def prob_empirica(victorias, total):
    return victorias / total


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

    for m in valores_m:
        print(f"\n--- Resultados para m = {m} ---")
        p_teorica = prob_teorica(m)
        print(f"Probabilidad teórica de coincidencia: {p_teorica:.4f}")
        
        for n in repeticiones:
            victorias, derrotas = realizar_simulacion(m, n)
            p_empirica = prob_empirica(victorias, n)
            print(f"Simulaciones: {n} -> Victorias: {victorias}, Derrotas: {derrotas}, Prob. empírica: {p_empirica:.4f}")


if __name__ == "__main__":
    main()