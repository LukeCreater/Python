# -*- coding: utf-8 -*-

"""
1 - Faça um programa que receba a idade do 
usuário e diga se ele é maior ou menor de idade.
"""

idade = 15
if idade >= 18:
	print("O usuário é maior de idade")
else:
	print("O usuário é menor de idade")

"""
2 - Faça um programa que receba duas notas digitadas pelo 
usuário. Se a nota for maior ou igual a seis, escreva 
aprovado, senão escreva reprovado.
"""



def inserir():
  nota = input("Qual a nota do aluno?")
  if float(nota) < 6:
      print ("Aluno reprovado")
  else:
      print ("Aluno aprovado")

try:
  inserir()
except:
  print('Você não digitou um número')
  inserir()

  """
  3 - Escreva um programa que resolva uma equação de segundo grau.

  Obrigado a Matheus Corrêa (mathycreater) por ter me ajudado a resolver
  https://github.com/mathycreater/
  """

from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)
 
if raiz_delta < 0:
    print("Delta negativo")
else:
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b + raiz_delta)/2*a
 
    print("As raízes são ", x1, " e ", x2)

"""
4 - Escreva um programa que ordene uma lista numérica com três elementos.   
"""

lista1 = [3,2,1]
print(sorted(lista))

"""
5 - 5. Escreva um programa que receba dois números e um sinal, 
e faça a operação matemática definida pelo sinal.   
"""

valor1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
valor2 = int(input("Digite o segundo número: "))
 
if sinal == "+":
    resultado = valor1 + valor2
 
elif sinal == "-":
    resultado = valor1 - valor2
 
elif sinal == "*":
    resultado = valor1 + valor2
 
elif sinal == "/":
    resultado = valor1 * valor2
 
else:
    print("Sinal inválido.")
 
print(resultado)