velocidade = int(input('Digite a velocidade do veiculo em KM/H sem a unidade: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('O veiculo passou com a velocidade de: {}KM/H e é a mais do que 80KM/H. A multa é de R${},00.'.format(velocidade, multa))
else:
    print('O veiculo passo com a velocidade de: {}KM/H, que é abaixo de 80KM/H, sendo assim não será multado!'.format(velocidade))
