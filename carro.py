class Carro:
    def __init__ (self, modelo, ano, cor, limvel):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.limvel = limvel
        self.combustivel = 0
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            print(f"{self.modelo} ligou!")
        else:
            print(f"O {self.modelo} está sem combustível! Abasteça o tanque para ligá-lo.")
    
    def desligar(self):
        if self.ligado:
            if self.velocidade == 0:
                self.ligado == False
                print(f"O {self.modelo} está em movimento! Pare antes de poder desligá-lo.")
        else:
            print(f"O {self.modelo} já está desligado.")
    
    def acelerar(self):
        if self.ligado is True:
            if self.combustivel >= 5:
                if self.velocidade < self.limvel:
                    self.velocidade += 10
                    self.combustivel -= 5
                    print(f"O {self.modelo} acelerou! Velocidade atual: {self.velocidade}Km/h")
                else:
                    print(f"O {self.modelo} já atingiu sua velocidade máxima!")
            else:
                print(f"O {self.modelo} não está com combustível o suficiente para acelerar.")
        else:
            print(f"O {self.modelo} está desligado.")
    
    def frear(self):
        if self.ligado:
            if self.velocidade >= 10:
                self.velocidade -= 10
            else:
                print(f"O {self.modelo} já está parado.")
        else:
            print(f"O {self.modelo} está desligado.")

    def abastecer(self, quantidade):
        if self.combustivel + quantidade <= 100:
            if self.velocidade == 0:
                self.combustivel += quantidade
                print(f"O {self.modelo} foi abastecido, combustível: {self.combustivel}")
            else:
                print(f"O {self.modelo} está em movimento, pare para abastecer.")

        elif self.combustivel == 100:
            print(f"O tanque do {self.modelo} já está cheio.")
        else:
            print(f"Abastecimento acima do limite de combustível.")
    
    def buzinar(self):
        if self.ligado:
            print(f"{self.modelo}: BEEP BEEP!")
        else:
            print(f"O {self.modelo} está desligado.")
    
    def status(self):
        print("\nStatus do carro:")
        print(f"- Modelo: {self.modelo}")
        print(f"- Ano: {self.ano}")
        print(f"- Cor: {self.cor}")
        print(f"- Combustível: {self.combustivel}")
        print(f"- Velocidade em KM/h: {self.velocidade}")
        print(f"- Ligado/Desligado: {self.ligado}")
    
Vrum= Carro("Fusca","1998","Azul", 100)
Vrum.abastecer(100)
Vrum.ligar()
for i in range (10):
    Vrum.acelerar()
Vrum.abastecer(20)
for i in range(10):
    Vrum.frear()
Vrum.buzinar()
Vrum.desligar()
Vrum.status()
