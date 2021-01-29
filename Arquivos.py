# -*- coding: utf-8 -*-
arquivo = open("arquivo.txt")
linhas = arquivo.read()
print (linhas)

w = open("arquivo2.txt", "a")
w.write("Esse é meu arquivo")
w.close()