from abc import ABC, abstractmethod

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

    def __init__(self, *args):
        super().__init__('','medir','Sensor desligado')
        if len(args) == 2:
            self.valorLido = args[0]
            self.valorMaximo = args[1]
        
        
    def set_valorLido(self, valorLido):
        self.valorLido = valorLido
    def get_valorLido(self):
        return self.valorLido

    def set_valorMaximo(self, valorMaximo):
        self.valorMaximo = valorMaximo
    def get_valorMaximo(self):
        return self.valorMaximo

    def set_funcao(self,funcao):
        self.funcao = funcao
    def get_funcao(self):
        return self.funcao

    def set_estado(self,estado):
        self.estado = estado
    def ligar(self):
        self.set_estado('Sensor ligado')
    def desligar(self):
        self.set_estado('Sensor desligado')
    def get_estado(self):
        return self.estado

class Atuadores(ComponentesEletromecanicos):
    def __init__(self, posicao, atuador):
        super().__init__('', 'atuar', 'Atuador deligado')
        self.posicao = posicao
        self.atuador = atuador

    def __init__(self):
        super().__init__('', 'atuar', 'Atuador deligado')

    def get_posicao(self):
        return self.posicao

    def set_posicao(self, posicao):
        self.posicao = posicao

    def get_atuador(self):
        return self.atuador

    def set_atuador(self, atuador):
        self.atuador = atuador

    def set_estado(self, estado):
        self.estado = estado

    def ligar(self):
        self.set_estado('Atuador ligado')

    def desligar(self):
        self.set_estado('Atuador desligado')

    def avancar(self):
        self.set_posicao('Fim do atuador')

    def recuar(self):
        self.set_estado('Inicio do Atuador')