#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal_inicial=float(input('Qual o seu salário? R$'))
sal_final=sal_inicial+(sal_inicial*0.15)
print(f'Seu novo salário será de R${sal_final}')