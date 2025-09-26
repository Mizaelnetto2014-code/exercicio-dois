nome=input('digite seu nome: ')
produto= input('informe o produto: ')
quantidade= int(input('informe a quantidade: '))
preco_unitario=float(input('digite o preco unitario: '))
valor_total=quantidade*preco_unitario
print('Compra realizada por ', nome)
print(f'produto: {produto}')
print(f'quantidade:{quantidade}')
print(f'preço:{preco_unitario}')
print('Total: ', valor_total)



