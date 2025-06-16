# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar

real = float(input('Quanto dinheiro você tem na carteira? (em R$?)'))
dolar = 5.54
dolares_comprados = real / dolar
print(f'Com R${real:.2f} você pode comprar US${dolares_comprados:.2f}')
