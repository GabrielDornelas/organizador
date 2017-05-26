#Organizador master

import os

k = 1
for nome in os.listdir():
    for i in nome:
        if i == ".":
            ext = nome[(nome.find(i))::]
            break
    novo_nome = str(k)
    os.rename(nome, novo_nome+ext)
    k+ = 1
print ('OK')
