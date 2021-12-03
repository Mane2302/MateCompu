import math

def Suma(num_1, num_2):
    return (num_1 + num_2)

def Resta(num_1, num_2):
    return (num_1 - num_2)

def Multiplicacion(num_1, num_2):
    return (num_1 * num_2)

def Divicion(num_1, num_2):
    return (num_1 / num_2)

def Potencia(num_1, num_2):
    return (num_1 ** num_2)

def Modulo(num_1, num_2):
    return (num_1 % num_2)

def Raiz_Cuadrada(num1):
    return (math.sqrt(num1))

print("********MASTER-CALCULATOR********\n"
      "BY EMMANUEL ROQUE NEPONUCENO\n"
      "16276360@uagro.mx\n"
      "*********************************")

empieza =int(1)
while empieza==1:
    print("Menu de opciones\n"
          "(1) SUMA\n"
          "(2) RESTA\n"
          "(3) MULTIPLICACION\n"
          "(4) DIVICION\n"
          "(5) POTENCIA\n"
          "(6) MODULO\n"
          "(7) Raíz Cuadrada")

    option = int(input('Ingresa el número de la opción que desees elegir\n'))

    if option==1:
        num_1=float(input("Ingresa el primer número a sumar: "))
        num_2= float(input("Ingresa el segundo número a sumar: "))
        print("El resultado de",num_1 , "+" ,num_2, " = " , Suma(num_1,num_2))

    elif option==2:
        num_1 = float(input("Ingresa el primer número a restar: "))
        num_2 = float(input("Ingresa el segundo número a restar: "))
        print("El resultado de",num_1 , "-" ,num_2, " = " , Resta(num_1, num_2))

    elif option==3:
        num_1 = float(input("Ingresa el primer número a multiplicar: "))
        num_2 = float(input("Ingresa el segundo número a multiplicar: "))
        print("El resultado de",num_1 , "*" ,num_2, " = " , Multiplicacion(num_1, num_2))

    elif option==4:
        num_1 = float(input("Ingresa el primer número a dividir: "))
        num_2 = float(input("Ingresa el segundo número a dividir: "))
        print("El resultado de",num_1 , "/" ,num_2, " = " , Divicion(num_1, num_2))

    elif option==5:
        num_1 = float(input("Ingresa la base de la potencia: "))
        num_2 = float(input("Ingresa el exponente de la potencia: "))
        print("El resultado de",num_1 , "^" ,num_2, " = " , Potencia(num_1, num_2))

    elif option==6:
        num_1 = float(input("Ingresa el dividendo: "))
        num_2 = float(input("Ingresa el divisor: "))
        print("El resultado de",num_1 , "%" ,num_2, " = " , Modulo(num_1, num_2))

    elif option==7:
        num_1 = float(input("Ingresa el radicando: "))
        print("El resultado de la raíz cuadrada de ",num_1,  " = " , Raiz_Cuadrada(num_1))
    else:
        print("opción no válida")

    empieza=int(input("¿Desea usar nuevamente el programa?\n"
                         "(1) SI\n"
                         "(0) NO\n"))
