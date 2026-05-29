      # Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_in_variable = 5
print(my_in_variable)


my_in_to_str_variable = str(my_in_variable)
print(my_in_to_str_variable)
print(type(my_in_to_str_variable))




my_bool_variable = True
print(my_bool_variable)




                  #Concatenación de variables en un print
print(my_string_variable, my_in_to_str_variable , my_bool_variable)
print("Este es el valor de:",my_bool_variable)


#Algunas Funciones del sistema
print(len(my_string_variable))


#Variables en una sola linea     ¡Cuidado con abusar de esta Sintaxis!
name, surname , alias , age = "Brando" , "Erazo" , "Nazi" , 27
print("Mi llamo:" , name ,surname , ". Mi edad es:" , age , ". Y mi alias es:" , alias)


# Inputs
'''
name = input("¿Cuál es tu nombre?")
age = input("¿Cuántos años tienes?")

print(name)
print(age)
'''

#Cambiamos su tipo 
name = 37
age = "Brando"
print(name)
print(age)


#Forzamos el tipo ???
address: str = "Mi dirección"

address = True
address = 5
address = 1.2

print(type(address))