# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2

largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))
area = largura * altura
litros = area / 2
print(f'A parede tem {area:.2f}m² e você precisará de {litros:.2f} litros de tinta.')