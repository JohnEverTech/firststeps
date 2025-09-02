import random


def run():
    num_aleatorio = random.randint(1,100)
    num_elegido =int(input("Elige un numero del 1 al 100: " ))
    cont = 0
    while num_elegido != num_aleatorio:
        if num_elegido > num_aleatorio:
            print("Elige un numero mas pequeño")
        else:
            print("Elige un numero mas grande")
        num_elegido = int(input ("Elige otro numero: "))
        cont +=1
    print(f"¡Ganaste!, Te tomó {cont} intentos")

if __name__ == "__main__":
    run()

                 