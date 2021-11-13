'''
Projeto - Valquiria
Grupo - Desempenho
'''

##############################################################################
#                                    Ideia                                   #
'''
 Aqui será um distribuidor de variáveis.                                    
'''
#                                                                            #
##############################################################################

##############################################################################
#                                   Funcões                                  #
#                                                                            #
import Calculos_Prototipo
#                                                                            #
##############################################################################

##############################################################################
#                                  Distribuição                              #

def mestra (Tipo_asa,
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
    
    Resultado_1 = Calculos_Prototipo.Calculos (Tipo_asa,
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
    
    (Peso_aeronave,
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
     Angulo_planeio) = Resultado_1
    
    return (Resultado_1)
#                                                                            #
##############################################################################