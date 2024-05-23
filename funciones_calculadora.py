from os import system

def limpiar_pantalla():
    """Limpia la pantalla
    """
    system("cls")

def pausar_pantalla():
    """Pausa la pantalla
    """
    system("pause")

def menu(x:int, y:int)-> str:
    """Menu de opciones

    Args:
        x (int): Recibe el primer operando
        y (int): Recibe el segundo operando

    Returns:
        str: Retorna la opcion que eliga el usuario
    """
    limpiar_pantalla()
    print("---Calculadora con funciones---")
    print("-------------------------------")
    print(f"1- Ingresar 1er operando ({x})")
    print(f"2- Ingresar 2do operando ({y})")
    print("3- Calcular...")
    print("4- Informar resultado")
    print("5- Salir")
    return input("Ingrese una opcion: ")

def operando()->int:
    """Pide al usuario un numero

    Returns:
        int: Retorna un numero entero despues de validarlo
    """
    numero = input("Ingrese un numero: ")
    while numero == "" or not numero.isdigit():
        numero = input("Reingrese un numero: ")
    return int(numero)

def menu_calcular(x:int, y:int):
    """Menu en el que se elige la operacion a realizar

    Args:
        x (int): Ingresa el primer operando
        y (int): Ingresa el segundo operando

    Returns:
        str: Retorna la opcion elegida por el usuario
    """
    print("Calcular")
    print(f"a) Calcular la suma ({x}+{y})")
    print(f"b) Calcular la resta ({x}-{y})")
    print(f"c) Calcular la division ({x}/{y})")
    print(f"d) Calcular la multiplicacion ({x}*{y})")
    print(f"e) Calcular factorial ({x}! {y}!)")
    return (input("Ingrese una opcion: "))

def suma(x:int, y:int)-> int:
    """Suma dos operandos

    Args:
        x (int): Ingresa el primer operando
        y (int): Ingresa el segundo operando

    Returns:
        int: Retorna el resultado de la suma entre los dos operandos
    """
    return x + y

def resta(x:int, y:int)-> int:
    """Resta dos operandos

    Args:
        x (int): Ingresa el primer operando
        y (int): Ingresa el segundo operando

    Returns:
        int: Retorna el resultado de la resta entre ambos operandos
    """
    return x - y

def division(x:int, y:int)-> float:
    """Divide dos operando

    Args:
        x (int): Ingresa el primer operando
        y (int): Ingresa el segundo operando

    Returns:
        float: En caso de que el segundo operando sea 0 retorna -1, si no retorna el resultado de la division entre operandos
    """
    if y == 0:
        retorno = -1
    else: 
        retorno = x / y
    return retorno


def multiplicacion(x:int, y:int)-> int:
    """Multiplica dos operandos

    Args:
        x (int): Ingresa el primer operando
        y (int): Ingresa el segundo operando

    Returns:
        int: Retorna el resultado de la multiplicacion entre operandos
    """
    return x * y

def factorial(operando:int)->int:
    """Calcula el factorial de un entero

    Args:
        operando (int): Ingresa un entero

    Returns:
        int: Retorna el factorial
    """
    resultado = 1
    for i in range(2, operando + 1):
        resultado *= i
    return resultado

def informar_resultado(operacion:str, x:int, y:int, resultado:float)-> None:
    """Informa el resultado de la operacion elegida

    Args:
        operacion (str): Ingresa la opcion corresponiente a la operacion que pide el usuario
        x (int): Ingresa el primer operando
        y (int): Ingresa el segundo operando
        resultado (float): Ingresa el resultado de la operacion elegida
    """
    match operacion:
        case "a":
            print(f"El resultado de {x} + {y} es: {resultado}")
        case "b":
            print(f"El resultado de {x} - {y} es: {resultado}")
        case "c":
            if resultado == -1:
                print(f"No se puede dividir por 0")
            else:
                print(f"El resultado de {x} / {y} es: {resultado}")
        case "d":
            print(f"El resultado de {x} * {y} es: {resultado}")
        case "e":
            print(f"El factorial de {x} es: {resultado["resultado_1"]} y El factorial de {y} es: {resultado["resultado_2"]}")
        case _:
            print(f"No se eligio una operacion a realizar!")





