##############################################################################
##           #====================Funcao Excel====================#         ##
##                                                                          ##
## A funcao Excel tem como objetivo armazenar todos os dados do programa.   ##
##                                                                          ##
##############################################################################

##############################################################################
## Aqui sao armazenadas todos os dados.                                     ##
##############################################################################

##############################################################################
## Bibliotecas                                                              ##
import pandas as pd                                                         ##
##############################################################################

def Resultados (Resultado_1):
    
    Lista_DataFrame = []
    
    contador_1 = 0
    while (contador_1 <= (len(Resultado_1)-1)):
        Lista_1_DataFrame = (Resultado_1 [contador_1])
        Lista_DataFrame.append (Lista_1_DataFrame)
        contador_1 = contador_1 + 1
        
    return (Lista_DataFrame)

def Banco_dados (data):
    dados = pd.DataFrame (data ,  columns = ['Peso da aeronave (N)',
                                             'Centro de gravidade ()',
                                             'Xcg ()',
                                             'Area da asa (m^2)',
                                             'Alongamento (ad)',
                                             'Afilamento (ad)',
                                             'Corda media (m)',
                                             'Posicao da corda media (m)',
                                             'Area molhada da asa (m^2)',
                                             'Volume de cauda horizontal ()',
                                             'Volume de cauda vertical ()',
                                             'Coeficiente angular (momento)',
                                             'Ponto neutro ()',
                                             'Margem estática',
                                             'Densidade de cruzeiro ()',
                                             'Reynolds da asa (ad)',
                                             'Coeficiente de friccao da asa (ad)',
                                             'Fator da asa ()',
                                             'Arrasto parasita da asa ()',
                                             'Eficiencia da asa ()',
                                             'K ()',
                                             'Coeficiente de Sustentacao (ad)',
                                             'Coeficiente de Arrasto (ad)',
                                             'Coeficiente de sustentacao X Coeficiente de arrasto (ad)',
                                             'Arrasto (N)',
                                             'Sustentacao (N)',
                                             'RPM ()',
                                             'Polar ()',
                                             'J ()',
                                             'Nf ()',
                                             'Tracao Disponivel (N)',
                                             'Potencia Disponivel (W)',
                                             'Tracao Requerida (N)',
                                             'Potencia Requerida (W)',
                                             'Velocidade (m/s)',
                                             'Razao de subida ()',
                                             'Angulo de Subida ()',
                                             'Razao de planeio ()',
                                             'Angulo de planeio ()'
                                             ])
    
    dados.to_excel ('Resultados_Prototipo.xls')