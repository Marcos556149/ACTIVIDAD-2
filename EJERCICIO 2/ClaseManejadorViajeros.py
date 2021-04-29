import csv
from ClaseViajero import ViajeroFrecuente
class ManejadorViajero:
    __listaViajeros = []
    def __init__(self):
        self.__listaViajeros = []
    def test(self):
        testNumero= 250
        testDni= 43642189
        testNombre= 'Marcos'
        testApellido= 'Cornejos'
        testCantidadDeMillas= 15000
        testViajero=ViajeroFrecuente(testNumero,testDni,testNombre,testApellido,testCantidadDeMillas)
        print("TEST REALIZADO CON EXITO")
    def mostrarLista(self):
        for ViajeroFrecuente in self.__listaViajeros:
            print(ViajeroFrecuente)
    def buscarViajero(self,NUMRO):
        for indice, ViajeroFrecuente in enumerate(self.__listaViajeros):
            if ViajeroFrecuente.GetNro() == NUMRO:
                return indice
    def leerArchivo(self):
        archivo = open('Viajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            num = int(fila[0])
            docu = fila[1]
            nom = fila[2]
            ape = fila[3]
            cant = int(fila[4])
            viajero = ViajeroFrecuente(num,docu,nom,ape,cant)
            self.__listaViajeros.append(viajero)
        archivo.close()
    def getMillas(self,indice):
        return self.__listaViajeros[indice].cantidadTotaldeMillas()
    def acumuMillas(self,indice,ultMilla):
        self.__listaViajeros[indice].acumularMillas(ultMilla)
        return self.__listaViajeros[indice].cantidadTotaldeMillas()
    def canjeMillas(self,indice,canjMillas):
        self.__listaViajeros[indice].canjearMillas(canjMillas)




