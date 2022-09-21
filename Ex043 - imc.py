from math import sqrt
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
altura = altura * 2
calculo = peso / altura

if calculo < 18.5:
    print('O seu IMC está abaixo do peso!')
elif calculo >= 18.5 and calculo < 25:
    print('De acordo com seu IMC, seu peso '
          'e ideal.')
elif calculo >= 25 and calculo < 30:
    print('De acordo com seu IMC, você está acim do peso!')
elif calculo >= 30 and calculo < 40:
    print('Voceê esta com obesividade!')
else:
    print('Você está com obesidade morbida!')
