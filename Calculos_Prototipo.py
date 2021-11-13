'''
Projeto - Valquiria
Grupo - Desempenho
'''

##############################################################################
#                                     Ideia                                  #
'''
 Aqui ficaram todos os cálculos necessários para o projeto.
'''
#                                                                            #
##############################################################################

##############################################################################
#                                  Bibliotecas                               #
#                                                                            #
import numpy as np                                                           
import ambiance as am 
#                                                                            #
##############################################################################

##############################################################################
##                                 Cálculos                                 ##

def Calculos (Tipo_asa,
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
              Carga_paga_referencia):
    
##############################################################################
#                                  Conversão                                 #
#                                                                            #
# Convertendo de rpm para rad/s
    Conversao_1 = 0.10472 
#                                                                            #
##############################################################################

##############################################################################
    # Cálculos a serem implementados
    
#--------------------------------------------------------- 4° parte

    # Ideia de gráfico - Word
    # Coeficiente_sustentacao/Coeficiente_arrasto X angulo_ataque
    # Coeficiente_momento X angulo_ataque
    
#--------------------------------------------------------- 5° parte
    # Fonte: Aula_07 no drive. Exemplo de gráfico em 4:20
    # Calculo de coeficiente angular da curva do coeficiente de sustentação x ângulo de ataque
    # Coeficiente_angular_0 = (Coeficiente_sustentacao(um ponto) - Coeficiente_sustentacao (um outro ponto)) / (angulo_ataque (um ponto) - angulo_ataque (um ponto))
    
    # Fonte: Aula_07 no drive. Exemplo de conta 6:05.
    # Calculo de Coeficiente angular do momento 
    # Momento_0 = (Coeficiente_momento (um ponto) - Coeficiente_momento (um ponto)) / (angulo_ataque (um ponto) - angulo_ataque (um ponto))
    
#--------------------------------------------------------- 6° parte
    # Fonte: Aula_07. exemplo 14:00
    # Calculo de distância do centro aerodinâmico.
    # Coeficiente_aerodinamico = (-Momento_0/Coeficiente_angular_0)
       
##############################################################################
#                                 Cálculos                                   #
#                                                                            #
# Asa -----------------------------------------------------------------------#
#                                                                            #

    # Definindo o peso da aeronave - Newton.
    Peso_aeronave = (Peso_asa + Peso_fuselagem + Peso_boom + Peso_trem_pouso_diantero + Peso_trem_pouso_traseiro + Peso_motor + Carga_paga) * 9.81
    
    # Definindo a distância X peso - Quilograma * Metro.
    Asa_kd = Peso_asa * Asa_referencia
    
    # Definindo a distância X peso - Quilograma * Metro.
    Fuselagem_kd = Peso_fuselagem * Fuselagem_referencia
    
    # Definindo a distância X peso - Quilograma * Metro.    
    Boom_kd = Peso_boom * Boom_referencia

    # Definindo a distância X peso - Quilograma * Metro.    
    Trem_pouso_diantero_kd = Peso_trem_pouso_diantero * Trem_pouso_diantero_referencia

    # Definindo a distância X peso - Quilograma * Metro.    
    Trem_pouso_traseiro_kd = Peso_trem_pouso_traseiro * Trem_pouso_traseiro_referencia

    # Definindo a distância X peso - Quilograma * Metro.    
    Motor_kd = Peso_motor * Motor_referencia
    
    # Definindo a distância X peso - Quilograma * Metro.    
    Carga_paga_kd = Carga_paga * Carga_paga_referencia
    
    # Definindo o total de quilograma X metro - Quilograma * Metro.
    Total_kd = Asa_kd + Fuselagem_kd + Boom_kd + Trem_pouso_diantero_kd + Trem_pouso_traseiro_kd + Motor_kd + Carga_paga_kd
    
    # Definindo o total de peso - Quilograma.
    Total_peso = Peso_asa + Peso_fuselagem + Peso_boom + Peso_trem_pouso_diantero + Peso_trem_pouso_traseiro + Peso_motor + Carga_paga
    
    # Definindo o centro de gravidade da aeronave.
    
    Centro_gravidade = Total_kd / Total_peso
    
    Xcg = (Centro_gravidade - 0.3) / Corda
    
    # Definindo o CG.
    
    if (Tipo_asa == 1):
        
        # Fonte: Aula_04 do drive.
        # Cálculo de área para uma asa retangular - Metro^2.
        Area_asa = Envergadura * Corda
        
        # Fonte: Aula_07. exemplo 18:00
        # Calculo de alongamento (AR) - Adimensional.
        Alongamento = (Envergadura / Corda)
        
        # Fonte: Aula_07 19:40
        # Cálculo de afilamento da asa - Adimensional.
        Afilamento = (Corda_ponta / Corda_raiz)
        
        # Fonte: Aula_07 20:40
        # Cálculo de corda média - Metro.
        Corda_media = (2 / 3) * Corda_raiz * ((1 + Afilamento + Afilamento**2) / (1 + Afilamento))
        
        # Fonte: Aula_07 20:40
        # Cálculo de posição da corda média ao longo da envergadura da asa - Metro.
        Posicao_corda_media = (Envergadura / 6) * ((1 + (2 * Afilamento))/(1 + Afilamento))
        
        # Fonte: fundamental of Aircraft
        # Cálculo de área molhada da asa.
        Area_molhada_asa = 2 * Area_asa * (1 + (Espessura_asa / (4 * (1 + Lambda ))) * (1 + Lambda * (Espessura_asa / Espessura_asa))) 
        
    if (Tipo_asa == 2):
        
        # Fonte: Aula_04 do drive.
        # Cálculo de área para uma asa trapezoidal - Metro**2. 
        Area_asa = ((Corda_raiz + Corda_ponta) * Envergadura) / 2
        
        # Fonte: https://aerotoolbox.com/intro-wing-design/
        # Calculo de alongamento.
        Alongamento = (Envergadura**2 / Area_asa)
        
        # Fonte: Aula_07 19:40
        # Cálculo de afilamento da asa.
        Afilamento = (Corda_ponta / Corda_raiz)

        # Fonte: Aula_07 20:40
        # Cálculo de corda média - Metro.
        Corda_media = (2 / 3) * Corda_raiz * ((1 + Afilamento + Afilamento**2) / (1 + Afilamento))
        
        # Fonte: Aula_07 20:40
        # Cálculo de posição da corda média ao longo da envergadura da asa - Metro.
        Posicao_corda_media = (Envergadura / 6) * ((1 + (2 * Afilamento)) / (1 + Afilamento))

        # Fonte: citeseerx
        # Cálculo de área molhada da asa.
        Area_molhada_asa = 2 * Area_asa * (1 + (Espessura_asa / (4 * (1 + Lambda ))) * (1 + Lambda * (Espessura_asa / Espessura_asa)))       
        
    if (Tipo_asa == 3):
        
        # Fonte: Aula_04 do drive.
        # Cálculo de área para uma asa elíptica - Metro**2 .
        Area_asa = (np.pi / 4) * Envergadura * Corda_raiz

        # Fonte: citeseerx
        # Cálculo de área molhada da asa.        
        Area_molhada_asa = 2 * Area_asa * (1 + (Espessura_asa / (4 * (1 + Lambda ))) * (1 + Lambda * (Espessura_asa / Espessura_asa))) 
        
#                                                                            #
# Empenagem -----------------------------------------------------------------#
#                                                                            #
    # Fonte: Aula_04 do drive.
    # Cálculo de volume da cauda Horizontal.
    Vol_cauda_h = (Distancia_h_cga_cgp * Area_empenagem_h) / (Corda * Area_asa)
    
    # Fonte: Aula_04 do drive.
    # Cálculo de volume da cauda Vertical.
    Vol_cauda_v = (Distancia_v_cg_cgl * Area_empenagem_v) / (Envergadura * Area_asa)
    
    # Cálculo de Coeficiente angular (momento)
    Coeficiente_angular_momento = (1 / (36.5 * Area_asa * Corda)) * (Parte_1 + Parte_2 + Parte_3 + Parte_4 + Parte_5 + Parte_6 + Parte_7 + Parte_8)
    
    # Cálculo de Ponto Neutro.
    Ponto_neutro = (Distancia_ca / Corda) - (Coeficiente_angular_momento / Coeficiente_angular) + (((Vol_cauda_v * Eficiencia_empenagem * Coeficiente_angular) / Coeficiente_angular) * 1 - 1.1)
    
    # Cálculo de margem estática.
    Margem_estatica = Ponto_neutro - (Centro_gravidade / Corda)

#                                                                            #
# Fluido --------------------------------------------------------------------#
#                                                                            #
    # Função da biblioteca para obter a densidade do ar conforme a altitude de atuação.
    Atmosfera_cruzeiro = am.Atmosphere(Altitude_cruzeiro)
    Densidade_ar = Atmosfera_cruzeiro.density
    
    # Densidade do ar para a atuação de cruzeiro - Quilograma/Metro**3.
    Densidade_cruzeiro = Densidade_ar[0]
    
    # Função da biblioteca para obter a viscosidade do ar conforme a altitude de atuação.
    Viscosidade_cruzeiro = Atmosfera_cruzeiro.dynamic_viscosity
    
    # Viscosidade do ar para a atuação do cruzeiro - Quilograma/Metro*Segundo
    Viscosidade_cruzeiro = Viscosidade_cruzeiro[0]
    
    # Fonte: Aula_06 do drive.
    # Cálculo de reynolds da asa - Adimensional.
    Reynolds_asa = (Densidade_cruzeiro * Velocidade * Corda) / (Viscosidade_cruzeiro)

#                                                                            #
# Aerodinâmica --------------------------------------------------------------#
#                                                                            #

    # Fonte: Fundamental airship.
    # Cálculo do Coeficiente de fricção da asa - Adimensional.
    Coeficiente_friccao_asa = 0.455 / (np.log10(Reynolds_asa))**2.58
    
    # Fonte: Fundamental airship.
    # Cálculo de fator das aletas - Adimensional.
    Fator_asa = 1 + 1.2 * (Lambda) + 100 * (Lambda)**4
    
    # Fonte: Fundamental Airship.
    # Cálculo de arrasto parasita da asa - Adimensional.
    Arrasto_parasita_asa = (Fator_asa * Coeficiente_friccao_asa * Area_molhada_asa) / Area_asa
    
    # Fonte: Slide de Análise.
    # Cálculo de eficiência da asa - Adimensional.
    Eficiencia_asa = 1 / (1 + Arrasto_parasita_asa)
    
    # Fonte: Slide de Análise
    # Cálculo do Coeficiênte de proporcionalidade - Adimensional
    K = ((1) / (np.pi * Alongamento * Eficiencia_asa))
    
    # Cálculo de Coeficiente de sustentação da asa - Adimensional.
    Coeficiente_sustentacao = (2 * Peso_aeronave) / ( Densidade_cruzeiro * Velocidade**2 * Area_asa)
    
    # Cálculo de Coeficiente de arrasto da asa - Adimensional.
    Coeficiente_arrasto = Arrasto_parasita_asa + K * (Coeficiente_sustentacao**2)
    
    # Fonte: Aula_06 no drive. Exemplo de gráfico no final do vídeo
    # Eficiência aerodinâmica da asa - Adimensional.
    cl_cd = Coeficiente_sustentacao / Coeficiente_arrasto
    
    # Fonte: Aula 07 23:30
    # Cálculo de momento da asa.
    # Momento_asa = ((1/2) * Densidade * velocidade**2 * Area_asa * Corda_media * Coeficiente_momento_asa)
    
    # Calculo de Arrasto - unidade Newton # CERTO
    Arrasto = (1/2)*Densidade_cruzeiro*Velocidade**2*Area_asa*Coeficiente_arrasto
    
    # Calculo de Sustentacao - unidade Newton # CERTO
    Sustentacao = (1/2)*Densidade_cruzeiro*Velocidade**2*Area_asa* Coeficiente_sustentacao
    
#                                                                            #
# Potência ------------------------------------------------------------------#
#                                                                            #
    # Calculo de rotação - unidade RPM
    RPM = Potencia_motor * Alimentacao_motor
    
    # Calculo de ________ - unidade rad/s
    Polar = RPM * Conversao_1
    
    #Pag 38 https://www.ufjf.br/mecanica/files/2016/07/UFJF_2018_TCC_-Leonardo-Morandi-de-Castro-Santos.pdf
    # Calculo da constante empirica da Tracao_requerida - unidade Adimensional
    #Kt0 = 57000 * (1.97-(Passo_helice/Diametro_Helice))
    
    J = Velocidade * 10/ (Polar * Diametro_helice)
    
    Ct = 0.14 - J * 0.175
    
    Cp = 0.07 - J * 0.0625
    
    Nf = (J * Ct) / Cp
    
    #Definir lá na frente
    
    # Calculo de Tracao disponivel [helice] - Newton 
    Tracao_disponivel =  (Potencia_motor_W_S*Nf)/Velocidade

    # Calculo de Potencia disponivel - Watts
    Potencia_disponivel = Tracao_disponivel * Velocidade

    # Calculo de tracao requerida - unidade Newton 
    Tracao_requerida = Sustentacao/(Coeficiente_sustentacao/Coeficiente_arrasto)
    
    # Calculo de Potencia requerida - Watts
    Potencia_requerida = Tracao_requerida * Velocidade
    
#                                                                            #
# Desempenho ----------------------------------------------------------------#
#                                                                            #
    
    # Calculo de Razão de subida - Adimensional
    R_c = (Potencia_disponivel - Potencia_requerida)/Peso_aeronave
     
    # Importante para o cálculo de ângulo (Razão de subida)
    Seno = R_c / Velocidade
    
    # Ângulo de subida - Ângulo.
    Angulo_subida = np.arcsin(Seno) * 57.2958
    
    Cl_max = 1.654
        
    # Calculo de Razão de planeio - Adimensional.
    Cosseno = (Velocidade**2 * Densidade_cruzeiro * Area_asa * Cl_max)/(2 * Sustentacao)
    
    Tgy_min = 1 / (Sustentacao / Arrasto)
    
    R_d = Cosseno * Velocidade * (-1)
    
    Angulo_planeio = (np.arctan(Tgy_min) * (-1)) * 57.29
    
    
    return (Peso_aeronave,
            Centro_gravidade,
            Xcg,
            Area_asa,
            Alongamento,
            Afilamento,
            Corda_media,
            Posicao_corda_media,
            Area_molhada_asa,
            Vol_cauda_h,
            Vol_cauda_v,
            Coeficiente_angular_momento,
            Ponto_neutro,
            Margem_estatica,
            Densidade_cruzeiro,
            Reynolds_asa,
            Coeficiente_friccao_asa,
            Fator_asa,
            Arrasto_parasita_asa,
            Eficiencia_asa,
            K,
            Coeficiente_sustentacao,
            Coeficiente_arrasto,
            cl_cd,
            Arrasto,
            Sustentacao,
            RPM,
            Polar,
            J,
            Nf,
            Tracao_disponivel,
            Potencia_disponivel,
            Tracao_requerida,
            Potencia_requerida,
            Velocidade,
            R_c,
            Angulo_subida,
            R_d,
            Angulo_planeio)
    