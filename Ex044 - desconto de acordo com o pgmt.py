preco = float(input('Digite o valor do produto: '))
pgmt = input('Digite a forma de pagamento: Débito, Crédito ou Dinheiro.')
if pgmt == 'Dinheiro':
    newPreco = preco - (preco * 0.10)
    print('Para pagamento no dinheiro o desconto é 10%,\n'
          'o preço do produto sem desconto é {},\n'
          'e com desconto fica: R${}.'.format(preco, newPreco))
elif pgmt == 'Débito':
    newPreco = preco - (preco * 0.05)
    print('Para pagamento no Débito o desconto é 5%,\n'
          'o preço do produto sem desconto é {},\n'
          'e com desconto fica: R${}.'.format(preco, newPreco))
elif pgmt == 'Crédito':
    parcela = float(input('Digite em quantas vezes deseja parcelar: \n'
                          '2 ou 3?'))
    if parcela == 2:
        print('Para crédito em duas vezes não temos desconto e o preço é: {}'.format(preco))
    elif parcela == 3:
        newPreco = preco + (preco * 0.20)
        print('Para parcelamentos em 3 vezes temos um juro de 20%\n'
              'antes o preço era: R${} mas ficou: R${}'.format(preco, newPreco))
else:
    print('Digite uma forma de pagamento valida!')
