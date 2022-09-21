import random
print('Vamos jogar par ou impar?')
jogo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = random.choice(jogo)
teste = 2
contador = 0
start = 0
while teste != 1:
    n = int(input('Digite um número: '))
    decisao = input('Faça sua escolha, digite: (p) para Par ou (i) Impar? ')
    jogo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = random.choice(jogo)
    start = a + n
    resto = start % 2
    if decisao == 'p':
        if resto == 0:
            print('Usuário venceu')
            teste = 0
            print(start)
            contador = contador + 1
        else:
            break
    elif decisao == 'i':
        if resto == 0:
            print('Usuário perdeu')
            teste = 1
            print('O total foi: {}'.format(start))
        else:
            print('O Usuário venceu')
            contador = contador + 1

print(f'O total foi {start}, e você venceu: {contador} partidas')



