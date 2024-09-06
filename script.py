usuarios = {}
flag = True

def mostrar_menu():
    print('*****MENU*****\n 1. Agregar usuario y contraseña. \n 2. Mostrar lista de usuarios. \n 3. Ingresar. \n 4. Salir.')

def agregar_usuario():
    llave = input('Ingrese un usuario: ')
    valor = input('Ingrese una contraseña: ')
    print(f'\nEl usuario "{llave}" se agrego correctaomente!')
    usuarios[llave] = valor

def mostrar_usario():
    print('\nEstos son los nombres de los usuarios registrados:')
    index = 0
    for i in usuarios:
        index += 1
        print(f'{index}. {i}')

def loguear():
        usuario = input('Ingrese su usuario: ')
        if usuario in usuarios:
            contraseña = input('Ingrese la contraseña: ')
            if usuarios[usuario] == contraseña:
                print('\nIngreso exitoso.')
            else:
                print(' ')
                print('Contraseña incorrecta.')
        else:
            print(' ')
            print('Usuario incorrecto.')

def salir():
    print('Saliste')
    global flag
    flag = False
    
def error(opcion_elegida):
    print(f'"{opcion_elegida}" No es una opcion correcta.')
           
while flag:
    mostrar_menu()
    opcion_elegida = input('Seleccione una opcion: ')
    if opcion_elegida == '1':
        agregar_usuario()
        print(' ')
    elif opcion_elegida == '2':
        mostrar_usario()
        print(' ')
    elif opcion_elegida == '3':
        loguear()
        print(' ')
    elif opcion_elegida == '4':
        salir()
    else:
        error(opcion_elegida)
        print(' ')