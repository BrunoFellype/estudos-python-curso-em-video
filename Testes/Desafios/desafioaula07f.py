#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2

l=float(input('Qual a largura da parede(em metros)? '))
a=float(input('Qual a altura da parede(em metros)? '))

area=(a*l)/2
tinta=(area/2)

print(f'A parede possui {area} m2 de área, sendo necessário {tinta} litros de tinta para pintá-lo')