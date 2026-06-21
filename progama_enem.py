from funcionalidades import *
import os

def main():
    enem_2014 = carregar_arquivo()

    menu = '''
1 - Top N Brasil (todas as áreas) (filter)
2 - Top N Brasil por Área (filter)
3 - Top N por Estado (filter)
4 - Top N por Estado e Rede (pública ou privada) (filter)
5 - Media Nacional por Área (filter e reduce)
6 - Melhor escola por Área e Estado ou BR (filter) (reduce)
7 - Listas Escolas por Estado Ordenada Por Renda
8 - Busca escola específica por parte Nome (filter/find)
9 - Ranking ENEM por Estado (filter)
10 - Ranking ENEM por Região do País (filter)
0 - Sair
'''
    consulta = int(input(menu))

    while consulta != 0:

        if consulta == 1:

            n = int(input('N: '))
            listar(top_n(enem_2014, n))
            
        elif consulta == 2:

            n = int(input('N: '))
            area = input('matematica, linguagens, redacao, ciencias_natureza?: ')

            lista_ordenada = sorted(enem_2014, key=lambda x: x[area], reverse=True)
            listar(top_n(lista_ordenada, n))
           
        elif consulta == 3:

            n = int(input('N: '))
            estado = obter_estado('Estado: ')

            lista = filtrar(enem_2014, lambda x: x['uf'] == estado)
            listar(top_n(lista, n))
            
        elif consulta == 4:

            n = int(input('N: '))
            estado = obter_estado('Estado: ')
            rede = input('Rede: ')

            lista = filtrar(enem_2014, lambda x: x['uf'] == estado and x['rede'] == rede)
            listar(top_n(lista, n))

        elif consulta == 5:
            
            area = input('matematica, linguagens, redacao, ciencias_natureza?: ')

            lista = sorted(enem_2014, key=lambda x: x[area], reverse=True)

            somatorio = reduce(lista, 0, lambda inicio, dict, atributo:dict[atributo] + inicio, area)
            media = somatorio / len(lista)

            print(f'Média nacional na área {area} : {media:.2f}')

        elif consulta == 6:

            area = input('matematica, linguagens, redacao, ciencias_natureza?: ')
            estado = obter_estado('Estado: ')

            lista = filtrar(enem_2014, lambda x:x[area] and x['uf'] == estado)
            melhor_estado_area = reduce(lista, lista[0], lambda inicio, dict, atributo: dict if dict[atributo] > inicio[atributo] else inicio, area)
            melhor_br_area = reduce(enem_2014, enem_2014[0], lambda inicio, dict, atributo: dict if dict[atributo] > inicio[atributo] else inicio, area)

            print(f'Melhor do estado {estado} na área {area}:\n' ,melhor_estado_area)
            print(f'Melhor do Brasil na área {area}:\n' ,melhor_br_area)

        elif consulta == 7:

            estado = obter_estado('Estado: ')

            listar(sorted(filtrar(enem_2014, lambda x:x['uf'] == estado),key= lambda  x:x['nivel_socio_economico'], reverse = True))

        elif consulta == 8:

            parte_nome = input('Parte do nome: ')

            listar(filtrar(enem_2014, lambda x:x if parte_nome in x['nome'] else None))

        elif consulta == 9:

            uf = obter_estado('Estado: ')

            lista = filtrar(enem_2014, lambda x: x['uf'] == uf)

            listar(lista)
        elif consulta == 10:

            regiao = obter_regiao('Regiao: ')

            lista = filtrar(enem_2014, lambda x: x['uf'] == regiao)

            listar(lista)
        

        input('>')
        limpar_tela()
        consulta = int(input(menu))



main()