from funciones_calculadora import *

operando_a = "x"
operando_b = "y"
operacion = ""
resultado = ""

while True:
    match menu(operando_a, operando_b):
        case "1":
            if operando_a == "x":
                operando_a = operando()
            else:
                print("Ya se ingreso el primer operando")
        case "2":
            if operando_b == "y":
                operando_b = operando()
            else:
                print("Ya se ingreso el segundo operando")
        case "3":
            if operando_a == "x" or operando_b == "y":
                print("No se ingresaron operandos")
            else:
                operacion = menu_calcular(operando_a, operando_b)
                if operacion == "a":
                    resultado = suma(operando_a, operando_b)
                elif operacion == "b":
                    resultado = resta(operando_a, operando_b)
                elif operacion == "c":
                    resultado = division(operando_a, operando_b)
                elif operacion == "d":
                    resultado = multiplicacion(operando_a, operando_b)
                elif operacion == "e":
                    resultado = {"resultado_1":factorial(operando_a), "resultado_2":factorial(operando_b)}
        case "4":
            informar_resultado(operacion, operando_a, operando_b, resultado)
            operando_a = "x"
            operando_b = "y"
        case "5":
            break
        case _:
            print("No se ingreso una opcion valida")
    pausar_pantalla()
