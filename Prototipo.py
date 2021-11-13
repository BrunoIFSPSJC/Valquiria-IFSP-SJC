'''
Projeto - Valquiria
Grupo - Desempenho
'''

##############################################################################
#                                   Ideia                                    #
'''                                                                      
 Objetivo do programa: O código foi feito para ajudar os integrantes do grupo
Valquiria-IFSP em seus cálculos aeronáuticos e servir como um auxiliador para
análises e resultados.                                                
'''
#                                                                            #                                                                    
##############################################################################

##############################################################################
#                               Bibliotecas                                  #
#                                                                            #
#                                                                            #
import numpy as np                                                                                                                                 
#                                Módulos                                     #
#                                                                            #                        
import Distribuicao_Prototipo                                             
import Excel_Prototipo                                                     
import Grafico_Prototipo                                                    
#                                                                            #                                           
##############################################################################

##############################################################################
#                       Quantidade de análises desejadas                     #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
Quantidade_analises = 99
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
##############################################################################

##############################################################################
#                       Especificações da aeronave                           #
#                                                                            #
'''
Tipo de asa (atribuir algum valor informado para a definição dos cálculos):
1 = Asa retângular
2 = Asa trapezoidal
3 = Asa elíptica
'''
#                                                                            #
Tipo_asa = 1
#                                                                            #
##############################################################################

##############################################################################
#                         Funcionamento do programa                          #
#                                                                            #
#                                                                            #
#                                                                            # 
'''
 A variável voltas é a responsável por exercutar o código (x vezes) seguindo
o valor adotado pelo usuário no começo do código.
'''                           
#                                                                            #
voltas = Quantidade_analises                                                 
#                                                                            #
#                                                                            #
#                                                                            # 
'''                                                                           
 A variavel contador está relacionada ao número de voltas em que o while vai
se repetir para que a condição total de voltas se complete, portanto, após a
primeira volta no final do programa é somada uma unidade ao contador com o in-
tuito de criação de um "range" para a atuação do while.
'''
#                                                                                                                                           
contador = 0
#                                                                            #
#                                                                            #
#                                                                            #                                                                 
'''
 A variável contador_1 é usada para que o programa possa alterar a linha no
Excel onde os dados das analises são armazenados.
'''
#                                                                            #                                                                
contador_1 = 0                                                               
#                                                                            #
#                                                                            #
#                                                                            #
##############################################################################

##############################################################################
#                             Procesamento                                   #
#                                                                            #
while (contador <= voltas):

# Variavel importante para o armazenamento funcionar corretamente.            
    linha_excel = contador_1                                                
                                                                          
    if (contador_1 <= 0):                                                                                                                                        
        contador_1 = contador_1 + 1
#                                                                            #                                         
##############################################################################

##############################################################################
#                              Conversões                                    #
#                                                                            #
# Convertendo polegada para metro.
    Conversao_1 = 39.37
#                                                                            #
#                                                                            #
##############################################################################

##############################################################################
#                        Entrada de variáveis                                #
#                                                                            #
# A ideia desse print é de mostrar ao usuário quantas análises já foram feitas.                                                                            
    print (contador,' - Analise')
#                                                                            #
# Asa -----------------------------------------------------------------------
#                                                                            #
    # Definicição de valores para uso de asa retângular.
    if (Tipo_asa == 1):
        
        # Definindo a envergadura da asa - Metro.
        Envergadura = 1.8
        
        # Definindo a corda da asa - Metro.
        Corda = 0.3
        
        # Definindo a corda da raiz da asa - Metro.
        Corda_raiz = 0.3
        
        # Definindo a corda da ponta da asa - Metro.
        Corda_ponta = 0.3
        
        # Definindo a espessura da asa - Metro.
        Espessura_asa = 0.15
        
        # Proporção entre a raiz e a ponta da cauda (razão de afunilamento) - Adimensional.
        Lambda = 0.15 
        
    # Definição de valores para uso de asa trapezoidal.
    if (Tipo_asa == 2):
        
        # Definindo a enveradura da asa - Metro.
        Envergadura = 1.95
        
        # Definindo a corda da raiz - Metro.
        Corda_raiz = 0.3
        
        # Definindo a corda da ponta - Metro.
        Corda_ponta = 0.2
        
        # Definindo a espessura da asa - Metro.
        Espessura_asa = 0.15
        
        # Definindo o lambda da asa (proporção entre a raiz e a ponta da asa).
        Lambda = 0.15 # Normalmente usado.
        
        # Não será usado.
        Corda = 0
        
    # Definição de valores para uso de asa elíptica.
    if (Tipo_asa == 3):
        
        # Definindo a envergadura da asa - Metro.
        Envergadura = 0
        
        # Definindo a corda da raiz da asa - Metro.
        Corda_Raiz = 0
        
        # Definindo a espessura da asa - Metro.
        Espessura_asa = 0.15
        
        # Definindo o lambda da asa (proporção entre a raiz e a ponta da asa).
        Lambda = 0.15 # Normalmente usado.
        
        
        # Não será usado.
        Corda = 0
        Corda_ponta = 0     
        
#                                                                            #
# Empenagem -----------------------------------------------------------------#
#                                                                            #

    # Definindo a área da empenagem (horizontal) - Metro^2.
    Area_empenagem_h = 1
    
    # Definindo a distância do centro aerodinâmico.
    Distancia_ca = 1
    
    # Definindo o coeficiente angular.
    Coeficiente_angular = 1
    
    # Definindo a distância do centro de gravidade até o centro aerodinâmico.
    Distancia_h_cga_cgp = 1
    
    # Definindo a área da empenagem (vertical) - Metro^2.
    Area_empenagem_v = 1
    
    #Definindo a eficiencia da empenagem.
    Eficiencia_empenagem = 0.8
    
    # Definindo a distância do centro de gravidade até o centro de sustentação.
    Distancia_v_cg_cgl = 1
    
    # Definindo forma (Parte 1).
    Parte_1 = 1.1
    
    # Definindo forma (Parte 2).
    Parte_2 = 1.1
    
    # Definindo forma (Parte 3).
    Parte_3 = 1.1
    
    # Definindo forma (Parte 4).
    Parte_4 = 1.1
    
    # Definindo forma (Parte 5).
    Parte_5 = -0.1
    
    # Definindo forma (Parte 6).
    Parte_6 = -0.1
    
    # Definindo forma (Parte 7).
    Parte_7 = -0.1
    
    # Definindo forma (Parte 8).
    Parte_8 = -0.1
#                                                                            #
# Hélice ------------------------------------------------------------------- #
#                                                                            # 
    # Definindo o diâmetro da hélice - Metro. 
    Diametro_helice = 0.2794
    
    # Definindo a eficiência da hélica - Adimensional.
    Eficiencia_helice = 70
    # Eficiencia_helice = np.random.randint (10,90, size = 1) [0] # Variando.
#                                                                            #
# Bateria ------------------------------------------------------------------ #
#                                                                            #
    # Definindo a alimentação do motor - Volt.
    Alimentacao_motor = 12   
    
    # Potencia do motor - Unidade Watts
    Potencia_motor_W_S = 700
    
    # Definindo a carga total do motor - KiloWatt.
    Potencia_motor = 1090
#                                                                            #
# Atuação ------------------------------------------------------------------ #
#                                                                            # 
    # Definindo a velocidade da aeronave - Metro/Segundo.
    # Velocidade = 11
    Velocidade = np.random.randint (4,30, size = 1) [0]

    # Definindo altitude de atuação da aeronave - Metro.
    Altitude_cruzeiro = 30

    # Definindo o ângulo de ataque - Grau.
    Angulo_ataque = np.random.randint (-10,17, size = 1) [0]
    
    # Definindo o tamanho da pista - Metro.
    Tamanho_pista = 60
#                                                                            #
# Peso --------------------------------------------------------------------- #   
#                                                                            #
    
    # Definindo o peso da asa - Quilograma.
    Peso_asa = 0.875
    
    # Definindo o peso de fuselagem - Quilograma.
    Peso_fuselagem = 0.604
    
    # Definindo o peso do BOOM - Quilograma.
    Peso_boom = 0.112
    
    # Definindo o peso de trem de pouso (dianteiro) - Quilograma.
    Peso_trem_pouso_diantero = 0.238
    
    # Definindo o peso de trem de pouso (traseiro) - Quilograma.
    Peso_trem_pouso_traseiro = 0.1339
    
    # Definindo o peso de motor - Quilograma.
    Peso_motor = 0.175
    
    # Definindo o peso de carga paga - Quilograma.
    Carga_paga = 10

#                                                                            #
# Distância ---------------------------------------------------------------- #
#                                                                            #
    # Definindo a distância da asa até o ponto de referência.
    Asa_referencia = 0.316
    
    # Definindo a distância até o ponto de referência.
    Fuselagem_referencia = 0.377
    
    # Definindo a distância do BOOM até o ponto de referência.
    Boom_referencia = 0.792
    
    # Definindo a distância da empenagem até o ponto de referência.
    Empenagem_referencia = 1.1178
    
    # Definindo a distância do trem de pouso (Dianteiro) até o ponto de referência.
    Trem_pouso_diantero_referencia = 0.0125
    
    # Definindo a distância do trem de pouso (Traseiro) até o ponto de referência.
    Trem_pouso_traseiro_referencia = 0.632
    
    # Definindo a distância do motor até o ponto de referência.
    Motor_referencia = 0.05
    
    # Definindo a distância até o ponto de referência.
    Carga_paga_referencia = 0.38
    
    
#                                                                            #
# Variados ----------------------------------------------------------------- #
#                                                                            #
    # Densidade do ar em terra - Quilograma/Metro**3.
    Densidade_terra = 1.225
#                                                                            #
##############################################################################

##############################################################################
#                           Distribução dos dados                            #
#                                                                            #
    Resultado_Mestre = Distribuicao_Prototipo.mestra (Tipo_asa,
                                                      Envergadura,
                                                      Corda,
                                                      Corda_raiz,
                                                      Corda_ponta,
                                                      Espessura_asa,
                                                      Lambda,
                                                      Area_empenagem_h,
                                                      Distancia_ca,
                                                      Coeficiente_angular,
                                                      Eficiencia_empenagem,
                                                      Distancia_h_cga_cgp,
                                                      Area_empenagem_v,
                                                      Distancia_v_cg_cgl,
                                                      Parte_1,
                                                      Parte_2,
                                                      Parte_3,
                                                      Parte_4,
                                                      Parte_5,
                                                      Parte_6,
                                                      Parte_7,
                                                      Parte_8,
                                                      Diametro_helice,
                                                      Eficiencia_helice,
                                                      Alimentacao_motor,
                                                      Potencia_motor_W_S,
                                                      Potencia_motor,
                                                      Velocidade,
                                                      Altitude_cruzeiro,
                                                      Angulo_ataque,
                                                      Peso_asa,
                                                      Peso_fuselagem,
                                                      Peso_boom,
                                                      Peso_trem_pouso_diantero,
                                                      Peso_trem_pouso_traseiro,
                                                      Peso_motor,
                                                      Carga_paga,
                                                      Asa_referencia,
                                                      Fuselagem_referencia,
                                                      Boom_referencia,
                                                      Empenagem_referencia,
                                                      Trem_pouso_diantero_referencia,
                                                      Trem_pouso_traseiro_referencia,
                                                      Motor_referencia,
                                                      Carga_paga_referencia)
#                                                                            #
##############################################################################

    (Resultado_1) = Resultado_Mestre 
    
##############################################################################
#                          Processo de armazenamento                         #
#                                                                            #
    Excel_Resultados = Excel_Prototipo.Resultados (Resultado_1)
    (Lista_DataFrame) = Excel_Resultados

    if (linha_excel == 0):
        data = [Lista_DataFrame]
        Lista_DataFrame = []

    if (linha_excel == 1) :   
        data_1 = Lista_DataFrame
        Lista_DataFrame = []
        data.append (data_1)
   
    Banco_dados = Excel_Prototipo.Banco_dados (data)
#                                                                            #
##############################################################################

    contador = contador + 1
#                                                                            #
#                               Fim                                          #
##############################################################################

##############################################################################
#                   Plotagem dos gráficos de análise                         #
#                                                                            #
Resultado_Grafico = Grafico_Prototipo.grafico (Quantidade_analises)
#                                                                            #
##############################################################################   


 