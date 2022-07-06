from classes import Pessoa

p1 = Pessoa('José Fábio', 48)
p2 = Pessoa('Aline Almeida', 41)

p1.comer('maçã')
p1.falar('POO')
p1.parar_comer()
p2.falar('Besteira')
p2.parar_falar()

nasc = p1.get_ano_nascimento()
print(nasc)
