import random

jogo = ['Pedra', 'Papel', 'Tesoura']
a = random.choice(jogo)
tentativa = int(input('Digite o número da sua escolha: \n'
                      '1 - Pedra\n'
                      '2 - Tesoura\n'
                      '3 - Papel\n'))

print('O computador escolheu: {}'.format(a))

if tentativa == 1 or 2 or 3:
    if jogo == 'Pedra' and tentativa == 1:
        escolha = 'Pedra'
        print('Jokenpô\n'
              'computador: {}\n'
              'Usúario: {}'.format(a, escolha))
        print('O jogo empatou, pedra com pedra')
    elif a == 'Pedra' and tentativa == 2:
        escolha = 'Tesoura'
        print('Jokenpô\n'
              'computador: {}\n'
              'Usúario: {}'.format(a, escolha))
        print('O computador venceu, pedra derrota Tesoura')

    elif a == 'Pedra' and tentativa == 3:
        print('Jokenpô\n'
              'computador: {}\n'
              'Usúario: {}'.format(a, escolha))
        print('O USÚARIO venceu, papel vence pedra.')

    elif a == 'Papel' and tentativa == 1:
        escolha = 'Pedra'
        print('Jokenpô\n'
              'computador: {}\n'
              'Usúario: {}'.format(a, escolha))
        print('O computador venceu, Papel derrota pedra')

    elif a == 'Papel' and tentativa == 2:
        escolha = 'Tesoura'
        print('Jokenpô\n'
              'computador: {}\n'
              'Usúario: {}'.format(a, escolha))
        print('O Usuário venceu, Tesoura derrota papel')

    elif a == 'Papel' and tentativa == 3:
        escolha = 'Papel'
        print('Jokenpô\n'
          'computador: {}\n'
          'Usúario: {}'.format(a, escolha))
        print('O jogo empatou, papel com papel')

    elif a == 'tesoura' and tentativa == 1:
        escolha = 'Pedra'
        print('a')
        print('Jokenpô\n'
          'computador: {}\n'
          'Usúario: {}'.format(a, escolha))
        print('O usuario venceu, tesoura ganha de papel.')

    elif a == 'tesoura' and tentativa == 2:
        escolha = 'tesoura'
        print('Jokenpô\n'
          'computador: {}\n'
          'Usúario: {}'.format(a, escolha))
        print('O jogo empatou, tesoura com tesoura.')

    elif a == 'tesoura' and tentativa == 3:
        escolha = 'Papel'
        print('Jokenpô\n'
          'computador: {}\n'
          'Usúario: {}'.format(a, escolha))
        print('O computador venceu, tesoura vence papel.')


