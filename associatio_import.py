from association import Caneta, Escritor, MaquinaDeEscrever

escritor = Escritor('Fábio')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever('Olivette')

# Associação de classes
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
