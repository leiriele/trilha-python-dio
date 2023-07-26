class Animal:
    def __init__(self, numero_patas) -> None:
        self.numero_patas = numero_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw) -> None:
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw) -> None:
        self.cor_bico = cor_bico
        super().__init__(**kw)
        
class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(numero_patas = 4, cor_pelo = "Branco")
print(gato)

cachorro = Cachorro(numero_patas = 4, cor_pelo = "Caramelo")
print(cachorro)

ornitorrinco = Ornitorrinco(numero_patas = 4, cor_pelo = "vermelho", cor_bico = "laranja")
print(ornitorrinco)