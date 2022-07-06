from composition import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insert_address('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.list_address()
print()

cliente2 = Cliente('Maria', 55)
cliente2.insert_address('Salvador', 'BA')
cliente2.insert_address('Recife', 'PE')
cliente2.insert_address('João Pessoa', 'PB')
print(cliente2.nome)
cliente2.list_address()
print()

cliente3 = Cliente('João', 25)
cliente3.insert_address('Fortaleza', 'CE')
print(cliente3.nome)
cliente3.list_address()
