import random
chance = 1
tentativa = int(input('Digite um número de 1 até 10.'))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteado = random.choice(lista)
while tentativa != sorteado:
    print('Você teve até agora: {}'.format(chance))
    chance += 1

    tentativa = int(input('Tente novamente, digite um número de 1 até 10.'))
print('Parabéns você acertou o número sorteado, que era: {} e precisou de {} chances.'.format(sorteado, chance))



