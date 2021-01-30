# -*- coding: utf-8 -*-
dicionario = {"L":"Lucas", "M":"Matheus"}
print(dicionario["L"])
for chave in dicionario:
	print(chave + " = " + dicionario[chave])

for i in dicionario.items():
	print(i)

for v in dicionario.values():
	print(v)

for k in dicionario.keys():
	print(k)