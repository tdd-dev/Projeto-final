# Hierarquia de classes funcionais dos principais componentes eletrônicos.

1 . Classe raíz: Componentes eletromecanico
2 . Classes derivadas': Sensores e Atuadores 
3 . Classes derivadas": Temperatura, Pressão e Pneumatico, Hidraulico


# Atributos de cada classe:

Classe Componentes_Eletromecanicos:
    1- Grandeza (unidades)
    2- Função (monitorar e agir)
    3- Estado (on/off)

    -> implementa um metodo abstrado (get/set)Grandeza()
    -> implementa um metodo abstrado (get/set)Função()
    -> implementa um metodo abstrado (get/set)Estado()
    
    Classe Sensores:
        1- valorLido
        2- valorMaximo

        -> implementar (get/set)ValorLido()
        -> implementar (get/set)valorMaximo()

        -> metodo medir(getValorLido)
        -> metodo maximo(getValorMaximo)

        Classe Temperatura:

            -> getGrandeza
            -> Implementar um metodo "PadronizarValorLidoTemp(getValorLido)" usando atributo "Grandeza"


        Classe Pressão:
            
        
    Classe Atuadores:
        1- posicao
        2- fluido
    
        Classe Pneumatico:

        Classe Hidraulico:
    


# metodos para as classes

Metodos para atuador:

    1. getPosicao e setPosicao
    2. getFluido e setFluido

Metodos para sensores:

    1. getValorLido e setValorLido
    2. getFaixa_operacional e setFaixa_operacional

Metodos para Componentes


# Polimorfismo


# Casos de teste iniciais

