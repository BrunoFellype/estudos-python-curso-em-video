#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
real=float(input('Digite quanto você tem na sua carteira: R$'))

dolar=real*0.19
print(f'Você pode comprar até U${dolar:.2f}')