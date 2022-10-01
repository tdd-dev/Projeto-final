import pytest
from ComponentesEletromecanicos import ComponentesEletromecanicos, Sensores, Atuadores
from Sensores import SensorTemperatura, SensorPressao


class Test(object):

    def test_set_funcao_sensor(self):
        teste_Sensor = Sensores()
        teste_Sensor.set_funcao('medir')
        assert teste_Sensor.get_funcao() == 'medir'

    def test_estado_inicial_construtor(self):
        sensor = Sensores()
        assert sensor.get_estado() == 'Sensor desligado'

    def test_ligar_sensor(self):
        sensor = Sensores()
        sensor.ligar()
        assert sensor.get_estado() == 'Sensor ligado'

    def test_deligar_sensor(self):
        sensor = Sensores()
        sensor.desligar()
        assert sensor.get_estado() == 'Sensor desligado'
    
    def test_estado_sensor_temperatura_ligado(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.ligar()
        assert sensor_temp.get_estado() == 'Sensor de temperatura ligado'

    def test_estado_sensor_temperatura_desligado(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.desligar()
        assert sensor_temp.get_estado() == 'Sensor de temperatura desligado'

    def test_estado_sensor_pressao_ligado(self):
        sensor_pres = SensorPressao()
        sensor_pres.ligar()
        assert sensor_pres.get_estado() == 'Sensor de pressão ligado'

    def test_estado_sensor_pressao_desligado(self):
        sensor_pres = SensorPressao()
        sensor_pres.desligar()
        assert sensor_pres.get_estado() == 'Sensor de pressão desligado'
    
    def test_grandeza_sensor_temp(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('32')
        sensor_temp.set_grandeza('C')
        assert sensor_temp.medir() == '32C'

    def test_grandeza_sensor_pressao(self):
        sensor_pres = SensorPressao()
        sensor_pres.set_valorLido('5')
        sensor_pres.set_grandeza('Pa')
        assert sensor_pres.medir() == '5Pa'
    
    def test_valor_sensor_temperatura_maior_range(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('150')
        sensor_temp.set_grandeza('C')
        assert sensor_temp.medir() == 'ERRO TEMPERATURA MAIOR QUE RANGE'

    def test_valor_sensor_temperatura_com_espaco(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('1 0')
        sensor_temp.set_grandeza('C')
        assert sensor_temp.medir() == 'ERRO TEMPERATURA DEVE SER NUMÉRICA'
    
    def test_grandeza_sensor_temperatura_incorreta(self):
        sensor_temp = SensorTemperatura()
        sensor_temp.set_valorLido('10')
        sensor_temp.set_grandeza('K')
        assert sensor_temp.medir() == 'GRANDEZA DEVE SER EM CELSIUS'
    
    def test_set_funcao_atuador(self):
        atuador = Atuadores()
        atuador.set_funcao('atuar')
        assert atuador.get_funcao() == 'atuar'
    
    def test_estado_atuador(self):
        atuador = Atuadores()
        atuador.ligar()
        assert atuador.get_estado() == 'Atuador ligado'

    def test_construtor_sensor_temperatura():
        sensor_temp = SensorTemperatura(10,10)
        assert sensor_temp.get_valorLido() == 10
        assert sensor_temp.get_valorMaximo() == 10
        



