#import ComponentesEletromecanicos
from ComponentesEletromecanicos import Sensores, ComponentesEletromecanicos

# import ComponentesEletromecanicos as rootClass
# class Test(object):
#
#     def test(self):
#
#         assert rootClass.get_funcao() == 'medir'
a = Sensores(10.0, 10.0)
#b = ComponentesEletromecanicos("df", "gh", "Gh")

a.set_funcao('atuar')
print(a.get_funcao())
#print(b.get_grandeza())