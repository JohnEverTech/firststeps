# Declarando variables de los datos a usar

VAlOR_PI = 3.14 # Mi Variable PI que será constante

radio_circulo = float(input("Ingrese el radio del circulo a calcular: "))
radio_cilindro = float(input("Ingrese el radio del cilindro a calcular: "))
altura_cilindro = float(input("Ingrese la altura del cilindro a calcular: "))

# Funcion para hallar el área de un circulo
def calcular_radio_circulo(radio):
    area = VAlOR_PI * (radio**2)
    return area

print("El área de circulo es: ")
print(round(calcular_radio_circulo(radio_circulo),2))

# Funcion para hallar el volumen de un cilindro
def calcular_volumen_cilindro(radio,altura):
    volumen = VAlOR_PI * (radio**2) * altura
    return volumen

print("El volumen del cilindro es: ")
print(round(calcular_volumen_cilindro(radio_cilindro,altura_cilindro),2))


