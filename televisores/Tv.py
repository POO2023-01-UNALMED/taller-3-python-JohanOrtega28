from mimetypes import init

class TV:
    numTV = 0
    def __init__(self,marca,estado) -> None:
        self.__marca = marca
        self.__estado = estado
        self.__volumen = 1
        self.__canal = 1
        self.__precio = 500
        TV.numTV+=1

    def setMarca(self,marca):
        self.__marca = marca
    def getMarca(self):
        return self.__marca
    def setControl(self,control):
        self.__control = control
    def getControl(self):
        return self.__control
    def setPrecio(self,precio):
        self.__precio = precio
    def getPrecio(self):
        return self.__precio
    def setVolumen(self,volumen):
        self.__volumen = volumen if volumen>=1 and volumen<=7 and self.__estado==True else self.__volumen
    def getVolumen(self):
        return self.__volumen
    def setCanal(self,canal):
        self.__canal = canal if canal>=1 and canal<=128 and self.__estado==True else self.__canal
    def getCanal(self):
        return self.__canal
    def getEstado(self):
        return self.__estado
    

    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def canalUp(self):
        self.__canal += 1 if self.__canal<120 and self.__estado==True else 0

    def canalDown(self):
        self.__canal -= 1 if self.__canal>1 and self.__estado==True else 0

    def columenUp(self):
        self.__volumen += 1 if self.__volumen<7 and self.__estado==True else 0

    def volumenDown(self):
        self.__volumen -= 1 if self.__volumen>1 and self.__estado==True else 0


    @classmethod
    def setNumTV(ops,numTV):
        ops.numTV = numTV
    @classmethod
    def getNumTV(ops):
        return ops.numTV