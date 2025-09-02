#importando la libreria random para obtener valores aleatorios
import random


def run():

    #Separador estético
    def separador():
        print("*" * 80)

 
    #Confirmacion de intentos limitado a 10. Y manejando la excepcion de q no se un número y esté en el rango 1 -10
    def confirm():
        while True:
            try:
                attempts = int(input("Hola, ¿Cuántas veces desea jugar a YanKenPo? (un máximo de 10 veces): "))
                if 1 <= attempts <= 10:
                    return attempts
                else:
                    print("\nPor favor, ingresa un número entre 1 y 10.\n")
                    separador()
            except ValueError:
                print("\nError: Por favor, ingresa un número válido (desde 1, hasta un máximo de 10).\n")
                separador()

    #Guardo el valor q retorna la confirmación de intentos
    intentos = confirm()

    #Mensaje de confirmación
    print(f"\nUsted jugará {intentos} veces ¡Buena suerte!\n")
    separador()

    #Contadores score
    score_user = 0
    score_cpu = 0
    draw = 0

    #Bucle de encuentros a realizarse/Lógica de juego
    for i in range(1, intentos+1):
        #Obteniendo opcion de jugador
        def valueuser():
            while True:
                try:
                    print(f"RONDA NÚMERO {i}\n")
                    useroption = int(input("Eliga su opción: \n Opción 1 para elegir 'Piedra'.\n Opción 2 para elegir 'Papel'.\n Opción 3 para elegir 'Tijera'.\n Opción 0 para terminar de jugar y salir.\n Eliga su opción: "))
                    if 0<= useroption <=3:
                        return useroption
                    else:
                        print("\nPor favor eliga una de las opciones dadas. 1,2 ó 3")
                        separador()
                except ValueError:
                        print("\nPor favor ingrese un valor numérico válido, 1,2 ó 3")
                        separador()

        #Guardo el valor q retorna la opción del usuario
        userchoice = valueuser()

        #Obteniendo opcion de la CPU
        def valuecpu():
            cpuoption= random.randint(1,3)
            return cpuoption
        
        #Guardo el valor de la opcion de la CPU
        cpuchoice = valuecpu()

        #Finalizando el programa
        if userchoice == 0:
            separador()
            print("\nUsted decidió dejar de jugar. Gracias por participar.")
            print("Aún asi, se mostrarán los resultados registrados hasta que decidió dejar de jugar.\n")
            separador()
            break

    #Lógica de juego
        #Casos donde el usuario gana
        if userchoice == 1 and cpuchoice == 3:
            print("\nUsted eligió piedra y la CPU eligió tijera.")
            print("Usted ganó, piedra le gana a tijera.\n")
            separador()
            score_user +=1
        elif userchoice == 2 and cpuchoice == 1:
            print("\nUsted eligió papel y la CPU eligió piedra.")
            print("Usted ganó, papel le gana a piedra.\n")
            separador()
            score_user +=1
        elif userchoice == 3 and cpuchoice == 2:
            print("\nUsted eligió tijera y la CPU eligió papel.")
            print("Usted ganó, tijera le gana a papel.\n")
            separador()
            score_user +=1
        #Casos donde el usuario pierde
        elif userchoice == 1 and cpuchoice == 2:
            print("\nUsted eligió piedra y la CPU eligió papel.")
            print("Usted perdió, papel le gana a piedra.\n")
            separador()
            score_cpu +=1
        elif userchoice == 2 and cpuchoice == 3:
            print("\nUsted eligió papel y la CPU eligió tijera.")
            print("Usted perdió, tijera le gana a papel.\n")
            separador()
            score_cpu +=1
        elif userchoice == 3 and cpuchoice == 1:
            print("\nUsted eligió tijera y la CPU eligió piedra.")
            print("Usted perdió, piedra le gana a tijera.\n")
            separador()
            score_cpu +=1
        #Casos donde se empata
        elif userchoice == 1 and cpuchoice ==1:
            print("\nAmbos jugadores eligieron piedra, ha sido un empate.\n")
            separador()
            draw +=1
        elif userchoice == 2 and cpuchoice ==2:
            print("\nAmbos jugadores eligieron papel, ha sido un empate.\n")
            separador()
            draw +=1
        elif userchoice == 3 and cpuchoice ==3:
            print("\nAmbos jugadores eligieron tijera, ha sido un empate.\n")
            separador()
            draw +=1

    #Mostrando los resultados
    print(f"\nUsted ha ganado : {score_user} veces")
    print(f"La CPU ha ganado : {score_cpu} veces")
    print(f"Usted y la CPU han empatado un total de: {draw} veces\n")
    separador()

    #Evaluando quién ganó 
    def count_general():
        if score_user > score_cpu:
            mensaje = "\nUsted ha ganado en el conteo general ¡Felicidades!"
        elif score_cpu > score_user:
            mensaje = "\nUsted ha perdido en el conteo general ¡Suerte para la próxima vez!"
        else:
            mensaje = "\nUsted y la CPU empataron en el conteo general. ¡Buen intento!"
        return mensaje
    #Guardando resultado final
    score_general = count_general()

    #Mostrando el resultado final
    print(score_general+"\n")
    separador()
    
if __name__ == "__main__":
    run ()