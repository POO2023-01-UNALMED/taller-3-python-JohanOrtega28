from mimetypes import init

class Control:

    def setTv(self,tv):
        self.__tv = tv
    def getTv(self):
        return self.__tv
    
    def enlazar(self,tv):
        self.__tv = tv
        self.__tv.setControl(self)
    def turnOn(self):
        self.__tv.turnOn()
    def turnOff(self):
        self.__tv.turnOff()
    def canalUp(self):
        self.__tv.canalUp()
    def canalDown(self):
        self.__tv.canalDown()
    def volumenUp(self):
        self.__tv.volumenUp()
    def volumenDown(self):
        self.__tv.volumenDown()
    def setCanal(self,canal):
        self.__tv.setCanal(canal)