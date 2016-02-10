# Grupo 008 (TG008) - Manuel Sousa (84740) & Tiago Novais (84888) #


# = = = = = = = = = = = = = = = = = = = = = = = = = #
#                                                   #
# = = =  F U N C O E S   A U X I L I A R E S  = = = #
#                                                   #
# = = = = = = = = = = = = = = = = = = = = = = = = = #

def tabuleiro_celulas_vazias(tabuleiro):
    """ 
    tabuleiro_celulas_vazias : tabuleiro -> logico
    tabuleiro_celulas_vazias(tabuleiro) Percorre as dimensoes das linhas e colunas do 
    tabuleiro atribuindo a celula um valor da coordenada pertencente ao tabuleiro caso 
    as instrucoes da celula nao estejam corretas retorna False 
    """
    dimensao = tabuleiro_dimensoes(tabuleiro)[0]

    for linha in range(dimensao):
        for coluna in range(dimensao):
            celula = tabuleiro_celula(tabuleiro, cria_coordenada(linha + 1, coluna + 1))
         
            if not(celula == 1 or celula == 2):
                return False
            
    return True 
# -- Fim: tabuleiro_celulas_vazias -- #

def numero_caracter(numero):
    """ 
    numero_caracter : inteiro -> caracter
    numero_caracter(numero) retorna o caracter correspondente ao numero de uma posisao do tabuleiro
    {0}-> Vazio ("?") {1}-> Vazio (".") {2}-> Vazio ("x")
    """
    if(numero == 0):
        return "?"

    return "." if numero == 1 else "x"
# -- Fim: numero_caracter -- #
 
def calcula_profundidade(tabuleiro):
    """ 
    calcula_profundidade : tabuleiro -> inteiro
    calcula_profundidade(tabuleiro) retorna um numero inteiro que indica 
    a profundidade maxima de uma especificacao
    """
    x = 0

    for l in range(len(tabuleiro)):
        x = max(x , len(tabuleiro[l]))

    return x
# -- Fim: calcula_profundidade -- #
 
def linha_completa(tuplo , coordenada):
    """ 
    linha_completa : tuplo , coordenada -> logico
    linha_completa(tuplo , coordenada) retorna o valor logico correspondente a comparacao
    de duas listas de especificacoes de linhas. Se forem iguais (True) a linha foi preenchida
    em conformidade com a sua especificacao
    """
    lista_conta = []
    tuple_para_lista = list(tuplo)    
    maximo = 0

    for l in range(len(coordenada)):
        if(coordenada[l] == 2):
            maximo += 1
        elif(maximo != 0):
            lista_conta.append(maximo)
            maximo = 0
        elif(coordenada[l] == 0):
            return False

    if(maximo != 0):
        lista_conta.append(maximo)

    return tuple_para_lista == lista_conta
# -- Fim: linha_completa -- #
 
def soma(especificacao):
    """ 
    soma : tuplo -> inteiro
    soma(especificacao) retorna um numero inteiro com a soma dos valores 
    de uma especificacao (linhas ou colunas)
    """
    soma = 0

    for a in range(len(especificacao)):
        for b in range(len(especificacao[a])):
            soma += especificacao[a][b]

    return soma
# -- Fim: soma -- #

def obtem_celulas(tabuleiro):
    """ 
    obtem_celulas : tabuleiro -> lista
    obtem_celulas(tabuleiro)
    """
    dimensao = tabuleiro_dimensoes(tabuleiro)[0]
    celulas = []
    
    for x in range(dimensao):
        linha_celulas = []
        
        for y in range(dimensao):
            linha_celulas += [tabuleiro_celula(tabuleiro, cria_coordenada(x + 1 , y + 1))]
            
        celulas += [linha_celulas]
        
    return celulas
# -- Fim: obtem_celulas -- #

def valida_coordenada_cadeia(coordenada_cadeia):
    """ 
    valida_coordenada_cadeia : string -> tuplo ou logico
    valida_coordenada_cadeia(coordenada_cadeia) retorna um tuplo apos verificar o formato de uma 
    jogada se esta mesmo respeitar o formato de jogada tipica (x : y) caso contrario retorna False
    """
    if not (len(coordenada_cadeia) >= 7 and coordenada_cadeia[0] == '(' and ' : ' in coordenada_cadeia and coordenada_cadeia[-1] == ')'):
        return False
    
    caracteres_especiais = 0
    conta = 0
    numero = ['', '']
    
    for x in coordenada_cadeia[1 : -1]: 
        if x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'): 
            numero[conta] += x 
        elif x in (' ', ':'): 
            caracteres_especiais += 1 
            conta = 1
        else:
            return False 
        
    if caracteres_especiais > 3 or '0' in numero: 
        return False
    
    return tuple(map(lambda x: int(x) , numero))
# -- Fim: valida_coordenada_cadeia -- #
 
# = = = = = = = = = = = = = = = = = = = = = = = = = #
#                                                   #
# = = =  F U N C O E S   P R I N C I P A I S  = = = #
#                                                   #
# = = = = = = = = = = = = = = = = = = = = = = = = = #


# = = = = = = = = = = = = = == = = #
# = = =  T A D (coordenada)  = = = #
# = = = = = = = = = = = = = == = = #

def cria_coordenada(linha , coluna):
    """ 
    # Construtor #
    cria_coordenada : inteiro , inteiro -> coordenada (tuple)
    cria_coordenada(linha , coluna) retorna um tuplo de dois elementos (coordenada) em que 
    ambos os elementos correspondem a uma coordenada (x,y) inteira maior que zero
    """
    if not (isinstance(linha , (int)) and isinstance(coluna , (int)) and linha > 0 and coluna > 0):
        raise ValueError("cria_coordenada: argumentos invalidos")
 
    return tuple((linha , coluna))
# -- Fim: cria_coordenada -- #
 
def coordenada_linha(coordenada):
    """ 
    # Seletor #
    coordenada_linha : coordenada -> inteiro
    coordenada_linha(coordenada) retorna o primeiro elemento da coordenada, a linha (x)
    """
    return coordenada[0]
# -- Fim: coordenada_linha -- #
 
def coordenada_coluna(coordenada):
    """ 
    # Seletor #
    coordenada_coluna : coordenada -> inteiro
    coordenada_coluna(coordenada) retorna o segundo elemento da coordenada, a coluna (y)
    """
    return coordenada[1]
# -- Fim: coordenada_coluna -- #
 
def e_coordenada(coordenada):
    """ 
    # Reconhecedor #
    e_coordenada : universal -> logico
    e_coordenada(coordenada) retorna um valor logico apos verificar com um conjunto de testes se e coordenada ou nao.
    True -> E coordenada | False -> Nao e coordenada
    """
    return isinstance(coordenada , tuple) and len(coordenada) == 2 and isinstance(coordenada[0] , int) \
       and isinstance(coordenada[1] , int) and coordenada[0] > 0  and coordenada[1] > 0   
# -- Fim: e_coordenada -- #
 
def coordenadas_iguais(coordenada1 , coordenada2):
    """ 
    # Teste #
    coordenadas_iguais : coordenada , coordenada -> logico
    coordenadas_iguais(coordenada1 , coordenada2) retorna um valor logico apos comparar se
    as duas coordenadas forem iguais. True -> se forem iguais | False -> se forem diferentes
    """
    return coordenada1 == coordenada2
# -- Fim: coordenadas_iguais -- #
 
def coordenada_para_cadeia(coordenada):
    """ 
    coordenada_para_cadeia : coordenada -> string
    coordenada_para_cadeia(coordenada) retorna uma coordenada em formato de cadeia de caracteres
    """ 
    return "(" + str(coordenada_linha(coordenada)) + " : " + str(coordenada_coluna(coordenada)) + ")"
# -- Fim: coordenada_para_cadeia -- #


# = = = = = = = = = = = = = = = = #
# = = =  T A D (tabuleiro)  = = = #
# = = = = = = = = = = = = = = = = #

def cria_tabuleiro(tuplo):
    """ 
    # Construtor #
    cria_tabuleiro : tuplo -> tabuleiro
    cria_tabuleiro(tuplo) retorna uma lista com a estrutura de um tabuleiro. Caso as instrucoes
    para a criacao do tabuleiro nao estiverem TODAS corretas, ira retornar ValueError
    """
    if not (isinstance(tuplo , tuple) and len(tuplo) == 2):
        raise ValueError("cria_tabuleiro: argumentos invalidos")

    if not (isinstance(tuplo[0] , tuple) and isinstance(tuplo[1], tuple) and len(tuplo[0]) == len(tuplo[1])):
        raise ValueError("cria_tabuleiro: argumentos invalidos")

    for a in range(len(tuplo)):
        for b in range(len(tuplo[a])):
            if not (isinstance(tuplo[a][b] , tuple)):
                raise ValueError("cria_tabuleiro: argumentos invalidos")
            for c in range(len(tuplo[a][b])):
                if not (isinstance(tuplo[a][b][c] , int)):
                    raise ValueError("cria_tabuleiro: argumentos invalidos")

    if not (soma(tuplo[0]) == soma(tuplo[1])):
        raise ValueError("cria_tabuleiro: argumentos invalidos")
 
    tamanho_tabuleiro_jogo = len(tuplo[0])
    #Ciclo em compreensao para inicializar todas as posicoes do tabuleiro a 0
    tabuleiro_jogo = [[0 for x in range(tamanho_tabuleiro_jogo)] for x in range(tamanho_tabuleiro_jogo)]
    return [tuplo,tabuleiro_jogo]
# -- Fim: cria_tabuleiro -- #

def tabuleiro_dimensoes(tabuleiro):
    """ 
    # Seletor #
    tabuleiro_dimensoes : tabuleiro -> tuplo
    tabuleiro_dimensoes(tabuleiro) retorna um tuplo com as dimensoes do tabuleiro
    """
    return (len(tabuleiro[0][0]) , len(tabuleiro[0][0]))
# -- Fim: tabuleiro_dimensoes -- #
 
def tabuleiro_especificacoes(tabuleiro):
    """ 
    # Seletor #
    tabuleiro_especificacoes : tabuleiro -> tuplo (especificacoes)
    tabuleiro_especificacoes(tabuleiro) retorna um tuplo com as especificacoes das linhas e das colunas
    """
    return tabuleiro[0]
# -- Fim: tabuleiro_especificacoes -- #

def tabuleiro_celula(tabuleiro , coordenada):
    """ 
    # Seletor #
    tabuleiro_celula : tabuleiro , coordenada -> tabuleiro
    tabuleiro_celula(tabuleiro , coordenada) retorna o valor correspondente ao caracter do tabuleiro
    de uma determianda coordenada
    """
    if not (e_coordenada(coordenada) and e_tabuleiro(tabuleiro)\
    and coordenada_coluna(coordenada) <= tabuleiro_dimensoes(tabuleiro)[0]\
    and coordenada_linha(coordenada) <= tabuleiro_dimensoes(tabuleiro)[0]):
        raise ValueError("tabuleiro_celula: argumentos invalidos")
 
    return tabuleiro[1][coordenada_linha(coordenada)-1][coordenada_coluna(coordenada)-1]
# -- Fim: tabuleiro_celula -- #
 
def tabuleiro_preenche_celula(tabuleiro , coordenada , numero):
    """ 
    # Modificador #
    tabuleiro_preenche_celula : tabuleiro , coordenada , numero -> tabuleiro
    tabuleiro_preenche_celula(tabuleiro , coordenada , numero) retorna um tabuleiro atualizado com a nova alteracao 
    do estado da coordenada no tabuleiro {0,1,2}. Caso um dos parametros da funcao seja invalido, retorna ValueError
    """
    if not (e_coordenada(coordenada) and e_tabuleiro(tabuleiro)\
    and isinstance(numero,(int)) and 0 <= numero <= 2\
    and coordenada_coluna(coordenada) <= tabuleiro_dimensoes(tabuleiro)[0]\
    and coordenada_linha(coordenada) <= tabuleiro_dimensoes(tabuleiro)[0]):
        raise ValueError("tabuleiro_preenche_celula: argumentos invalidos")
 
    tabuleiro[1][coordenada_linha(coordenada)-1][coordenada_coluna(coordenada)-1] = numero
    return tabuleiro
# -- Fim: tabuleiro_preenche_celula -- #

def e_tabuleiro(tabuleiro):
    """ 
    # Reconhecedor #
    e_tabuleiro : universal -> logico
    e_tabuleiro(coordenada) retorna um valor logico apos verificar com um conjunto de testes se e tabuleiro ou nao.
    True -> E tabuleiro | False -> Nao e tabuleiro
    """
    if not ( isinstance(tabuleiro , list) and len(tabuleiro) == 2):
        return False
  
    if not ( isinstance(tabuleiro[0] , tuple) and isinstance(tabuleiro[1] , list)):
        return False
 
    if not ( len(tabuleiro[0]) == 2 and isinstance(tabuleiro[0][1] , tuple) and isinstance(tabuleiro[0][1] , tuple) ):
        return False
  
    if not (len(tabuleiro[0][0]) == len(tabuleiro[0][1])):
        return False
 
    if not (len(tabuleiro[0][0]) == len(tabuleiro[1]) and soma(tabuleiro[0][0]) == soma(tabuleiro[0][1])):
        return False
  
    for a in range(len(tabuleiro[0])):
        for b in range(len(tabuleiro[0][a])):
            if not (isinstance(tabuleiro[0][a][b] , tuple)):
                return False
            for c in range(len(tabuleiro[0][a][b])):
                if not (isinstance(tabuleiro[0][a][b][c] , int)):
                    return False
   
    tamanho = len(tabuleiro[1][0])
    for linha in range(tabuleiro_dimensoes(tabuleiro)[0]):
        if not (len(tabuleiro[0][0]) == len(tabuleiro[1][linha])):
            return False
        for coluna in range(tabuleiro_dimensoes(tabuleiro)[0]):
            if not (isinstance(tabuleiro[1][linha][c] , int)):
                return False
            if (tabuleiro[1][linha][coluna] != 0 and tabuleiro[1][linha][coluna] != 1 and tabuleiro[1][linha][coluna] != 2):
                return False
        if not ( isinstance(tabuleiro[1][linha] , list) or tamanho != len(tabuleiro[1][linha])):
            return False
 
    return True
# -- Fim: e_tabuleiro -- #

def tabuleiro_completo(tabuleiro):
    """ 
    # Reconhecedor #
    tabuleiro_completo : tabuleiro -> logico
    tabuleiro_completo(tabuleiro) retorna um valor logico apos verificar se o tabuleiro esta
    completo sobre todas as especificacoes. True -> se estiver completo | False -> se nao estiver completo
    """
    if not (tabuleiro_celulas_vazias(tabuleiro)):
        return False
    
    matriz = obtem_celulas(tabuleiro)
    matriz_transposta = list(zip(*matriz)) #Troca as linhas por colunas. Desta podemos comparar facilmente as colunas como se fossem linhas
    
    for x in range(tabuleiro_dimensoes(tabuleiro)[0]):
        if not(linha_completa(tabuleiro_especificacoes(tabuleiro)[0][x] , matriz[x])\
        or linha_completa(tabuleiro_especificacoes(tabuleiro)[1][x] , matriz_transposta[x])):
            return False
    
    return True
# -- Fim: tabuleiro_completo -- #
 
def tabuleiros_iguais(tabuleiro1 , tabuleiro2):
    """ 
    # Teste #
    tabuleiros_iguais : tabuleiro , tabuleiro -> logico
    tabuleiros_iguais(tabuleiro1 , tabuleiro2) retorna um valor logico apos comparar se
    os dois tabuleiros forem iguais. True -> se forem iguais | False -> se forem diferentes
    """
    return tabuleiro1 == tabuleiro2
# -- Fim: tabuleiros_iguais -- #

def escreve_tabuleiro(tabuleiro):
    """
    # Transformador de saida #
    escreve_tabuleiro : tabuleiro -> NADA (imprime o tabuleiro)
    escreve_tabuleiro(tabuleiro) ira imprimir o tabuleiro tendo em conta as profundidades maximas
    das especificacoes e dos espacos em branco a dar
    """
    if not (e_tabuleiro(tabuleiro)):
        raise ValueError ('escreve_tabuleiro: argumentos invalidos')

    i = calcula_profundidade(tabuleiro_especificacoes(tabuleiro)[1]) - 1
    especificacoes_linhas = tabuleiro_especificacoes(tabuleiro)[0]
    especificacoes_colunas = tabuleiro_especificacoes(tabuleiro)[1]
    dimensao = tabuleiro_dimensoes(tabuleiro)[1]
    #Imprimir as especificacoes do topo
    while i >=0:
        print(end="  ")
        for l in range(dimensao):
            if(len(especificacoes_colunas[l]) >= i+1 and l+1 != dimensao):
                t=len(especificacoes_colunas[l]) - i-1
                print(especificacoes_colunas[l][t] , end="    ")
            elif(len(especificacoes_colunas[l]) >= i+1 and l+1==dimensao):
                t=len(especificacoes_colunas[l]) - i-1
                print(especificacoes_colunas[l][t] , end="    ")
            elif not (len(especificacoes_colunas[l]) >= i+1) and l+1 == dimensao:
                print(end="     ")
            else:
                print(end="     ")
        i-=1
        print()
    #Imprime os quadrados do Tabuleiro e as especificacoes laterais
    dimensao = tabuleiro_dimensoes(tabuleiro)[0]
    for l in range(dimensao):
      	#Imprime linha a linha, o tabuleiro
        for c in range(dimensao):
            print('[' , numero_caracter(tabuleiro_celula(tabuleiro,cria_coordenada(l+1,c+1))) , ']' , end="")
        
        print(end = " ")
        profundidade = calcula_profundidade(especificacoes_linhas)
        #Imprime especificacoes relativas a linha do tabuleiro impressa
        for a in range(profundidade):
            if(len(especificacoes_linhas[l]) >= a+1 and (a+1) != profundidade):
                print(especificacoes_linhas[l][a],end=" ")
            elif(len(especificacoes_linhas[l]) >= a+1 and (a+1) == profundidade):
                print(especificacoes_linhas[l][a] , end="")
            elif (a+1) == profundidade:
                print(end=" ")
            else:
                print(end="  ")
        print(end="|")
        print()
    print()
# -- Fim: escreve_tabuleiro -- #


# = = = = = = = = = = = = = = = = #
# = = = =  T A D (jogada) = = = = #
# = = = = = = = = = = = = = = = = #

def cria_jogada(coordenada , numero):
    """ 
    # Construtor #
    cria_jogada : coordenada , numero -> jogada
    cria_jogada(coordenada , numero) cria uma lista que representa uma jogada apos verificar se a coordenada
    e o numero (relativo a um caracter) sao validos. Caso nao sejam dados validos, retorna uma ValueError
    """
    if not (e_coordenada(coordenada) and isinstance(numero , (int))  and 0 < numero <= 2):
        raise ValueError("cria_jogada: argumentos invalidos")
 
    jogada = []
    jogada.append(coordenada)
    jogada.append(numero)

    return jogada
# -- Fim: cria_jogada -- #

def jogada_coordenada(jogada):
    """ 
    # Seletor #
    jogada_coordenada : jogada -> tuplo (coordenada)
    jogada_coordenada(jogada) retorna a coordenada relativa a jogada
    """
    return jogada[0]
# -- Fim: jogada_coordenada -- #

def jogada_valor(jogada):
    """ 
    # Seletor #
    jogada_valor : jogada -> inteiro
    jogada_valor(jogada) retorna o numero inteiro relativo a jogada
    """
    return jogada[1]
# -- Fim: jogada_valor -- #

def e_jogada(jogada):
    """
    # Reconhecedor #
    e_jogada : universal -> logico
    e_jogada(jogada) retorna um valor logico apos verificar com um conjunto de testes se e jogada ou nao.
    True -> E jogada | False -> Nao e jogada
    """
    return isinstance(jogada , (list)) and len(jogada) == 2 and e_coordenada(jogada[0]) \
    and isinstance(jogada[1] , (int)) and (jogada[1] == 0 or jogada[1] == 1 or jogada[1] == 2 )
# -- Fim: e_jogada -- #

def jogadas_iguais(jogada1 , jogada2):
    """ 
    # Teste #
    jogadas_iguais : jogada , jogada -> logico
    jogadas_iguais(jogada1 , jogada2) retorna um valor logico apos comparar se
    as duas jogadas sao iguais. True -> se forem iguais | False -> se forem diferentes
    """
    return jogada1 == jogada2
# -- Fim: jogadas_iguais -- #

def jogada_para_cadeia(jogada):
    """ 
    jogada_para_cadeia : jogada -> string (coordenada_cadeia)
    jogada_para_cadeia(jogada) retorna uma jogada no formato de uma cadeia de caracteres
    """
    return coordenada_para_cadeia(jogada_coordenada(jogada)) + ' --> ' + str(jogada_valor(jogada))
# -- Fim: jogada_para_cadeia -- #

def le_tabuleiro(ficheiro):
    """ 
    le_tabuleiro : string -> tuplo (especificacoes)
    le_tabuleiro(ficheiro) retorna um tuplo com as especificacoes de um tabileiro (lido por um ficheiro)
    """
    ficheiro_lido = open(ficheiro , 'r')
    jogo_lido = ficheiro_lido.readline()
    ficheiro_lido.close()
    return eval(jogo_lido)
# -- Fim: le_tabuleiro -- #



# = = = = = = = = = = = = = = = = = = = = = = = = = #
#                                                   #
# = = =  F U N C O E S  A D I C I O N A I S   = = = #
#                                                   #
# = = = = = = = = = = = = = = = = = = = = = = = = = #

def jogo_picross(ficheiro):
    """ 
    jogo_picross : string -> logico
    jogo_picross(ficheiro) interage com o utilizador de forma a que este possa jogar o jogo PICROSS. Pede jogadas 
    e vai escrevendo o tabuleiro. Valida o que o utilizador insere e termina o jogo quando preencher o tabuleiro todo.
    Indica tambem se o tabuleiro esta corretamente preenchido
    """
    tabuleiro = cria_tabuleiro(le_tabuleiro(ficheiro))
    print("JOGO PICROSS")

    while not(tabuleiro_celulas_vazias(tabuleiro)):  
        escreve_tabuleiro(tabuleiro)
        jogada = pede_jogada(tabuleiro)
     
        while not e_jogada(jogada):
            print('Jogada invalida.')
            jogada = pede_jogada(tabuleiro)
            
        tabuleiro = tabuleiro_preenche_celula(tabuleiro, jogada_coordenada(jogada), jogada_valor(jogada))
    escreve_tabuleiro(tabuleiro)
   
    if tabuleiro_completo(tabuleiro):
        print('JOGO: Parabens, encontrou a solucao!')
        return True
    else:
        print('JOGO: O tabuleiro nao esta correto!')
        return False
# -- Fim: jogo_picross -- #

def pede_jogada(tabuleiro):
    """ 
    pede_jogada : tabuleiro -> jogada
    pede_jogada(tabuleiro) cria uma jogada, apos receber valores do utilizador. Se os valores nao respeitarem um conjunto 
    de valicadoes a funcao retornara um valor logico (False)
    """
    print('Introduza a jogada')
    dimensao = tabuleiro_dimensoes(tabuleiro)[0]
    coordenada = input('- coordenada entre (1 : 1) e (%i : %i) >> ' % (dimensao , dimensao))
    valor = int(input('- valor >> '))
    
    coordenada = valida_coordenada_cadeia(coordenada)

    if not(coordenada and 1 <= coordenada[0] <= dimensao and 1 <= coordenada[1] <= dimensao):
        return False
    return cria_jogada(cria_coordenada(coordenada[0] , coordenada[1]) , valor)
# -- Fim: pede_jogada -- #