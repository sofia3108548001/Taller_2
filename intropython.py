# comentario de una linea 
# tolo lo que va despues es ignorado por el interprete de python 
#interprete de pyton 

#variable: espacio de memoria, con nombre, donde guardo valores
#los nombre de variables deben ser cortos, descrptivos, no tener espacion en blanco, ni caracteres especiales. no deben empezar por numero 

#descriptivo significa que respresenta la categoria del dato que quiero guardar 

#En pyton las variables pueden contener cualquier dato de tipo primitivo 
#Números (enteros o reales), cadenas de caracteres (string ) booleanos (tru, false )
#caracteres (letras)


variable= 1 
variable= 'juventus divino tesoro, te vas para no volver, cuando quiero llorar no lloro'
variable= True 
variable= 'a' 
variable= 3.1415926535

#para asignar un valor a la variable se usa el operador =


#OPERADORES: Mecanismo para obtener un dato a partir de otros datos. # los datos qie intervienen se llaman operandos.

#Arimeticos: + - * %
#De comparacion: Retornan True or False. < >= <= == !=
#Los de logica booleana: OR AND. Retornan True or False de acuerdo 
#a una tabla de verdad. Los operadores siempre son booleanos ( True or False)

a=True 
b=False 

print( a and b)

#los operadores booleanos y de comparacion son muy uyilizamos al definir condiciones 

#Estructura de control de codigo: en general un programa se ejecuta linea por linea de manera secuencial. se puede romper esa secuencialidad empleando un conjunto de secuencias (expresiones) que permite 
#1. seleccionar la ejecución de un bloque de codigo 
#2. Repetir la ejecucion de un boque de codigo 
#3. seleccionar entre ejecutar un bloque de codigo u otro bloque de codigo. 
# de esta manera ppodemos "romper" la secuencalidad 
# Principios del paradigma de la programacion 

#1 sentencia if. si se cumple una condicion (se ejecuta un bloque de codig) se ejecuta un bloque de codigo 
print ("linea 1")
print("linea 2")
if 5>8 or 3<7:

    print("esto se muestra si la condicion es verdadera")
    
else: 
    print("Esto muestra si la condicion es false")
    
entrada= int(input("cuantos años tiene?"))

if entrada<18:
    print("eres un menor de edad ")
    
else:
    print("Ya eres mas grande ")
    
    
#Taller" programa em pyton que genere un numero aleatorio ente 1-12 si el numero es 7 gano y si no deje de jugar 
    

