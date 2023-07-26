class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando motor ...")
        

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def verifica_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("vermelha", "ABC1234", 2)
moto.ligar_motor()
print(moto.cor,moto.placa,moto.numero_rodas)

carro = Carro("azul", "ABCD4567", 4)
carro.ligar_motor()
print(carro.cor,carro.placa,carro.numero_rodas)

caminhao = Caminhao("Verde", "ASDF1239", 8, False)
caminhao.ligar_motor()
caminhao.verifica_carregado()

