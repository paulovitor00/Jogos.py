Salario = int(input('Digite o seu sálario: '))
Valor_casa = int(input('Digite o valor da casa: '))
a = int(input('Digite em quantos anos irá pagar o empréstimo: '))
m = a * 12
prestacao = (Valor_casa / m)  # calcula o valor de cada prestação mensal
if prestacao > Salario * 0.30: #condição para ver se o valor da prestação é maior que 30% do salário
    print('Para pagar em {} meses o valor da prestação fica {:.2f}, com o salário de: R$ {:.2f}.'
          'Sendo assim a prestação é maior do que 30% do sálario.'
          ' Portanto o empréstimo foi \033[1:41:30m NEGADO\033[m!'.format(m, prestacao, Salario))
else:
    print('O valor da prestação para pagar em {} meses é de: R$ {}. '
          'Como a prestação é menor que 30% do valor do salário que é R${} o empréstimo foi \033[1:41:30m APROVADO. \033[m')
