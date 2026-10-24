
Saldototal = 1000


def Deposito(num1):
    global Saldototal
    if num1 < 0:
        print("La cantidad debe ser mayor que 0")
        return Saldototal
    else:
        resultado = num1 + Saldototal
        return resultado


def retiro(num1):
    global Saldototal
    if num1 > Saldototal:
        print("No puede retirar más dinero del que tiene")
        return Saldototal
    else:
        resultado = Saldototal - num1
        return resultado


def menu():
    print("""
*** MENU ***
1. Consultar dinero
2. Depositar dinero
3. Retirar dinero
0. Salir
""")


def leerOpcion():
    opcion = input(">>> Opción: ")
    while opcion < "0" or opcion > "3":
        print("Error. Opción no válida.")
        input("Presione Enter para continuar...")
        print("\n\n\n")
        menu()
        opcion = input(">>> Opción: ")

    return int(opcion)


def ConsultarSaldo():
    print("\n\n1. Consultar el saldo")
    print("Su saldo es de:", Saldototal)


def Depositar():
    print("\n\n2. Depositar dinero")
    depositacion = int(input("\nIngrese la cantidad a depositar: "))
    print("Nuevo saldo:", Deposito(depositacion))
    return Deposito(depositacion)


def Retirar():
    print("\n\n3. Retirar dinero")
    retiracion = int(input("\nIngrese la cantidad a retirar: "))
    print("Nuevo saldo:", retiro(retiracion))
    return retiro(retiracion)


# Programa principal
while True:
    menu()
    opcion = leerOpcion()

    match opcion:
        case 1:
            ConsultarSaldo()

        case 2:
            Saldototal = Depositar()

        case 3:
            Saldototal = Retirar()

        case 0:
            print("Gracias por usar la calculadora...")
            break

    input("Presione Enter para continuar...")

 









