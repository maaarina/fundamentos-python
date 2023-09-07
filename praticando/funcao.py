#Implementar uma solução que retorne o menor elemento de uma lista

def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if elem < minimo:
            minimo = elem
    return minimo

lista_teste = [2,5,7,4,1]
menor = encontrar_minimo(lista_teste)

print("O menor elemento da lista é [{}]".format(menor))
