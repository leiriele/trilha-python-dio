
class Cachorro:
    def __init__(self, cor, nome, raca) -> None:
        self.cor = cor
        self.nome = nome
        self.raca = raca

b1 = Cachorro("caramelo", "nami", "vira-lata")
print(b1.cor, b1.nome, b1.raca)
