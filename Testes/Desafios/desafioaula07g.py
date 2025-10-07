#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco_prod=float(input('Digite o preço do produto: R$'))
preco_final=preco_prod-(preco_prod*0.05)
print(f'O novo preço será: R${preco_final}')