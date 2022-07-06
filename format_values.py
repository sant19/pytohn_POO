"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float) Ex.: :.2f
:(CARACTERE)(> OU < OU ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
> - Direita
^ - Centro
"""
nome = 'Fábio'
sobre_nome = 'Santos'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobre_nome)
print(nome_formatado)


nome_1 = 'José Fábio'
print(nome_1.lower())  # tudo minúsculo
print(nome_1.upper())  # tudo maiúsculo
print(nome_1.title())  # Primeiras letras maiúsculas
print(nome_1.capitalize())  # |Primeira letra maiúscula
