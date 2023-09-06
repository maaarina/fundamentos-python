peso = eval(input('Digite seu peso em quilogramas: '))
altura = eval(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")
