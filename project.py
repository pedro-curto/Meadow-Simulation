# -------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------| 103091 Pedro Curto |-----------------------------------------------#
# ----------------------------------------------| Projeto 2: O Prado |-----------------------------------------------#
# -------------------------------------------------------------------------------------------------------------------#

# -##################################################################################################################-#
#                                                     TAD POSICAO                                                     #
# -##################################################################################################################-#

#######################################################################################################################
#                                 Representação interna:(coordenada x, coordenada y)                                  #
#######################################################################################################################
#                                           Funções encontradas nesta TAD:                                            #
# ------------------------------------------------------------------------------------------------------------------- #
#                                         cria_posicao: int x int -> posicao                                          #
# ------------------------------------------------------------------------------------------------------------------- #
#                                       cria_copia_posicao: posicao -> posicao                                        #
# ------------------------------------------------------------------------------------------------------------------- #
#                                             obter_pos_x: posicao -> int                                             #
# ------------------------------------------------------------------------------------------------------------------- #
#                                             obter_pos_y: posicao -> int                                             #
# ------------------------------------------------------------------------------------------------------------------- #
#                                          eh_posicao: universal -> booleano                                          #
# ------------------------------------------------------------------------------------------------------------------- #
#                                   posicoes_iguais: posicao x posicao -> booleano                                    #
# ------------------------------------------------------------------------------------------------------------------- #
#                                          posicao_para_str: posicao -> str                                           #
# -##################################################################################################################-#

# Construtor:

def cria_posicao(x, y):
    """
    cria_posicao: int x int -> posicao
    Recebe dois inteiros x, y que correspondem respetivamente às coordenadas x e y de uma posição,
    e devolve a respetiva posição. Se os argumentos fornecidos forem inválidos, é gerado um erro.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("cria_posicao: argumentos invalidos")
    if x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return x, y


def cria_copia_posicao(p):
    """
    cria_copia_posicao: posicao -> posicao
    Recebe uma posição p e devolve uma cópia da mesma.
    """
    return cria_posicao(obter_pos_x(p), obter_pos_y(p))


# --------------------------------------------------------------------------------------------------------------------#

# Seletores:

def obter_pos_x(p):
    """
    obter_pos_x: posicao -> int
    Recebe uma posição p e devolve a componente x da posição.
    """
    return p[0]


def obter_pos_y(p):
    """
    obter_pos_y: posicao -> int
    Recebe uma posição p e devolve a componente y da posição.
    """
    return p[1]


# --------------------------------------------------------------------------------------------------------------------#

# Reconhecedor:

def eh_posicao(arg):
    """
    eh_posicao: universal -> booleano
    Recebe qualquer argumento e retorna True se corresponder a um TAD posição, senão retorna False.
    """
    if not isinstance(arg, tuple):
        return False
    if len(arg) != 2:
        return False
    if not isinstance(arg[0], int) or not isinstance(arg[1], int):
        return False
    if arg[0] < 0 or arg[1] < 0:
        return False
    return True


# --------------------------------------------------------------------------------------------------------------------#

# Teste:

def posicoes_iguais(p1, p2):
    """
    posicoes_iguais: posicao x posicao -> booleano
    Recebe duas posições p1, p2 e retorna True se forem iguais; em caso contrário, retorna False.
    """
    if eh_posicao(p1) and eh_posicao(p2) and obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2):
        return True
    return False


# --------------------------------------------------------------------------------------------------------------------#

# Transformador:

def posicao_para_str(p):
    """
    posicao_para_str: posicao -> str
    Recebe uma posição p e retorna a string correspondente ao argumento.
    """
    return str(p)


# --------------------------------------------------------------------------------------------------------------------#

# Funções de alto nivel:

def obter_posicoes_adjacentes(p):
    """
    obter_posicoes_adjacentes: posicao -> tuplo
    Recebe uma posição p e devolve um tuplo com as posições adjacentes, iniciando na posição acima
    e seguindo o sentido horário.
    """
    res = ()
    x, y = obter_pos_x(p), obter_pos_y(p)
    lst = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    for i in range(len(lst)-1, -1, -1):
        if lst[i][0] < 0 or lst[i][1] < 0:
            del lst[i]
    for pair in lst:
        res += (cria_posicao(pair[0], pair[1]),)
    return res


def ordenar_posicoes(t):
    """
    ordenar_posicoes: tuplo -> tuplo
    Recebe um tuplo t com posições, ordena-as de acordo com a ordem de leitura de posições
    e retorna o tuplo ordenado.
    """
    # 1) obter maior posicao x de todas
    # 2) formula matematica para calcular numero de cada posicao: maxX * y + x
    #    (usamos x_max pois não sabemos a medida exata de Nx do prado)
    # 3) ordenar conforme a fórmula matemática
    x_max = obter_pos_x(max(t, key=lambda pos: obter_pos_x(pos)))
    return tuple(sorted(t, key=lambda pos: x_max * obter_pos_y(pos) + obter_pos_x(pos)))


# -##################################################################################################################-#
#                                                     TAD ANIMAL                                                      #
# -##################################################################################################################-#

#######################################################################################################################
#  Representação interna:{'especie':especie, 'idade':idade, 'freq_alim':freq_alim, 'freq_rep':freq_rep, 'fome':fome}  #
#######################################################################################################################
#                                           Funções encontradas nesta TAD:                                            #
# ------------------------------------------------------------------------------------------------------------------- #
#                                       cria_animal: str x int x int -> animal                                        #
# ------------------------------------------------------------------------------------------------------------------- #
#                                         cria_copia_animal: animal -> animal                                         #
# ------------------------------------------------------------------------------------------------------------------- #
#                                            obter_especie: animal -> str                                             #
# ------------------------------------------------------------------------------------------------------------------- #
#                                         obter_freq_reproducao: animal -> int                                        #
# ------------------------------------------------------------------------------------------------------------------- #
#                                        obter_freq_alimentacao: animal -> int                                        #
# ------------------------------------------------------------------------------------------------------------------- #
#                                             obter_idade: animal -> int                                              #
# ------------------------------------------------------------------------------------------------------------------- #
#                                              obter_fome: animal -> int                                              #
# ------------------------------------------------------------------------------------------------------------------- #
#                                           aumenta_idade: animal -> animal                                           #
# ------------------------------------------------------------------------------------------------------------------- #
#                                            reset_idade: animal -> animal                                            #
# ------------------------------------------------------------------------------------------------------------------- #
#                                            aumenta_fome: animal -> animal                                           #
# ------------------------------------------------------------------------------------------------------------------- #
#                                            reset_fome: animal -> animal                                             #
# ------------------------------------------------------------------------------------------------------------------- #
#                                          eh_animal: universal -> booleano                                           #
# ------------------------------------------------------------------------------------------------------------------- #
#                                         eh_predador: universal -> booleano                                          #
# ------------------------------------------------------------------------------------------------------------------- #
#                                           eh_presa: universal -> booleano                                           #
# ------------------------------------------------------------------------------------------------------------------- #
#                                     animais_iguais: animal x animal -> booleano                                     #
# ------------------------------------------------------------------------------------------------------------------- #
#                                           animal_para_char: animal -> str                                           #
# ------------------------------------------------------------------------------------------------------------------- #
#                                           animal_para_str: animal -> str                                            #
# -##################################################################################################################-#

# Construtores:

def cria_animal(s, r, a):
    """
    cria_animal: str x int x int -> animal
    Recebe uma cadeia de caracteres s e dois valores inteiros r, a que correspondem respetivamente
    à frequência de reprodução e à frequência de alimentação, e devolve o animal correspondente.
    Gera um erro caso os argumentos fornecidos sejam inválidos.
    """
    if not isinstance(s, str) or not isinstance(r, int) or not isinstance(a, int):
        raise ValueError("cria_animal: argumentos invalidos")
    if len(s) == 0 or r <= 0 or a < 0:
        raise ValueError("cria_animal: argumentos invalidos")
    if a > 0:
        return {'especie': s, 'idade': 0, 'freq_alim': a, 'freq_rep': r, 'fome': 0}
    else:
        return {'especie': s, 'idade': 0, 'freq_rep': r}


def cria_copia_animal(a):
    """
    cria_copia_animal: animal -> animal
    Recebe um animal a e retorna uma cópia do mesmo.
    """
    return dict(a)


# --------------------------------------------------------------------------------------------------------------------#

# Seletores:

def obter_especie(a):
    """
    obter_especie: animal -> str
    Recebe um animal a e devolve a sua espécie.
    """
    return a['especie']


def obter_freq_reproducao(a):
    """
    obter_freq_alimentacao: animal -> int
    Recebe um animal a e devolve a sua frequência de reprodução.
    """
    return a['freq_rep']


def obter_freq_alimentacao(a):
    """
    obter_freq_alimentacao: animal -> int
    Recebe um animal a e devolve a sua frequência de alimentação. As presas retornam sempre 0.
    """
    if eh_predador(a):
        return a['freq_alim']
    return 0


def obter_idade(a):
    """
    obter_idade: animal -> int
    Recebe um animal a e devolve a sua idade.
    """
    return a['idade']


def obter_fome(a):
    """
    obter_freq_alimentacao: animal -> int
    Recebe um animal a e devolve a sua fome. As presas retornam sempre 0.
    """
    if eh_predador(a):
        return a['fome']
    return 0


# --------------------------------------------------------------------------------------------------------------------#

# Modificadores:

def aumenta_idade(a):
    """
    aumenta_idade: animal -> animal
    Recebe um animal a e altera a sua idade, aumentando-a em 1.
    """
    a['idade'] += 1
    return a


def reset_idade(a):
    """
    reset_idade: animal -> animal
    Recebe um animal a e altera a sua idade, definindo-a como 0.
    """
    a['idade'] = 0
    return a


def aumenta_fome(a):
    """
    aumenta_fome: animal -> animal
    Recebe um animal a e altera a sua fome, aumentando-a em 1. Presas ficam inalteradas.
    """
    if eh_predador(a):
        a['fome'] += 1
    return a


def reset_fome(a):
    """
    reset_fome: animal -> animal
    Recebe um animal a e altera a sua fome, definindo-a como 0. Presas ficam inalteradas.
    """
    if eh_predador(a):
        a['fome'] = 0
    return a


# --------------------------------------------------------------------------------------------------------------------#

# Reconhecedores:

def eh_animal(arg):
    """
    eh_animal: universal -> booleano
    Recebe qualquer tipo de argumento e devolve True se e somente se corresponder a uma TAD animal.
    """
    if not isinstance(arg, dict):
        return False
    if len(arg) != 3 and len(arg) != 5:
        return False
    if len(arg) == 3 and not all(key in arg for key in ('idade', 'especie', 'freq_rep')):
        return False
    if len(arg) == 5 and not all(key in arg for key in ('idade', 'especie', 'freq_rep', 'fome',
        'freq_alim') or not isinstance(arg['freq_alim'], int) or not isinstance(arg['fome'], int)):
        return False
    if not isinstance(arg['idade'], int) or not isinstance(arg['especie'], str) \
            or not isinstance(arg['freq_rep'], int):
        return False
    return True


def eh_predador(arg):
    """
    eh_predador: universal -> booleano
    Recebe qualquer tipo de argumento e devolve True se e somente se corresponder a um
    TAD animal do tipo predador.
    """
    if eh_animal(arg):
        if len(arg) == 5 and all(key in arg for key in ('idade', 'especie', 'freq_rep', 'freq_alim',
                                                        'fome')):
            if arg['freq_alim'] > 0:
                return True
    return False


def eh_presa(arg):
    """
    eh_presa: universal -> booleano
    Recebe qualquer tipo de argumento e devolve True se e somente se corresponder a uma
    TAD animal do tipo presa.
    """
    if not eh_animal(arg):
        return False
    if len(arg) != 3:
        return False
    return True


# --------------------------------------------------------------------------------------------------------------------#

# Teste:

def animais_iguais(a1, a2):
    """
    animais_iguais: animal x animal -> booleano
    Recebe como argumento dois animais a1, a2 e devolve True apenas se estes forem iguais;
    senão, retorna False.
    """
    return a1 == a2


# --------------------------------------------------------------------------------------------------------------------#

# Transformadores:

def animal_para_char(a):
    """
    animal_para_char: animal -> str
    Recebe como argumento um animal a e retorna um único caracter correspondente à primeira letra
    da espécie do animal, em maiúscula se for predador e em minúscula se for presa.
    """
    if eh_presa(a):
        return a['especie'][0].lower()
    if eh_predador(a):
        return a['especie'][0].upper()


def animal_para_str(a):
    """
    animal_para_str: animal -> str
    Recebe como argumento um animal a, transforma-o numa string e devolve o resultado da
    transformação.
    """
    if eh_presa(a):
        return '{} [{}/{}]'.format(obter_especie(a), obter_idade(a), obter_freq_reproducao(a))
    if eh_predador(a):
        return '{} [{}/{};{}/{}]'.format(obter_especie(a), obter_idade(a), obter_freq_reproducao(a),
                                         obter_fome(a),obter_freq_alimentacao(a))


# --------------------------------------------------------------------------------------------------------------------#

# Funções de alto nivel:

def eh_animal_fertil(a):
    """
    eh_animal_fertil: animal -> booleano
    Recebe um animal a e retorna True se o animal estiver em idade de reprodução;
    em caso contrário, devolve False.
    """
    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """
    animal_para_str: animal -> booleano
    Recebe um animal a e retorna True se este estiver faminto (fome superior ou igual à
    frequência de alimentação), senão, retorna False. As presas retornam sempre False.
    """
    return eh_predador(a) and obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """
    reproduz_animal: animal -> animal
    Recebe um animal a, modifica-o destrutivamente alterando a sua idade para 0 e devolve um novo
    animal da mesma espécie, com idade e fome iguais a 0.
    """
    reset_idade(a)
    new_animal = cria_copia_animal(a)
    reset_fome(new_animal)
    reset_idade(new_animal)
    return new_animal


# -##################################################################################################################-#
#                                                      TAD PRADO                                                      #
# -##################################################################################################################-#

#######################################################################################################################
#    Representação interna: [pos montanha canto inf direito, tuplo pos rochedos, tuplo animais, tuplo pos animais ]   #
#######################################################################################################################
#                                           Funções encontradas nesta TAD:                                            #
# ------------------------------------------------------------------------------------------------------------------- #
#                                cria_prado: posicao x tuplo x tuplo x tuplo -> prado                                 #
# ------------------------------------------------------------------------------------------------------------------- #
#                                          cria_copia_prado: prado -> prado                                           #
# ------------------------------------------------------------------------------------------------------------------- #
#                                            obter_tamanho_x: prado -> int                                            #
# ------------------------------------------------------------------------------------------------------------------- #
#                                            obter_tamanho_y: prado -> int                                            #
# ------------------------------------------------------------------------------------------------------------------- #
#                                        obter_numero_predadores: prado -> int                                        #
# ------------------------------------------------------------------------------------------------------------------- #
#                                          obter_numero_presas: prado -> int                                          #
# ------------------------------------------------------------------------------------------------------------------- #
#                                   obter_posicao_animais: prado -> tuplo posicoes                                    #
# ------------------------------------------------------------------------------------------------------------------- #
#                                       obter_animal: prado x posicao -> animal                                       #
# ------------------------------------------------------------------------------------------------------------------- #
#                                      eliminar_animal: prado x posicao -> prado                                      #
# ------------------------------------------------------------------------------------------------------------------- #
#                                   mover_animal: prado x posicao x posicao -> prado                                  #
# ------------------------------------------------------------------------------------------------------------------- #
#                                  inserir_animal: prado x animal x posicao -> prado                                  #
# ------------------------------------------------------------------------------------------------------------------- #
#                                           eh_prado: universal -> booleano                                           #
# ------------------------------------------------------------------------------------------------------------------- #
#                                   eh_posicao_animal: prado x posicao -> booleano                                    #
# ------------------------------------------------------------------------------------------------------------------- #
#                                  eh_posicao_obstaculo: prado x posicao -> booleano                                  #
# ------------------------------------------------------------------------------------------------------------------- #
#                                    eh_posicao_livre: prado x posicao -> booleano                                    #
# ------------------------------------------------------------------------------------------------------------------- #
#                                      prados_iguais: prado x prado -> booleano                                       #
# ------------------------------------------------------------------------------------------------------------------- #
#                                            prado_para_str: prado -> str                                             #
# -##################################################################################################################-#

# Construtor:

def cria_prado(d, r, a, p):
    """
    cria_prado: posicao x tuplo x tuplo x tuplo -> prado
    Recebe a posição d da montanha no canto inferior direito do prado, um tuplo r com 0 ou mais
    elementos que representa as posições de rochedos no prado, um tuplo a com 1 ou mais elementos
    que correspondem a animais e um tuplo p da mesma dimensão do tuplo a, que indica as posições
    ocupadas por cada animal, e retorna o prado correspondente de acordo com estes dados.
    Se os argumentos não corresponderem ao esperado, é gerado um erro.
    """
    if not eh_posicao(d):
        raise ValueError("cria_prado: argumentos invalidos")
    if not all(isinstance(els, tuple) for els in (r, a, p)):
        raise ValueError("cria_prado: argumentos invalidos")
    if len(a) == 0 or len(p) == 0 or len(a) != len(p):
        raise ValueError("cria_prado: argumentos invalidos")
    if any(not eh_posicao(el) for el in r) or any(not eh_animal(ani) for ani in a)\
    or any(not eh_posicao(el) for el in p):
        raise ValueError("cria_prado: argumentos invalidos")
    # verificar se os rochedos estão dentro do prado (excluindo fronteira)
    max_x = obter_pos_x(d)
    max_y = obter_pos_y(d)
    for pos in r:
        x = obter_pos_x(pos)
        y = obter_pos_y(pos)
        if x <= 0 or x >= max_x or y <= 0 or y >= max_y:
            raise ValueError("cria_prado: argumentos invalidos")
    # verificar se todos os rochedos estão em posições diferentes
    for i in range(len(r)):
        for j in range(len(r)):
            if i != j:
                if posicoes_iguais(r[i], r[j]):
                    raise ValueError("cria_prado: argumentos invalidos")
    # verificar se os animais estão dentro do prado (excluindo fronteira)
    for pos in p:
        x = obter_pos_x(pos)
        y = obter_pos_y(pos)
        if x <= 0 or x >= max_x or y <= 0 or y >= max_y:
            raise ValueError("cria_prado: argumentos invalidos")
    # verificar se algum animal está na posição de um rochedo
    for pos1 in p:
        for pos2 in r:
            if posicoes_iguais(pos1, pos2):
                raise ValueError("cria_prado: argumentos invalidos")
    # verificar se todos os animais estão em posições diferentes
    for i in range(len(p)):
        for j in range(len(p)):
            if i != j:
                if posicoes_iguais(p[i], p[j]):
                    raise ValueError("cria_prado: argumentos invalidos")
    return [d, r, a, p]


def cria_copia_prado(m):
    """
    cria_copia_prado: prado -> prado
    Recebe um prado m e retorna uma cópia do mesmo prado.
    """
    return [el for el in m]


# --------------------------------------------------------------------------------------------------------------------#

# Seletores:

def obter_tamanho_x(m):
    """
    obter_tamanho_x: prado -> int
    Recebe um prado e devolve um inteiro correspondente à dimensão Nx do prado.
    """
    return obter_pos_x(m[0]) + 1


def obter_tamanho_y(m):
    """
    obter_tamanho_y: prado -> int
    Recebe um prado e devolve um inteiro correspondente à dimensão Ny do prado.
    """
    return obter_pos_y(m[0]) + 1


def obter_numero_predadores(m):
    """
    obter_numero_predadores: prado -> int
    Recebe um prado m e retorna o inteiro que representa o número de predadores no prado.
    """
    pred_cont = 0
    for animal in m[2]:
        if eh_predador(animal):
            pred_cont += 1
    return pred_cont


def obter_numero_presas(m):
    """
    obter_numero_presas: prado -> int
    Recebe um prado m e retorna o inteiro que representa o número de presas no prado.
    """
    presa_cont = 0
    for animal in m[2]:
        if eh_presa(animal):
            presa_cont += 1
    return presa_cont


def obter_posicao_animais(m):
    """
    obter_posicao_animais: prado -> tuplo posicoes
    Recebe um prado m e retorna um tuplo com posições ocupadas por animais, de acordo com a ordem
    de leitura do prado.
    """
    if m[3]:
        return ordenar_posicoes(m[3])
    return ()

def obter_animal(m, p):
    """
    obter_animal: prado x posicao -> animal
    Recebe um prado m e uma posição p e retorna o animal que ocupa essa posição.
    """
    for i in range(len(m[3])):
        if posicoes_iguais(m[3][i], p):
            return m[2][i]


# --------------------------------------------------------------------------------------------------------------------#

# Modificadores

def eliminar_animal(m, p):
    """
    eliminar_animal: prado x posicao -> prado
    Recebe um prado m e uma posição p e elimina o animal que se encontra na posição p, deixando-a
    livre. Retorna o próprio prado alterado.
    """
    for i in range(len(m[3])):
        if posicoes_iguais(m[3][i], p):
            m[3] = m[3][:i] + m[3][i+1:]
            m[2] = m[2][:i] + m[2][i+1:]
            return m
    return m


def mover_animal(m, p1, p2):
    """
    mover_animal: prado x posicao x posicao -> prado
    Recebe um prado m e duas posições p1, p2 e move o animal que se encontra na posição p1,
    deixando-a livre, para a posição p2. Retorna o próprio prado alterado.
    """
    for i in range(len(m[3])):
        if posicoes_iguais(m[3][i], p1):
            m[3] = m[3][:i] + (cria_posicao(obter_pos_x(p2), obter_pos_y(p2)),) + m[3][i + 1:]
            return m
    return m


def inserir_animal(m, a, p):
    """
    inserir_animal: prado x animal x posicao -> prado
    Recebe um prado m, um animal a e uma posição p e acrescenta ao prado o animal dado, que se
    encontra na posição fornecida como argumento.
    """
    m[2] += (a,)
    m[3] += (p,)
    return m


# --------------------------------------------------------------------------------------------------------------------#

# Reconhecedores:

def eh_prado(arg):
    """
    eh_prado: universal -> booleano
    Recebe qualquer argumento e devolve True somente se este corresponder a um TAD prado;
    senão, retorna False.
    """
    if not isinstance(arg, list):
        return False
    if len(arg) != 4:
        return False
    if not eh_posicao(arg[0]) or not all(isinstance(els, tuple) for els in (arg[1], arg[2], arg[3])):
        return False
    if len(arg[2]) < 1 or len(arg[3]) < 1 or len(arg[2]) != len(arg[3]):
        return False
    if not all(eh_posicao(obs) for obs in arg[1]) or not all(eh_animal(a) for a in arg[2]) \
            or not all(eh_posicao(pos_an) for pos_an in arg[3]):
        return False
    return True


def eh_posicao_animal(m, p):
    """
    eh_posicao_animal: prado x posicao -> booleano
    Recebe um prado m e uma posição p e retorna True se a posição p estiver ocupada por um animal.
    Em caso contrário, retorna False.
    """
    for pos in m[3]:
        if posicoes_iguais(pos, p):
            return True
    return False


def eh_posicao_obstaculo(m, p):
    """
    eh_posicao_obstaculo: prado x posicao -> booleano
    Recebe um prado m e uma posição p e retorna True se a posição p estiver ocupada por um
    obstáculo (montanha ou rochedo). Em caso contrário, retorna False.
    """
    # verificar montanhas
    max_x, max_y = obter_pos_x(m[0]), obter_pos_y(m[0])
    x, y = obter_pos_x(p), obter_pos_y(p)
    if x == 0 or y == 0 or x == max_x or y == max_y:
        return True
    # verificar rochedos
    for pos in m[1]:
        if posicoes_iguais(pos, p):
            return True
    return False


def eh_posicao_livre(m, p):
    """
    eh_posicao_livre: prado x posicao -> booleano
    Recebe um prado m e uma posição p e retorna True se a posição p não estiver ocupada por nenhum
    animal ou obstáculo; senão, retorna False.
    """
    if eh_posicao_obstaculo(m, p):
        return False
    if eh_posicao_animal(m, p):
        return False
    return True


# --------------------------------------------------------------------------------------------------------------------#

# Teste:

def prados_iguais(p1, p2):
    """
    prados_iguais: prado x prado -> booleano
    Recebe dois prados p1, p2 e retorna True se estes forem iguais. Caso contrário, retorna False.
    """
    return p1 == p2


# --------------------------------------------------------------------------------------------------------------------#

# Transformador:

def prado_para_str(m):
    """
    prado_para_str: prado -> str
    Recebe um prado m e retorna a cadeia de caracteres que o representa, com os limites
    representados por "+", "-", "|", obstáculos representados por "@" e animais representados por
    um caracter (minúsculo para presas, maiúsculo para predadores).
    """
    # inicia já com as montanhas em cima
    meadow = "+{}+\n".format("-" * (obter_tamanho_x(m) - 2))
    # principia na segunda linha e acaba na penúltima linha, excluindo as montanhas de cima e as
    # montanhas de baixo, que se adicionam individualmente
    for linha_y in range(1, obter_tamanho_y(m) - 1):
        # no início de cada linha, adiciona-se a montanha à esquerda "|"
        meadow += "|"
        # principia na segunda coluna e acaba na penúltima coluna, excluíndo as montanhas
        # à esquerda e à direita que são adicionadas individualmente
        for coluna_x in range(1, obter_tamanho_x(m) - 1):
            if eh_posicao_livre(m, cria_posicao(coluna_x, linha_y)):
                meadow += "."
            if eh_posicao_animal(m, (cria_posicao(coluna_x, linha_y))):
                meadow += animal_para_char(obter_animal(m, (cria_posicao(coluna_x, linha_y))))
            if eh_posicao_obstaculo(m, cria_posicao(coluna_x, linha_y)):
                meadow += "@"
        # no fim de cada linha, adiciona-se a montanha à direita e muda-se de linha
        meadow += "|\n"
    # montanhas em baixo
    meadow += "+{}+".format("-" * (obter_tamanho_x(m) - 2))
    return meadow


# --------------------------------------------------------------------------------------------------------------------#

# Funções de alto nível:

def obter_valor_numerico(m, p):
    """
    obter_valor_numerico: prado x posicao -> int
    Recebe um prado m e uma posição p e retorna o inteiro que representa a posição p consoante
    a ordem de leitura do prado.
    """
    nx = obter_tamanho_x(m)
    x, y = obter_pos_x(p), obter_pos_y(p)
    return (nx * y) + x


def obter_movimento(m, p):
    """
    obter_movimento: prado x posicao -> posicao
    Recebe um prado m e uma posição p e retorna a posição seguinte do animal nessa posição,
    segundo as regras de movimento no prado.
    """
    def metodo(lst, atual, m):
        num, p = obter_valor_numerico(m, atual), len(lst)
        return lst[num % p]
    # obter uma lista só com presas e uma só com posições livres
    adj, pos_presa, pos_livre = list(obter_posicoes_adjacentes(p)), [], []
    for posicao in adj:
        if eh_posicao_livre(m, posicao):
            pos_livre += [posicao]
        if eh_posicao_animal(m, posicao):
            if eh_presa(obter_animal(m, posicao)):
                pos_presa += [posicao]
    # movimento do predador
    if eh_predador(obter_animal(m, p)):
        if len(pos_presa) > 0:
            return metodo(pos_presa, p, m)
    # movimento da presa ou do predador se não existirem presas
    if len(pos_livre) == 0:
        return p
    return metodo(pos_livre, p, m)


# -##################################################################################################################-#
#                                                  FUNCOES ADICIONAIS                                                 #
# -##################################################################################################################-#


def geracao(m):
    """
    geracao: prado -> prado
    É a função auxiliar da principal, em que se recebe como argumento um prado m que é modificado de acordo com toda a
    evolução correspondente a uma geração, devolvendo o prado modificado. Cada animal efetua o seu turno seguindo a
    ordem de leitura do prado, de acordo com as regras de evolução.
    """
    posicoes = obter_posicao_animais(m)
    lst = []
    for pos in posicoes:
        # verifica se a posição atual se encontra na lista com posições de animais comidos;
        # se sim, pega na próxima posição e ignora este loop
        parar = False
        for el in lst:
            if posicoes_iguais(el, pos):
                parar = True
        if parar:
            continue
        a1, p2 = obter_animal(m, pos), obter_movimento(m, pos)
        aumenta_idade(a1), aumenta_fome(a1)
        if not posicoes_iguais(pos, p2):
            # se for um predador, move-se para uma posição com uma presa e dá reset à fome
            for p in obter_posicao_animais(m):
                if posicoes_iguais(p2, p):
                    eliminar_animal(m, p2)
                    reset_fome(a1)
                    lst += [p2]
                    break
            # move-se independentemente do resto
            mover_animal(m, pos, p2)
            # verifica se é um animal fértil; se sim, reproduz
            if eh_animal_fertil(a1):
                new_animal = reproduz_animal(a1)
                inserir_animal(m, new_animal, pos)
        # verifica-se se algum predador morre
        if eh_animal_faminto(a1):
            eliminar_animal(m, p2)
    return m


def simula_ecossistema(f, g, v):
    """
    simula_ecossistema: str x int x booleano -> tuplo
    Esta é a função principal do projeto, que permite simular o ecossistema de um prado.
    Recebe como argumentos uma cadeia de caracteres f, um inteiro g e um valor booleano v e devolve um tuplo com dois
    elementos, que correspondem ao número de predadores e de presas no final da simulação.
    A cadeia de caracteres f corresponde ao nome do ficheiro de configuração que contém os dados necessários para a
    simulação, o inteiro g indica o número de gerações que se pretende simular e o booleano v ativa o modo verboso,
    se for True, ou o modo quiet, se for False. O modo quiet apresenta o prado, o número de animais e o número de
    geração no início e no final da simulação. O modo verboso mostra também estas informações, não apenas no
    início e fim da simulação mas a cada geração em que ocorra alguma alteração no número de predadores ou presas.
    """
    with open(f) as file:
        cont = file.readlines()
    # cria um prado com a posição d (montanha canto inferior direito), o tuplo r (rochedos), o tuplo a (animais)
    # e o tuplo p (posições dos animais)
    d = eval(cont[0])
    d = cria_posicao(d[0], d[1])
    r = eval(cont[1])
    r = tuple([cria_posicao(r[i][0], r[i][1]) for i in range(len(r))])
    animais = [eval(el) for el in cont[2:]]
    a = tuple(cria_animal(animais[i][0], animais[i][1], animais[i][2]) for i in range(len(animais)))
    p = tuple(cria_posicao(animais[i][3][0], animais[i][3][1]) for i in range(len(animais)))
    prado, gen = cria_prado(d, r, a, p), 0
    presas, pred = obter_numero_presas(prado), obter_numero_predadores(prado)
    while gen <= g:
        # Modo quiet -> apenas dá print à geração 0 e à última geração
        if not v and (gen == 0 or gen == g):
            npresas, npred = obter_numero_presas(prado), obter_numero_predadores(prado)
            print('Predadores: {} vs Presas: {} (Gen. {})'.format(npred, npresas, gen))
            print(prado_para_str(prado))
        # Modo verboso -> dá print à primeira e última geração, e a todas as gerações em que se altere
        # o número de presas ou predadores
        if v:
            # número de presas e predadores da geração atual
            npresas, npred = obter_numero_presas(prado), obter_numero_predadores(prado)
            # compara-se o número de presas da geração anterior com a atual
            if npresas != presas or npred != pred or gen == 0:
                # atualizar número de presas e predadores
                presas, pred = npresas, npred
                print('Predadores: {} vs Presas: {} (Gen. {})'.format(pred, presas, gen))
                print(prado_para_str(prado))
        presas, pred = obter_numero_presas(prado), obter_numero_predadores(prado)
        geracao(prado)
        gen += 1
    return tuple((pred, presas))
