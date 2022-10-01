
from regex import P
from ComponentesEletromecanicos import ComponentesEletromecanicos, Sensores, Atuadores
from Sensores import Temperatura, Pressao

class Test(object):

    # def test_classe_abstrata(self):
    #     ComponentesEletromecanicos.set_funcao('agir')
    #     #print(teste_Sensor.get_funcao())
    #     assert ComponentesEletromecanicos.get_funcao() == 'agir'

    def test_set_funcao_sensor(self):
        teste_Sensor = Sensores()
        teste_Sensor.set_funcao('medir')
        #print(teste_Sensor.get_funcao())
        assert teste_Sensor.get_funcao() == 'medir'

    def test_estado_sensor (self):
        sensor = Sensores()
        sensor.ligar()
        assert sensor.get_estado() == 'sensor ligado'
    
    def test_estado_sensor_temperatura(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.ligar()
        assert sensor_temp.get_estado() == 'sensor de temperatura ligado'

    def test_estado_sensor_pressao(self):
        sensor_pres = SensorPressao()
        sensor_pres.ligar()
        assert sensor_pres.get_estado() == 'sensor de pressão ligado'
    
    def test_grandeza_sensor_temp(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('32')
        sensor_temp.set_grandeza('C')
        assert sensor_temp.medir() == '32 C'

    def test_grandeza_sensor_pressao(self):
        sensor_pres = SensorPressao()
        sensor_pres.set_valorLido('5')
        sensor_pres.set_grandeza('mmHg')
        assert sensor_pres.medir() == '5 mmHg'
    
    def test_funcao_atuador(self):
        atuador = Atuadores()
        atuador.set_funcao('atuar')
        assert atuador.get_funcao() == 'atuar'
    
    def test_estado_atuador(self):
        atuador = Atuadores()
        atuador.ligar()
        assert atuador.get_estado() == 'atuador ligado'

    def test_construtor_sensor_temperatura():
        sensor_temp = SensorTemperatura(10,10)
        assert sensor_temp.get_valor_lido() == 10
        assert sensor_temp.get_valor_maximo() == 10
        



