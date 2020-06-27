#Criado por Lucas Rosa 23/06/2020 - TCM, mapa de calor de uma figura geometrica
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def crie_matriz(n_linhas, n_colunas, valor):
    # criar a matriz
    matriz = []  # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = []  # lista vazia
        for j in range(n_colunas):
            linha.append(valor)
        # coloque linha na matriz
        matriz.append(linha)
    # print('matriz criada')
    return matriz


def compara_matriz(matriznova, matrizbase, max):
    # compara se os valores das matrizes estao estabilizados
    # se for maior que 0.5 ainda ocorre intercoes
    fim = 0
    for i in range(max):
        for j in range(max):
            if (matriznova[i][j] == None):
                pass
            else:
                prova = (matriznova[i][j] - matrizbase[i][j])
                if (prova < -0.5 or prova > 0.5):
                    fim += 1
    # Print para checar se estava realizando as comparcoes corretamente
    # print('fim é igual a :',fim)
    return fim


# função que atualiza os dados da matriz respeitando as condicoes de contorno
def atualiza_matriz(matriznova, matrizbase, mx, m20, m40, m60, m80, m0, fo):
    for i in range(mx):
        for j in range(mx):
            if (i == m0 and j < m20):
                pass
            elif (i < (m40 - 1) and j > (m20 - 1)):
                pass
            elif (i >= m60 and j < (m80 - 1)):
                pass
            elif (i > m0 and i < m40 and j == (m20 - 1)):
                pass
            elif (i < m60 and j == m0):
                pass
            elif (i == (m40 - 1) and j >= m20 and j < mx):
                pass
            elif (i >= m40 and i < mx and j == (mx - 1)):
                pass
            elif (i == (mx - 1) and j >= m80 and j < mx):
                pass
            elif (i >= m60 and i < mx and j == (m80 - 1)):
                pass
            elif (i == (m60 - 1) and j < m80 and j > m0):
                pass
            # atualizacao dos dados
            else:
                x = (matrizbase[i + 1][j] + matrizbase[i - 1][j] + matrizbase[i][j + 1] + matrizbase[i][j - 1]) * fo
                matriznova[i][j] = x + (1 - (4 * fo)) * matrizbase[i][j]
    return matriznova


def resolve():
    # variaveis o numero de nos
    my = 200
    mx = 200
    m20 = 40
    m40 = 80
    m60 = 120
    m80 = 160
    m0 = 0

    # temperaturas das condicoes de contorno
    ta = 100.0
    tb = 200.0
    tc = 200.0
    td = 400.0
    te = 300.0
    tf = 400.0
    tg = 450.0
    th = 500.0

    # valores usados para a atualizacao dos dados
    fo = 0.2
    atualizacao = 0
    resultado = 10

    # criacao das duas matrizes usadas no progama
    matriz = crie_matriz(mx, my, 0.0)
    matriz_2 = crie_matriz(mx, my, 0.0)


    # criando as condicoes de contorno
    for i in range(mx):
        for j in range(mx):
            if (i == m0 and j < m20):
                # linha A
                matriz[i][j] = ta
            elif (i < (m40 - 1) and j > (m20 - 1)):
                # espaço branco direita
                matriz[i][j] = 0.0
            elif (i >= m60 and j < (m80 - 1)):
                # espaço branco esquerda
                matriz[i][j] = 0.0
            elif (i > m0 and i < m40 and j == (m20 - 1)):
                # linha B
                matriz[i][j] = tb
            elif (i < m60 and j == m0):
                # linha H
                matriz[i][j] = th
            elif (i == (m40 - 1) and j >= m20 and j < mx):
                # linha C
                matriz[i][j] = tc
            elif (i >= m40 and i < mx and j == (mx - 1)):
                # linha D
                matriz[i][j] = td
            elif (i == (mx - 1) and j >= m80 and j < mx):
                # linha E
                matriz[i][j] = te
            elif (i >= m60 and i < mx and j == (m80 - 1)):
                # linha F
                matriz[i][j] = tf
            elif (i == (m60 - 1) and j < m80 and j > m0):
                # linha G
                matriz[i][j] = tg
            else:
                matriz[i][j] = 0.0

    # onde sera feita as atualizacoes dos dados
    while (resultado > 1):
        # copia da matriz
        matriz_2 = np.copy(matriz)
        # atualizacao dos valores de acordo com a equacao 17 e respeitando as condicoes de contorno
        matriz = atualiza_matriz(matriz, matriz_2, mx, m20, m40, m60, m80, m0, fo)
        # meu criterio de parada
        resultado = compara_matriz(matriz, matriz_2, mx)
        # variavel que usei para checar a quantidade de atulizacoes que o codigo contem
        atualizacao += 1

    #print('foram {} interacoes'.format(atualizacao))
    # Deu certo se aparecer isso
    # print('terminou saporra')
    #print(i, j)
    return matriz


