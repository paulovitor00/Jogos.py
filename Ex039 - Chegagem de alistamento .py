import datetime
ano = int(input('Digite o ano do seu nascimento: '))
idade = 2022 - ano
if idade == 18 or idade == 17:
    print('Está na hora de se aliastar!')
elif idade > 18:
    print('Passou da hora de se alistar!')
else:
    falta = 18 - idade
    print('Ainda não é hora de se alistar, falta {} anos!'.format(falta))



