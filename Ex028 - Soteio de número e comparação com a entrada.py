import random
lista = [1, 2, 3, 4, 5]
sorteado = random.choice(lista)
tentativa = int(input('Digite um número de 1 a 5 para saber se o computador escolheu o mesmo número: '))
if sorteado == tentativa:
    print('O número sorteado é {} e é igual ao que foi digitado!, Parabéns você acertou!'.format(sorteado))
else:
    print('O número sorteado é {} e é DIFERENTE do que foi digitado, sinto muito!'.format(sorteado))

