class ViajeroFrecuente:
    __numero = ''
    __DNI = ''
    __nombre = ''
    __apellido = ''
    __cantmillas = ''
    def __init__(self,num='',docu='',nom='',ape='',cant=''):
        self.__numero = num
        self.__DNI = docu
        self.__nombre = nom
        self.__apellido = ape
        self.__cantmillas = cant
    def __str__(self):
        return 'Numero: {}, DNI: {}, Nombre: {}, Apellido: {}, Cantidad de millas: {}'.format(self.__numero,self.__DNI,self.__nombre,self.__apellido,self.__cantmillas)
    def GetNro(self):
        return self.__numero
    def cantidadTotaldeMillas(self,):
        return self.__cantmillas
    def acumularMillas(self,ultMilla):
        self.__cantmillas += ultMilla
    def canjearMillas(self,canjear):
        if canjear <= self.__cantmillas:
            print("Es posible canjear las millas ingresadas")
            self.__cantmillas -= canjear
            print("Millas restantes: ",self.__cantmillas)
        else:
            print("ERROR en la operacion")
