a = 0
for i in range(30): #abrir bloco ' : '
    if a % 2 == 0: 
        a += 1
        continue
    else:
        if a % 5 == 0: #*A identação é usada para delimitar blocos de código
            break
        else:
            a += 3
print (a) 
""" O bloco é encerrado quando a identação volta para o nível anterior. Ou seja, quando você retira a identação, o bloco é considerado encerrado. """
