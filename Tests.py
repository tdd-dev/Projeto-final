
from ComponentesEletromecanicos import ComponentesEletromecanicos, Sensores, Atuadores

class Test(object):

    # def test_classe_abstrata(self):
    #     ComponentesEletromecanicos.set_funcao('agir')
    #     #print(teste_Sensor.get_funcao())
    #     assert ComponentesEletromecanicos.get_funcao() == 'agir'

    def test_funcao_sensor(self):
        teste_Sensor = Sensores()
        teste_Sensor.set_funcao('medir')
        #print(teste_Sensor.get_funcao())
        assert teste_Sensor.get_funcao() == 'medir'

    def test_estado(self):
        sensor = Sensores()
        sensor.ligar()
        assert sensor.get_estado() == 'sensor Ligado'

