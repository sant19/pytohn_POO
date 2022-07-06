"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
secret = 'perfume'
typed = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letter = input('Digite uma letter: ')

    if len(letter) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    typed.append(letter)  # adiciona a letra

    if letter in secret:
        print(f'UHUULLL, a letra "{letter}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letter}" NÃO EXISTE na palavra secreta.')
        typed.pop()  # remove a letra

    temporary_secret = ''
    for secret_letter in secret:
        if secret_letter in typed:
            temporary_secret += secret_letter
        else:
            secret_letter += '*'

    if temporary_secret == secret:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {temporary_secret}')
        break
    else:
        print(f'A palavra secreta está assim: {temporary_secret}')

    if letter not in secret:
        chances -= 1

    print(f'Voce ainda tem {chances} chances')
    print()
