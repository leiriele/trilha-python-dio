class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): #construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    #comportamentos/metodos
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self): 
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("azul", "caloi", 2023, 600) #instancia da bicicleta
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()

b3 = Bicicleta("vermelha", "monark", 1992, 189)
print(b3)
b3.buzinar()