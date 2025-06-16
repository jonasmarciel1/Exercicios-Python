# faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Seu salário: '))
aumento = salario * 0.15
novoaumento = salario + aumento
print(f'O seu salário que era R${salario:.2f}, com 15% de aumento agora é R${novoaumento:.2f}.')
