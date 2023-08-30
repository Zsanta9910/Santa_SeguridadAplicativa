
print  ("Este es un programa que funciona como calculadora")
print ("El numero 1 = a la suma de los valores ingresados")
print ("El numero 2 = a la resta de los valores ingresados")
print ("El numero 3 = a la multiplicacion de los valores ingresados")
print ("El numero 4 = a la division de los valores ingresados")

a = int (input("Ingresa el primer valor :"))
b = int (input("Ingresa el segundo valor :"))

c = int (input("Que operacion deseas realizar? "))


if (c == 1):
    x = a + b
    print (x)
    
elif(c == 2):
    x = a - b
    print (x)
    
elif(c == 3):
    x = a * b
    print (x)

elif(c == 4):
    x = a / b
    print (x)
    
else:
    print("Favor de seleccionar una opcion valida")
