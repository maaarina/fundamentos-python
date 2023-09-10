#calcular as raízes de uma equação quadrática

import numpy as np
#NumPy é uma biblioteca fundamental em Python para computação científica e numérica

def entrada_de_dados ():
    coeficiente = eval(input("Digite o valor do coeficiente"))
    return coeficiente

def calcula_delta (a, b, c):
    delta = b * b - 4 * a * c
    return delta

def calcular_raizes(a, b, c, delta):
    if a == 0 :
        resultado = "Não é uma equação quadrática (a = 0)"
    elif delta < 0 :
        resultado = "A equação não possui raízes nos números reais"
    elif delta == 0 :
        x = -b / (2 * a)
        resultado = f"a equação possui apenas a raíz {x}"
    else: #se delta for maior que 0
        x1 = (-b - np.sqrt(delta) / (2*a)) #np.sqrt = raíz quadrada
        x2 = (-b + np.sqrt(delta) / (2*a))
        resultado = f"a equação possui as raízes {x1} e {x2}"
    return resultado

a = entrada_de_dados ()
b = entrada_de_dados ()
c = entrada_de_dados ()

delta = calcula_delta(a, b, c)
resultado = calcular_raizes (a, b, c, delta)
print(resultado)
