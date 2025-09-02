def run():
    
    anio = int(input("Ingrese año a evaluar: "))

    def bisiesto(anio):
        if (anio%4 == 0) and (anio%100 != 0 or anio%400 == 0):
            return True
        else:
            return False

    if bisiesto(anio) == True:
        print ("El año ingresado es bisiesto")
    else:
        print ("El año ingresado no es bisiesto")
        

if __name__ == "__main__":
    run()