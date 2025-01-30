import os
estudiantes=[] # type: ignore
activo = True
accion=0
print("bienvenido a la lista de estudiantes\n")
os.system("pause")
while activo is True:
    os.system('cls')
    print( f'acontinucacion se le muestra la lista actual de estudiantes :\n {estudiantes}')
    try:
        accion=int(input("ingrese el numero de la accion que desea realizar:\n1.agregar estudianten\n2.editar estudiante\n3.eliminar estudiante\n4.buscar estudiante\n5.salir\n:"))
    except ValueError:
        print('ingrese numero valido :')
    else:
        match accion :
            case 1:
                os.system('cls')
                while True:
                    accion_1=input('ingrese el nombre de el estudiante que desea añadir\n:')
                    if accion_1.isalpha():
                        estudiantes.append(accion_1)
                        print(f'la lista de estudiantes es {estudiantes}')
                        os.system('pause')
                        break
                    else:
                        print("el nombre no pude contener digitos numericos")
                        os.system('pause')
                
            case 5:
                activo= False
            case _al:
                os.system('cls')
                print('por favor digite un numero valido')
                os.system('pause')