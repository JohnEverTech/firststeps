import random


def generar_contrasena():
    list_mayus = ["A","B","C","D","E","F","G"]
    list_minus = ["a","b","c","d","e","f","g"]
    list_caracter = ["#","+","*","$","%","&"]
    list_numeros = ["1","2","3","4","5","6","7","8","9","0"]

    list_total = list_mayus + list_minus + list_caracter + list_numeros
    contrasena =[]

    for i in range(10):
        contrasena_random =random.choice(list_total)
        contrasena.append(contrasena_random)


    contrasena = "".join(contrasena)
    return(contrasena)
    

def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == "__main__":
    run() 