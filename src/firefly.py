import random
import math

import numpy as np


def firefly(d, n, gamma, alpha, beta, maxGeneration):
    """
    :param d: number of pipelines (weights)
    :param n: number of agents
    :param gamma: absorption coefficient
    :param alpha: random
    :param beta: attraction factor
    :param maxGeneration: number of max generation
    :return: best firefly
    """
    t = 0
    alpha_t = 1.0
    random.seed(0)
    lin = [0.0]*n

    fireflies = []
    z = [0]*n #Vetor para guardar os resultados das métricas
    ff_dis = [] #Matriz com os valores das distancias



    #Geracao inicial de fireflies
    #Geracao da matriz de distancias
    for i in range(n):
        ff = create_firefly(d)
        fireflies.append(ff)
        ff_dis.append(lin)


    while t < maxGeneration:
        for i in range(n):
            #Guarda o valor do resultado da metrica
            #de acordo com os pesos recebidos
            z[i] = iou_result(fireflies[i])

        #Indice dos valores de acordo com o resultado da metrica
        #Sendo a posicao indice[0] o com maior resultado da metrica
        indice = np.argsort(z)

        #Ordenando os resultados
        z.sort()
        #Invertendo o sinal de todos os resultados
        z = [-x for x in z]

        #Vetor para ranquear os vagalumes pela sua intensidade
        rank = [0]*n
        for i in range(n):
            rank[i] = fireflies[indice[i]]

        fireflies = rank

        for i in range(n):
            for j in range(n):
                ff_dis = dist(fireflies[i], fireflies[j])

        alpha_t = alpha * alpha_t

        for i in range(n):
            for j in range(n):
                if z[i] < z[j]:
                    ff = create_firefly(d)

                    beta_t = beta*math.exp(-gamma*(ff_dis[i][j]**2))

                    if i != n-1:
                        for k in range(d):
                            fireflies[i][k] = int(((1 - beta_t) * fireflies[i][k] + beta_t * fireflies[j][k] + alpha_t*ff[k]) / (1 + alpha_t))

        bests = fireflies[0]
        t += 1

    return bests

#Create a firefly with random weights

def create_firefly(n):
    dec = 1 #number of decimals

    ff = [random.random() for i in range(n)]
    ssum = sum(ff)
    ff = [i/ssum for i in ff]
    ff = [round(i, dec) for i in ff]
    return ff

def dist(a,b):
    d = 0
    for k in range(len(a)):
        d += (a[k] - b[k]) ** 2
    d = math.sqrt(d)
    return d