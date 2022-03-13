#networkx para teoría de grafos, matplot para gráficar, random para generar números aleatorios, stats para la entropia y solve para optimizar.
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from scipy import stats as st
import math


class object1:
    
    # Esta función genera un vector con probabilidades acumuladas de la distribución de pareto
    @staticmethod
    def pareto_cumm_probabilities(particiones, xfin, distribution=st.pareto.cdf):
        """
        (particiones,xfin) -----> (probability_cum_vector)
        Esta función recibe un xfinal hasta donde sumar y un número de particiones
        juntos definen la longitud y el valor máximo del vector resultante
        """
        dx = xfin/particiones
        x = []
        probability_cum_vector = []
        for i in range(particiones):
            equis = 1 + dx*i
            x.append(equis)
            # se eligió un coeficiente de 2.4 para la distribución de pareto
            pes = st.pareto.cdf(x[i], 2.4)
            probability_cum_vector.append(pes)
            # entrega como resultado el vector y los valores de x asociados
        return probability_cum_vector, x
