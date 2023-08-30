#De la siguiente lista realizar las funciones que obtengan lo siguientes:
# Obtener el promedio
# La cantidad de aspirantes que reprobaron


lista = [8,9,10,6,6,7,8,9,5,6,7,6,8,8,9,9,5,6,7,9,10,7,8,9,9]


suma = 0
cont = 0

for valor in lista:
    suma = suma + valor
    if valor <=5:
        cont += 1  

contador = len(lista)
promedio = suma / contador
print(f"El promedio es {promedio}")
print (f"El numero de reprobados es  {cont}")







