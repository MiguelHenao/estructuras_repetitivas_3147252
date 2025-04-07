##Diccionarios:

#Son colecciones de datos
#Cada  elemento en un diccionario
##Se puede diidir en 2 partes 
# ## 1. clave: el nombre del
# ## 2.


pais = {
    
    "Nombre": "colombia",
    "Capital" : "Bogota",
    "idioma" : "Español",
    "Poblacion": 51,
    "superficie": 1141748,
    "Moneda": "Peso colombiano",
    "ciudades": [
        "BOGOTA"
        "MEDELLIN"
        "CALI"
        "BARRANQUILLA"
        "CARTAGENA"
    ]
    
}

#ACCEDER A PROPIEDADES
print ("CAPITAL DE COLOMBIA", pais["Capital"])
print ("Y SE HABLA", pais ["idioma"])
print ("HABITAN", pais["Poblacion"])
print ("Y SUS CIUDADES SON:")
for ciudad in pais ["ciudades"]:
    print(ciudad)