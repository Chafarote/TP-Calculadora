from funciones_calculadora import *

operando_a = "x"
operando_b = "y"
operacion = ""
resultado = ""

while True:
    match menu(operando_a, operando_b):
        case "1":
            operando_a = operando()
        case "2":
            operando_b = operando()
        case "3":
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
        case "5":
            break
    pausar_pantalla()
