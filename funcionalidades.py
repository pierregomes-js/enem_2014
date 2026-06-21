import os

def carregar_arquivo():
    notas = []
    arquivo = open('enem2014_nota_por_escola.txt')
    linhas = arquivo.readlines()

    for linha in linhas:
        dado = linha.strip().split(';')
        nota = {'nome' : dado[1], 'municipio' : dado[2], 'uf' : (dado[3]), 'rede' : (dado[4]), 'permanencia' : (dado[5]), 'nivel_socio_economico' : (dado[6]), 'medias_objetivas' : float(replace(dado[7])), 'linguagens' : float(replace(dado[8])), 'matematica' : float(replace(dado[9])), 'ciencias_natureza' : float(replace(dado[10])), 'humanas' : float(replace(dado[11])), 'redacao' : float(replace(dado[12]))}
        notas.append(nota)

    arquivo.close()

    return notas

def limpar_tela():
    os.system('cls')

def replace(item):
    itens = item.split(',')
    
    novo_item = itens[0] + '.' + itens[1]
    

    return float(novo_item)


def filtrar(lista, condicao):
    nova_lista = []
    for dict in lista:
        if condicao(dict):
            nova_lista.append(dict)

    return nova_lista

def reduce(lista, inicio, op, atributo):
    valor_inicial = inicio
    for dict in lista:
        valor_inicial = op(valor_inicial, dict, atributo)

    return valor_inicial



def obter_estado(texto):
    estado = input(texto)
    return estado.upper()


def obter_regiao(regiao):
    regiao = input(regiao)
    regiao = regiao.lower()

    if regiao == 'nordeste':
        return ('PI' or 'MA' or 'CE' or'RN' or 'PB' or 'PE' or 'AL' or 'SE' or 'BA')
    elif regiao == 'norte':
        return ('AM' or 'PA' or 'AC' or'AP' or 'TO' or 'RR' or 'RO')
    elif regiao == 'sul':
        return ('RS' or 'SC' or 'PR')
    elif regiao == 'sudeste':
        return ('SP' or 'RJ' or 'MJ' or 'ES')
    else:
        return ('GO' or 'MS' or 'MT')


def listar(lista):
    for dict in lista:
        print(dict)
    print('-'*20)


def top_n(lista, n):
    lista_filtrada = []
    for index in range(0, len(lista)):
        if index < n:
            lista_filtrada.append(lista[index])
    return lista_filtrada
