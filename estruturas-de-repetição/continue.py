# imprime todos os números de 1 até 10, pulando apenas o 5.
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')
