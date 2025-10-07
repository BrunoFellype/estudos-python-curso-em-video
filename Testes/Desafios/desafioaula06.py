#01 soma entre dois números
def soma():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    s = n1+n2

    #print('A soma entre {} e {} é igual a {}'.format (n1, n2, s))
    
    print(f'A soma entre {n1} e {n2} é igual a {s}')

#02 tipo de entrada
def tipo_input():
    n = input('Digite algo: ')

    if n.isspace()==False:
        if n.isalnum()==True:
            print ('O que você digitou é alfanumérico!')
            if n.isalpha()==True:
                print  ('Apenas contem letras do alfabeto!')
                if n.islower():
                    print ('Com apenas letras minúsculas!')
                else:
                    print('Contem também letra maiúscula!')
            elif n.isnumeric():
                print ('Apenas contem número!')        
            else:
                print('Contem mais de um tipo de caracter!')        
        else:
            print ('O que você digitou não é alfanumérico!')
    else:
        print('Foi digitado um espaço!')      

print('Escolha uma das opções:\n[1] Soma entre números\n[2] Tipo de entrada digitada')
x = int(input())

if x==1:
    soma()
elif x==2:
    tipo_input()
else:
    print('Opção inválida!')