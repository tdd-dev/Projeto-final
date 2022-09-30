from abc import ABC, abstractmethod
import Sensores
import Atuadores

class ComponentesEletromecanicos(ABC):
    
    def __init__(self, grandeza, funcao, estado):
        self.grandeza = grandeza
        self.funcao = funcao
        self.estado = estado

    def get_grandeza(self):
        pass

    def set_grandeza(self, grandeza):
        pass

    def get_funcao(self):
        pass

    def set_funcao(self, funcao):
        pass

    def get_estado(self):
        pass

    def set_estado(self, estado):
        pass

    def ligar(self):
        pass

    def desligar(self):
        pass

class Sensores(ComponentesEletromecanicos):

    def __init__(self, valorLido, valorMaximo):
        #super().__init__()
        self.valorLido = valorLido
        self.valorMaximo = valorMaximo
        self.funcao = 'medir'

    def set_valorLido(self):
        pass

    def get_valorLido(self,valorLido):
        pass

    def set_valorMaximo(self):
        pass

    def get_valorMaximo(self,valorMaximo):
        pass

    def set_funcao(self,funcao):
        self.funcao = funcao

    def get_funcao(self):
        return self.funcao

class Atuadores(ComponentesEletromecanicos):


    pass
