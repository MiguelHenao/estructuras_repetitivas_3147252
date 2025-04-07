# Coleccion de paises:
paises = [
    {
        "nombre": "Colombia",
        "capital": "Bogotá",
        "moneda": "Peso colombiano",
        "ciudades": [
            {
                "nombre": "Bogotá",
                "poblacion": "7.9",
                "fundacion": "1538",
            },
            {
                "nombre": "Medellín",
                "poblacion": "2.6",
                "fundacion": "1616",
            },
            {
                "nombre": "Cali",
                "poblacion": "2.2",
                "fundacion": 1536,
            },
        ]
    },
    {
        "nombre": "Perú",
        "capital": "Lima",
        "moneda": "Sol",
        "ciudades": [
            {
                "nombre": "Lima",
                "poblacion": "9.7",
                "fundacion": "1535",
            },
            {
                "nombre": "Cuzco",
                "poblacion": "0.4",
                "fundacion": "1100",
            },
        ]
    },
    {
        "nombre": "Argentina",
        "capital": "Buenos Aires",
        "moneda": "Peso argentino",
        "ciudades": [
            {
                "nombre": "Misiones",
                "poblacion": "1.2",
                "fundacion": "1900",
            },
            {
                "nombre": "Rosario",
                "poblacion": "1.3",
                "fundacion": "1852",
            },
        ]
    },
]

# Iterar cada país
print("--------------")
print("Recorrido de Países")
print("--------------")

for pais in paises:
    print("Nombre:", pais["nombre"])
    print("Capital:", pais["capital"])
    print("Moneda:", pais["moneda"])
    for ciudad in pais["ciudades"]:
        print(f"- {ciudad['nombre']}: {ciudad['poblacion']} millones de habitantes")
    print("------------------------")
