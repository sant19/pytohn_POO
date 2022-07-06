'''
Manipulando strings
* String índices
* Fatiamento de strings [ínicio:fim:passo]
* Funções bult-in len, abs, type, print, etc...

Você pode conferir tudo isso em:
http://docs.python.org/3/library/stdtypes.html (tipos built-in)
http://docs.python.org/3/library/functions.html (funções built-in)
'''
# positivos [0, 1, 2, 3 , 4, 7, 8, 9]
text = 'Python s2'
print(text[0])
print(text[6])
print(text[7])

# negativos [-9, -8, -7, -6, -5, -4, -3, -2, -1]
print(text[-9])
print(text[-1])


new_string = text[2:6]
print(new_string)


new_string_1 = text[0:6:2]
print(new_string_1)
