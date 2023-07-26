class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class Aviao:
    def voar(self):
        print("Avião voando alto")
# é capaz de tratar cada objeto de forma polimórfica, chamando o método voar() 
# apropriado para cada tipo de objeto, sem depender do tipo específico do objeto em si.
def plano_voo(obj): 
    obj.voar()

pardal = Pardal()
avestruz = Avestruz()
aviao = Aviao()

plano_voo(pardal)   
plano_voo(avestruz)
plano_voo(aviao)   
