from abc import ABC, abstractmethod
import Sensores
import Atuadores

class ComponentesEletromecanicos(ABC):
    
    def __init__(self, grandeza, funcao, estado):
        self.grandeza = grandeza
        self.funcao = funcao
        self.estado = estado

    @abstractmethod
    def get_grandeza(self):
        pass

    @abstractmethod
    def set_grandeza(self, grandeza):
        pass

    @abstractmethod
    def get_funcao(self):
        pass

    @abstractmethod
    def set_funcao(self, funcao):
        pass

    @abstractmethod
    def get_estado(self):
        pass

    @abstractmethod
    def set_estado(self, estado):
        pass

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Sensores(ComponentesEletromecanicos):
    
    def __init__(self, valorLido, valorMaximo):
        super().__init__()
        self.valorLido = valorLido
        self.valorMaximo = valorMaximo

    def set_valorLido(self):
        pass

    def get_valorLido(self,valorLido):
        pass

    def set_valorMaximo(self):
        pass

    def get_valorMaximo(self,valorMaximo):
        pass

    def set_funcao(self,funcao):
        self.funcao = 'medir'

    def get_funcao(self):
        return self.funcao

class Atuadores(ComponentesEletromecanicos):
    
    pass
