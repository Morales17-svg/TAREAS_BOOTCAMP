from operaciones import ingresar_puntuacion, mostrar_resultados, finalizar_proceso

def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                finalizar_proceso()
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

if __name__ == "__main__":
    main()
