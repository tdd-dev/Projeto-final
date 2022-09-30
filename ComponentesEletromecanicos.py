from abc import ABC, abstractmethod

class ComponentesEletromecanicos(ABC):
    grandeza: str
    funcao: str
    estado: str

    @abstractmethod
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