# faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05
novo_preco = preco - desconto
print(f'O produto que custava R${preco:.2f}, com 5% de desconto agora custa R${novo_preco:.2f}.')


