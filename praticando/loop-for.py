s = 0
for i in range(5):
    s += 3*i
print(s)

#30

"""O laço for vai ser repetido cinco vezes, já que range(5) retorna a sequência (0, 1, 2, 3, 4). Vale observar que a instrução print(s) está fora do laço for, o que a levará a ser executada apenas uma vez quando o laço se encerrar. A variável s começa com valor zero e é acrescida, a cada iteração, do valor 3*i, sendo que i pertence à sequência (0, 1, 2, 3, 4). Ou seja, s recebe estes acréscimos: 0 + 3 + 6 + 9 + 12. Assim, ela termina o laço com o valor 30, que será impresso pela instrução print(s)."""
