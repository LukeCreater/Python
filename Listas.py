# -*- coding: utf-8 -*-
lista1 = ["Opa", "Eae"]
lista2 = [0,1,2,3,4,5,6]

for item in lista1:
	print(item)
tamanho = len(lista2) #Espera-se 6
print(tamanho)

lista1.append("Bão?")
print(lista1)

del lista2[5] #Os valores começam em 0

if 5 in lista2:
	print("5 está na lista 2")
else:
	print("5 não está na lista 2") #Espera-se funcionar o Else

pessoa = []
pessoa.append("Lucas")
print(pessoa)