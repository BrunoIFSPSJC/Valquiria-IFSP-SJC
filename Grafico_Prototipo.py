##############################################################################
##                               Funcao Grafico                             ##
##                                                                          ##
## A funcao Grafico tem como objetivo plotar diferentes tipos de graficos   ##
## analiticos, para que o usuario possa ter resultados que possam auxiliar  ##
##no desenvolvimento de uma aeronave mais leve que o ar.                    ##                                         ## 
##                                                                          ##
##############################################################################

##############################################################################
## Aqui sao realizados todos os plots de graficos do programa               ##
##############################################################################

##############################################################################
## Bibliotecas                                                              ##
import pandas as pd                                                         ##
import matplotlib.pyplot as plt                                             ##
##############################################################################

def grafico (Quantidade_analises):
    
    contador = 2

    # Plotagem do peso vazio e peso bruto de decolagem
    # Aqui eu faco a atribuicao de valore de um excel em uma determinada variavel
    Dados_Tracao_Requerida = pd.read_excel('Resultados_Prototipo.xls',usecols=['Tracao Requerida (N)'])
    Dados_Tracao_Disponivel = pd.read_excel('Resultados_Prototipo.xls',usecols=['Tracao Disponivel (N)'])
    Dados_Potencia_Requerida = pd.read_excel('Resultados_Prototipo.xls',usecols=['Potencia Disponivel (W)'])
    Dados_Potencia_Disponivel = pd.read_excel('Resultados_Prototipo.xls',usecols=['Potencia Requerida (W)'])
    Dados_Razao_Subida = pd.read_excel('Resultados_Prototipo.xls',usecols=['Razao de subida ()'])
    Dados_Razao_Planeio = pd.read_excel('Resultados_Prototipo.xls',usecols=['Razao de planeio ()'])
    Velocidade = pd.read_excel('Resultados_Prototipo.xls',usecols=['Velocidade (m/s)'])
    
    ## https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html - locar um determinado valor da tabela
    
    '''
    
    cont_1 = 0
    armazena_1 = []
    armazena_2 = []
    armazena_3 = []
    
    while (Quantidade_analises > cont_1):
        
        #Transformar para Lista https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html
        Lista_1 = list (Dados_Tracao_Requerida['Tracao Requerida (N)'])
        Lista_2 = list (Dados_Tracao_Disponivel['Tracao Disponivel (N)'])
        Lista_3 = list (Velocidade['Velocidade (m/s)'])
        
        # https://pt.stackoverflow.com/questions/257905/retornando-somente-o-maior-valor-de-uma-lista-python     - Maior e monor da lista
        Maior_tracao = max(Lista_2)
        Menor_tracao = min(Lista_1)
        
        conta_1 = Lista_1 [cont_1]
        conta_2 = Lista_2 [cont_1]
        conta_3 = Lista_3 [cont_1]
        
        Resultado = conta_1 - conta_2
    
        if (Menor_tracao == conta_1):
            
            Vel_Menor_tracao = conta_3
            
            print (Vel_Menor_tracao)
            
        if (Maior_tracao == conta_2):
            
            Vel_Maior_tracao = conta_3
            
            print (Vel_Maior_tracao)
        
        if ((Resultado > 0.5)and(Resultado <1.5)):
            
            # https://www.datacamp.com/community/tutorials/python-list-methods?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9100214&gclid=CjwKCAjw1JeJBhB9EiwAV612y3xqid1YYh4bPmjCwGoFY_xzwj1kUBS5yeUMu8oBcgYZUW1Fe78uxBoCgj8QAvD_BwE     - uso do append
            armazena_1.append (conta_1)
            armazena_2.append (conta_2)
            armazena_3.append (conta_3)
            
            # https://pt.stackoverflow.com/questions/192567/removendo-elementos-duplicados-em-uma-lista-com-python   - Para tirar os repetidos
            # https://www.horadecodar.com.br/2021/05/11/remover-itens-duplicados-de-lista-em-python/    - para tirar os repetidos
            armazena_1 = list(set(armazena_1))
            armazena_2 = sorted(set(armazena_2))
            armazena_3 = list(set(armazena_3))
            print (armazena_1)
            print (armazena_2)
            print (armazena_3)
            
        cont_1 = cont_1 + 1
        
    '''
        
##########################Tracao################################

    if (contador == 1):
        
        ## https://www.youtube.com/watch?v=t4huiU3difE - criação de gráficos juntos
        ## https://www.youtube.com/watch?v=_nK3jeh8UFI - subplots de gráficos 
        plt.scatter(Velocidade, Dados_Tracao_Requerida, c='r', label = 'Tracao Requerida')
        plt.scatter(Velocidade, Dados_Tracao_Disponivel, c='g', label = 'Tracao Disponivel')
        # https://www.acervolima.com.br/2020/04/definindo-cores-com-matplotlib.html - Cores do python
        #plt.scatter(armazena_3[0], armazena_1[0], c='b', label = 'Velocidade Mínima')
        #plt.scatter(armazena_3[1], armazena_1[1], c='c', label = 'Velocida Máxima')
        #plt.scatter(Vel_Menor_tracao, Menor_tracao, c='m', label = 'Pico Requerida')
        #plt.scatter(Vel_Maior_tracao, Maior_tracao, c='y', label = 'Pico Disponível')
        plt.legend ()
       
        plt.xlabel ('Velocidade [m/s]')
        plt.ylabel ('Tracao [N]')
        
        plt.show ()
    
############################Potencia############################## 

    if (contador == 2):
        
        plt.scatter(Velocidade, Dados_Potencia_Disponivel, c='r', label = 'Potencia Disponivel')
        plt.scatter(Velocidade, Dados_Potencia_Requerida, c='b', label = 'Potencia Requerida')
        plt.legend ()
    
        plt.xlabel ('Velocidade [m/s]')
        plt.ylabel ('Potencia [W]')
    
        plt.show ()
        
    if (contador == 3):
        
        plt.scatter(Velocidade, Dados_Razao_Subida, c='r', label = 'Desempenho subida')
    
        plt.xlabel ('Velocidade [m/s]')
        plt.ylabel ('Razao de Subida [m/s]')
        
    if (contador == 4):
        
        plt.scatter(Velocidade, Dados_Razao_Planeio, c='r', label = 'Desempenho Planeio')
    
        plt.xlabel ('Velocidade [m/s]')
        plt.ylabel ('Razao de Planeio [m/s]')
           
        
    '''
    fig,ax = plt.subplots ()
    ax.set_xlabel ('Velocidade')
    ax.set_ylabel('Tracao Requerida')
    
    print (Dados_Tracao_Requerida)
    
    ax.plot(Velocidade,Dados_Tracao_Requerida,color = 'tomato')
    
    ax2 = ax.twinx ()
    ax2.set_ylabel('Tracao Disponivel')
    
    ax2.plot (Velocidade,Dados_Tracao_Disponivel)
    
    plt.show ()
    
    '''
    
    return 
    