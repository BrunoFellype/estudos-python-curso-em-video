n1=int (input ("Digite a nota da 1ªVA:"))
n2=int (input("Digite a nota da 2ªVA:"))

media= (n1+n2)/2
print ("Sua média foi",media)
if media >=7:
    print ("Aprovado")
else:
    print ("Prova final")
    nfinal=int (input("Digite nota da prova final:"))
    if nfinal>=5:
        print ("Aprovado")
    else:
        print ("Reprovado")