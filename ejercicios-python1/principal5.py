"""
    @reroes
    Manejo de estructuras
"""

diccionario = {"nombre": "René", "apellidos": "Elizalde"}
diccionario2 = {"nombre": "Erick", "apellidos": "Jaramillo"}

lista = [diccionario, diccionario2] 

for l in lista:
    midiccionario = l
    print("Imprimir diccionario")
    print("Mi nombre es: %s y mi apellido es: %s" % 
    (midiccionario["nombre"], midiccionario["apellidos"] ))


