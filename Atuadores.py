from ComponentesEletromecanicos import Atuadores


class AtuadorPneumatico(Atuadores):
    def __init__(self):
        super().__init__('Inicio do pistão pneumático', 'Ar')
    def ligar(self):
        self.set_estado('Pistão pneumático ligado')

    def desligar(self):
        self.set_estado('Pistão pneumático desligado')

    def avancar(self):
        self.set_posicao('Fim do pistão pneumático')

    def recuar(self):
        self.set_estado('Inicio do pistão pneumático')

class AtuadorHidraulico:
    def __init__(self):
        super().__init__('Inicio da prensa hidráulica', 'óleo')

    def ligar(self):
        self.set_estado('Prensa hidráulica ligada')

    def desligar(self):
        self.set_estado('Prensa hidráulica desligada')

    def avancar(self):
        self.set_posicao('Fim da prensa hidráulica')

    def recuar(self):
        self.set_estado('Inicio do pistão pneumático')
