from ClaseManejadorViajeros import ManejadorViajero
if __name__=='__main__':
    manejador1 = ManejadorViajero()
    manejador1.leerArchivo()
    manejador1.test()
    manejador1.mostrarLista()
    NUMRO = int(input('\nIngrese numero de viajero: '))
    indice = manejador1.buscarViajero(NUMRO)
    if indice != None:
        while True:
            print("_______MENÚ_______")
            print("[1]...Consultar cantidad de millas")
            print("[2]...Acumular millas")
            print("[3]...Canjear millas")
            print("[0]...Salir")
            print()
            try:
                op = int(input('Selecciona una opcion: '))
                if op in range(4):
                    if op == 1:
                        print("Cantidad de millas: ",manejador1.getMillas(indice))
                    if op == 2:
                        ultMilla = int(input('ingrese cantidad de millas recorridas en el ultimo viaje: '))
                        total = int(manejador1.acumuMillas(indice,ultMilla))
                        print("Millas totales: ",total)
                    if op == 3:
                        canjMillas=int(input('Ingrese cantidad de millas a canjear: '))
                        manejador1.canjeMillas(indice,canjMillas)
                    if op == 0:
                        print("___Menù Finalizado__")
                        break
                        print()
                else:
                    print("Error, solo se aceptan numeros del 0 al 3")
            except ValueError:
                print("Error, ingrese solamente numeros")
    else:
        print("Numero de viajero no encontrado")




