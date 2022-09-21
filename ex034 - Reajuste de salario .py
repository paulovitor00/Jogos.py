s = int(input('Digite o salário do funcionario: '))
teto = 1250
if s >= teto:
    ajuste = (s * 0.10) + s
    print('O salário que antes era {} vai passar a ser: {}'.format(s, ajuste))
else:
    ajuste = (s * 0.15) + s
    print('O salário que antes era {} vai passar a ser: {}'.format(s, ajuste))




