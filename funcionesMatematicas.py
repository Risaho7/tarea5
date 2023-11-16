# Definición de la función 'sumar' recibe dos parámetros y devuelve la suma
def sumar(a, b): 
    return a + b

# Definición de la función 'restar' recibe dos parámetros y devuelve la resta
def restar(a, b):
    return a - b

# Definición de la función 'multiplicar' recibe dos parámetros y devuelve la multiplicación
def multiplicar(a, b):
    return a * b

# Definición de la función 'dividir' recibe dos parámetros y devuelve la división
def dividir(a, b):
    try:
        # Intenta realizar la división
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        # Captura la excepción si se intenta dividir entre cero
        raise ValueError("No se puede dividir entre cero")

# Bloque principal para probar las funciones
if __name__ == "__main__":
    print(sumar(5, 3))
    print(restar(5, 3))
    print(multiplicar(5, 3))
    print(dividir(5, 3))