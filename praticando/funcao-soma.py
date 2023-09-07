#Implementar uma solução que some todos os elementos pares de uma lista

def par(n):
    r = (n % 2 ==0)
    return r

def somar_par (lst):
    soma = 0
    for num in lst:
        if(par(num)):
           soma = soma + num
    return soma

lista = [10, 2, 5, 7, 6, 3]
soma = somar_par(lista)
print(f"a soma dos elementos pares é: {soma}")
