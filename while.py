while True:
    print()
    num_1 = input('Digite num_1: ')
    num_2 = input('Digite num_2: ')
    operator = input('Digite um operador: ')
    exit = input('Deseja sair? [s]im [n]ão: ')

    if exit == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '/':
        print(num_1 / num_2)
    elif operator == '*':
        print(num_1 * num_2)
    else:
        print('Essa não é uma operação válida.')


'''
While | Else
contadores
acumuladores
'''
count = 0
accumulator = 0

while count < 100:
    print(count)

    accumulator = accumulator + count  # = accumulator += count
    count += 1  # = count = count + 1
else:
    print('Cheguei no else.')


# Iterar string com while
phrase = 'O rato roeu a roupa do rei de Roma'
size_phrase = len(phrase)
count = 0
new_string = ''


while count < size_phrase:
    # print(phrase[count], count)
    letter = phrase[count]

    if letter == 'r':
        new_string += 'R'
    else:
        new_string += letter

    count += 1

print(new_string)
