from ComponentesEletromecanicos import Sensores

class SensorTemperatura(Sensores):
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

    def ligar(self,estado):
        self.set_estado('Sensor de temperatura ligado')
    def desligar(self,estado):
        self.set_estado('Sensor de temperatura desligado')

    def medir(self):
        self.get_grandeza
        

class SensorPressao(Sensores):
    pass