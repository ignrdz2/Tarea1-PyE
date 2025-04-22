import random

# Parámetros del problema
probabilidad_enfermedad = 1 / 10000
probabilidad_falso_positivo = 0.02
probabilidad_falso_negativo = 0.01
probabilidad_verdadero_positivo = 1 - probabilidad_falso_negativo

numero_personas = 1_000_000
repeticiones = 50

def simular():
    resultados = []

    for _ in range(repeticiones):
        # Determinar si cada persona tiene o no la enfermedad
        personas_con_enfermedad = [random.random() < probabilidad_enfermedad for _ in range(numero_personas)]

        resultados_test = [False] * numero_personas

        # Test para personas con enfermedad
        for i in range(numero_personas):
            if personas_con_enfermedad[i]:
                resultados_test[i] = random.random() < probabilidad_verdadero_positivo
            else:
                resultados_test[i] = random.random() < probabilidad_falso_positivo

        # Casos positivos
        cantidad_test_positivos = sum(resultados_test)
        casos_reales_entre_positivos = sum(personas_con_enfermedad[i] for i in range(numero_personas) if resultados_test[i])

        if cantidad_test_positivos == 0:
            probabilidad_condicional = 0
        else:
            probabilidad_condicional = casos_reales_entre_positivos / cantidad_test_positivos

        resultados.append(probabilidad_condicional)

    return resultados

def calcular_valor_teorico():
    p_enfermedad = probabilidad_enfermedad
    p_no_enfermedad = 1 - p_enfermedad
    p_test_pos_dado_enfermedad = probabilidad_verdadero_positivo
    p_test_pos_dado_no_enfermedad = probabilidad_falso_positivo

    p_test_pos = p_test_pos_dado_enfermedad * p_enfermedad + p_test_pos_dado_no_enfermedad * p_no_enfermedad
    p_enfermedad_dado_test_pos = (p_test_pos_dado_enfermedad * p_enfermedad) / p_test_pos

    return p_enfermedad_dado_test_pos

if __name__ == "__main__":
    resultados = simular()

    print("Primeras 10 repeticiones:")
    print("Repetición | Probabilidad estimada")
    print("-" * 35)
    for i in range(10):
        print(f"{i+1:10d} | {resultados[i]:.6f}")

    print("\nÚltimas 10 repeticiones:")
    print("Repetición | Probabilidad estimada")
    print("-" * 35)
    for i in range(len(resultados) - 10, len(resultados)):
        print(f"{i+1:10d} | {resultados[i]:.6f}")

    promedio = sum(resultados) / len(resultados)
    print("\nPromedio de las 50 ejecuciones:")
    print(f"{promedio:.6f}")

    valor_teorico = calcular_valor_teorico()
    print("\nValor teórico (teorema de Bayes):")
    print(f"{valor_teorico:.6f}")
