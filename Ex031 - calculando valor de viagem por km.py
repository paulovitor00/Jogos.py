viagem = int(input('Digite quantos km serão percorridos: '))
longa = 200
if viagem >= 200:
    preco = viagem * 0.45
    print('A viagem terá {} e o valor por km é: R$0,45,'
          ' sendo assim o valor total da viagem será: R${:.2F}'.format(viagem, preco))
else:
    preco = viagem * 0.50
    print('A viagem terá {} e o valor por km é: R$0,50,'
          ' sendo assim o valor total da viagem será: R${:.2F}'.format(viagem, preco))