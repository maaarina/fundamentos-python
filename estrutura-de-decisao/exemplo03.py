"""Implementar uma solução em python que resolva a seguinte questão:
- Se a nota for maior que 7 o estudante será aprovado
- Se a nota for menor que 7 e maior ou igual a 5 o estudante está em recuperação
- Se a nota for menor que 5 está reprovado!"""

nota = 6

if (nota >= 7):
    print("Aprovado!")
elif (nota >= 5):
    print("Está em recuperação!")
else:
    print("Reprovado!")
