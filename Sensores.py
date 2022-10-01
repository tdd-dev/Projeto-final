from ComponentesEletromecanicos import Sensores

class SensorTemperatura(Sensores):
    def __init__(self):
        super().__init__()

    def set_grandeza(self, grandeza):
        self.grandeza = grandeza
    def get_grandeza(self):
        return self.grandeza

    def set_valorLido(self,valorLido):
        self.valorLido = valorLido
    def get_valorLido(self):
        return self.valorLido

    def set_estado(self,estado):
        self.estado = estado
    def get_estado(self):
        return self.estado

    def ligar(self):
        self.set_estado('Sensor de temperatura ligado')
    def desligar(self):
        self.set_estado('Sensor de temperatura desligado')

    def medir(self):
        if(self.get_valorLido().isdigit() != True):
            print('Valor invalido')
        elif(int(self.get_valorLido()) < 0):
            print('Valor invalido')
        elif(int(self.get_valorLido()) > 100):
            print('Valor invalido')
        elif(' ' in self.get_valorLido()):
            print('Valor invalido')
        elif(self.get_grandeza() != 'C'):
            print('Valor invalido')
        else:
            return self.get_valorLido() + self.get_grandeza()
        
        

class SensorPressao(Sensores):

    def __init__(self):
        super().__init__()

    def set_grandeza(self, grandeza):
        self.grandeza = grandeza
    def get_grandeza(self):
        return self.grandeza

    def set_estado(self,estado):
        self.estado = estado
    def get_estado(self):
        return self.estado

    def ligar(self):
        self.set_estado('Sensor de pressão ligado')
    def desligar(self):
        self.set_estado('Sensor de pressão desligado')

    def medir(self):
        if(self.get_valorLido().isdigit() != True):
            print('Valor invalido')
        elif(int(self.get_valorLido()) < 0):
            print('Valor invalido')
        elif(int(self.get_valorLido()) > 100):
            print('Valor invalido')
        elif(' ' in self.get_valorLido()):
            print('Valor invalido')
        elif(self.get_grandeza() != 'Pa'):
            print('Valor invalido')
        else:
            return self.get_valorLido() + self.get_grandeza()