import pytest
import ComponentesEletromecanicos as rootClass
class Test(object):
    
    def test(self):
        
        assert rootClass.get_funcao() == 'medir'
