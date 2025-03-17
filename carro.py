class Carro:
    def __init__ (self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 100
        self.velocidade = 0
        self.ligado = False

    def ligar(self):
        if self.combustivel > 0:
            self.ligado == True
        else:
            print("O carro está sem combustível! Abasteça o tanque para ligá-lo.")
    
    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado == False
        elif self.velocidade > 0:
            print("O carro está em movimento! Pare antes de poder desligá-lo.")
        else:
            print("O carro já está desligado.")
    
    def acelerar(self):
        if self.ligado and self.combustivel >= 5 and self.velocidade <= 90:
            self.velocidade += 10
            self.combustivel -= 5
        elif self.combustivel < 5:
            print("O carro não está com combustível o suficiente! Abasteça-o antes de poder acelerar.")
        elif 90 < self.velocidade < 100:
            self.velocidade = 100
            print("Velocidade máxima atingida!")
        elif self.velocidade == 100:
            print("O carro já atingiu sua velocidade máxima!")
        else:
            print("O carro está desligado!")
    
    def frear(self):
        if self.ligado and self.velocidade > 10:
            self.velocidade -= 10
        elif 0 < self.velocidade < 10:
            self.velocidade = 0
        elif self.ligado and self.velocidade == 0:
            print("O carro já está parado.")
        else:
            print("O carro está desligado!")

    def abastecer(self, quantidade):
        if self.combustivel + quantidade <= 100:
            self.combustivel += quantidade
        elif self.combustivel + quantidade > 100:
            self.combustivel == 100
            print("Essa quantidade vai além do limite! O tanque foi preenchido até sua capacidade máxima.")
        else:
            print("O tanque já está cheio.")
    
    def buzinar(self):
        if self.ligado:
            print("BEEP BEEP!")
        else:
            print("O carro está desligado.")
    
    def status(self):
        print("\nStatus do carro:\\n")
        print(f"Modelo: {self.modelo}\n")
        print(f"Ano: {self.ano}\n")
        print(f"Cor: {self.cor}\n")
        print(f"Combustível: {self.combustivel}\n")
        print(f"Velocidade em KM/h: {self.velocidade}\n")
        print(f"Ligado/Desligado: {self.ligado}")
    
Vrum= Carro("Fusca","2008","Azul")

Vrum.ligar()