# faça um programa que leia um número inteiro qualquer e mostre na sua tela a sua tabuada

n = int(input('Digite um número inteiro para ver sua tabuada: '))
print(f'\nTabuada do {n}:\n')
for i in range(1, 11):
 print(f'{n} x {i} = {n * i}')
