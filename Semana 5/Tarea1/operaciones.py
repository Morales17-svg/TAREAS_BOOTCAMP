def ingresar_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point <= 0 or point > 5:  # Verifica si es menor que 0 o mayor que 5
                print('Por favor, introduzca un valor entre 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:  # Utilizando with para manejar el archivo
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def mostrar_resultados():
    print('Resultados hasta la fecha:')
    with open("data.txt", "r") as read_file:  # Utilizando with para manejar el archivo
        print(read_file.read())

def finalizar_proceso():
    print('Finalizando el proceso.')

