import os 
import time 
#listas
equipos=[] 
equipo=[]
jugadores=[]
Jugador=[]
cts=[]
ct=[]
cMds=[]
cMd=[]
estadisticas=[]
#whiles
menu_equipos= True
menu_principal= True
menu_jugador= True
menu_dorsal= True 
menu_edad= True
menu_posicion= True 
menu_agregar= True
edicion_j= True
eliminar_J= True 
#while
#acciones
tiempo=2
accion=0
accion2=0
while menu_principal is True:
    os.system('cls')
    print('____________________________________________________\nbienvenido a la seleccion ded equipos betplay\n____________________________________________________')
    try:
        ingreso=int(input('1.registrar equipo\n2.salir\n:'))
        nombre_equipo=('')
        menu_equipos=True
        match ingreso:
            case 1:
                while menu_equipos is True:
                    nombre_equipo=str(input("escriba el nombre de el equipo   :"))
                    equipo.append(nombre_equipo)
                    os.system('cls')
                    menu_jugador= True
                    menu_dorsal= True 
                    menu_edad= True
                    menu_posicion= True 
                    menu_agregar= True
                    edicion_j= True
                    eliminar_J= True
                    try:
                        os.system('cls')
                        accion=int(input('ingrese el numero de la accion que desea realizar\n1.registrar jugardor\n2.registrar integrante de el cuerpo tecnico\n3.registrar integrante de el cuerpo medico\n4.agregar estadisticas.\n5.regresar a el menu anterior\n:'))
                        match accion:
                            case 1:
                                
                                #jugador
                                while menu_jugador is True:
                                    Jugador=[]
                                    menu_dorsal= True 
                                    menu_edad= True
                                    menu_posicion= True 
                                    menu_agregar= True
                                    edicion_j= True
                                    eliminar_J= True
                                    os.system('cls')
                                    nombre=input("ingrese el nombre de el jugador\n(si desea volver atras digite (b)  )\n:")
                                    if nombre.upper()=='B':
                                        break
                                    elif nombre.isalpha():
                                        Jugador.append(nombre)
                                        print(Jugador)
                                        time.sleep(tiempo)
                                       #dorsal
                                        while menu_dorsal is True:
                                            os.system('cls')
                                            try:
                                                dorsal=int(input(f'escriba el numero de el dorsal de {nombre}.\n si quiere regresar digite (00))\n:'))
                                                if dorsal==00:
                                                    break
                                                elif dorsal.is_integer :
                                                    Jugador.append(dorsal)
                                                    print(Jugador)
                                                    time.sleep(tiempo)
                                                    #edad 
                                                    while menu_edad is True:
                                                        os.system('cls')
                                                        try:
                                                            edad=int(input(f'ingrese la edad de {nombre}.\nsi desea regresar digite (00)\n:'))
                                                            if edad==00:
                                                                break
                                                            elif edad.is_integer:
                                                                Jugador.append(edad)
                                                                print(Jugador)
                                                                time.sleep(tiempo)
                                                                #posicion
                                                                while menu_posicion is True:
                                                                    os.system('cls')
                                                                    try:
                                                                        posicion=str(input(f'escriba la posicion en la que juega {nombre}.\nsi desea regresar digite (b).\n:'))
                                                                        if posicion.upper()=='B':
                                                                            break
                                                                        elif posicion.isalpha():
                                                                            Jugador.append(posicion)
                                                                            print(Jugador)
                                                                            time.sleep(tiempo)
                                                                            #confirmar
                                                                            while menu_agregar is True:
                                                                                os.system('cls')
                                                                                print(f'la informacion de el jugador se encuentra en este orden (nombre/numero/edad/posicion)  {Jugador}.')
                                                                                try:
                                                                                    accion2=int(input(f'1.desea cambiar algun dato?\n2.desea agregar el jugador con su informacion a el equipo  {nombre_equipo}?\npor favor digite el numero de su acción:'))
                                                                                    match accion2:
                                                                                        case 1:
                                                                                            desicion=int(input("1.remplazar\n2.borrar\n3.volver\n:"))
                                                                                            match desicion:
                                                                                                case 1:
                                                                                                    #edicion
                                                                                                    while edicion_j is True:
                                                                                                        os.system('cls')
                                                                                                        try:
                                                                                                            editar=int(input('la palabra que desea remplazar es:\n1.nombre\n2.dorsal\n3.edad\n4.posicion.\nsi desea volver digite (00)\n:'))
                                                                                                            match editar:
                                                                                                                case 00:
                                                                                                                    break
                                                                                                                case 1:
                                                                                                                    remplazo=input('ingrese el nuevo nombre:')
                                                                                                                    Jugador[0]=remplazo
                                                                                                                    break
                                                                                                                case 2:
                                                                                                                    emplazo=input('ingrese el nuevo dorsal:')
                                                                                                                    Jugador[1]=remplazo
                                                                                                                    break
                                                                                                                case 3:
                                                                                                                    emplazo=input('ingrese la nueva edad:')
                                                                                                                    Jugador[2]=remplazo
                                                                                                                    break
                                                                                                                case 4:
                                                                                                                    emplazo=input('ingrese la nueva posicion:')
                                                                                                                    Jugador[3]=remplazo
                                                                                                                    break
                                                                                                        except ValueError:
                                                                                                            print('por favor solo digite el numero de la accion.')
                                                                                                            time.sleep(tiempo)
                                                                                                case 2:
                                                                                                    #elimnar
                                                                                                    while eliminar_J is True:
                                                                                                        os.system('cls')
                                                                                                        try:
                                                                                                            eliminar=int(input(f'ingrese la posicion de el dato que desea borrar de la sigueinte lista {Jugador} partiendo de el primer dato como 0 y en orden ascendente por unidad.\n:'))
                                                                                                            Jugador.remove(Jugador[eliminar])
                                                                                                            time.sleep(tiempo)
                                                                                                            break
                                                                                                        except ValueError:
                                                                                                                os.system('cls')
                                                                                                                print('por favor solo digite el numero de la posicion que desea eliminar.')
                                                                                                                time.sleep(tiempo)
                                                                                        case 2:
                                                                                            equipo.append(Jugador)
                                                                                            print(f'asi esta el equipo {nombre_equipo} {equipo}.')
                                                                                            time.sleep(6)
                                                                                            os.system('cls')
                                                                                            k1=int(input(f'desea agregar otro jugador a el equipo {nombre_equipo}?\n1.si\n2.no\n:'))
                                                                                            match k1:
                                                                                                case 1:
                                                                                                    #menu_jugador= False
                                                                                                    menu_dorsal= False
                                                                                                    menu_edad= False
                                                                                                    menu_posicion= False
                                                                                                    menu_agregar= False
                                                                                                    edicion_j= False
                                                                                                    eliminar_J= False
                                                                                                case 2:
                                                                                                    menu_equipos= False
                                                                                                    menu_jugador= False
                                                                                                    menu_dorsal= False
                                                                                                    menu_edad= False
                                                                                                    menu_posicion= False
                                                                                                    menu_agregar= False
                                                                                                    edicion_j= False
                                                                                                    eliminar_J= False
                                                                                                    equipos.append(equipo)
                                                                                except ValueError:
                                                                                    print('por favor solo digite el numero de la accion.')
                                                                                    time.sleep(tiempo)
                                                                        else:
                                                                            print('la posicion no puede tener valor numerico.')
                                                                    except ValueError:
                                                                        print('la posicion no puede tener valor numerico')
                                                                        time.sleep(tiempo)
                                                            else:
                                                                print('no se que digito, pero le quedo mal.')
                                                                time.sleep(tiempo)
                                                        except ValueError:
                                                            print('la edad solo puede poseer caracteres numericos.')
                                                            time.sleep(tiempo)
                                            except ValueError:
                                                print("el numero de el dorsal solo puede ser numerico.")
                                                time.sleep(tiempo)
                                    else:
                                        print('el nombre no puede contener caracteres numericos')
                                        time.sleep(tiempo)
                            case 2:
                                #cuerpo tecnico

                                pass
                            case 3:
                                #cuerpo medico
                                pass
                            case 4:
                                #estadisticas
                                pass
                            case 5:
                                break
                    except ValueError:
                        print('por favor digite el valor numerico de la accion')
                        time.sleep(tiempo)
            case 2:
                print(f'equipos registrados: {equipos}')
                time.sleep(6)
                menu_principal=False
    except ValueError:
        print('por favor digite valor numerico de la eleccion')
        time.sleep(tiempo)