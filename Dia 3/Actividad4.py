




alumnos = {
    "Juan" : 8 ,
    "Giselle" : 9 ,
    "Damian" : 5 ,
    "Ricardo" : 6 ,
    "Yaotzin" : 6 ,
    "Erick" : 7,
    "Mario" : 8 ,
    "Edgar" : 9 ,
    "Fernanda" : 5 ,
    "Daniel" : 6 ,
    "Jesus" : 7 ,
    "Damian" : 8,
    "Yemahina" : 6 ,
    "Eduardo" : 9 ,
    "Bryan" : 9 ,
    "Mariano" : 10 ,
    "Alberto" : 8 
    
}


alumnos["Juan"]
a = 0
for promedio in alumnos:
    a = a + alumnos[promedio] / len(alumnos)
    if (alumnos[promedio]==10):
        print ("Los alumnos que tuvieron la calificacion mas ALTA son: ", promedio)
    elif (alumnos[promedio]==5):
        print ("Los alumnos que tuvieron la calificacion mas BAJA son: ", promedio)
        
print ("El promedio del grupo es :" , a)
    

    
    





