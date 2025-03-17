class Cachorro:
    def __init__ (self,nome,raça,comida):
        self.nome = nome
        self.raça = raça
        self.comida = comida
        self.acordado = True
        self.feliz = False
        self.energia = 100

    def dormir(self):
        self.energia = 100
        self.acordado = False
        print(f"{self.nome} está dormindo...zZz")

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado!")

    def brincar(self):
            if self.acordado and self.energia >= 20:
            self.feliz = True
            self.energia -= 20
            print(f"{self.nome} brincou e está feliz agora!")
            else:
            print(f"{self.nome} está cansado demais para brincar!")
        else:
            print(f"{self.nome} não pode fazer isso, ele está dormindo!")

    def comer(self):
        if self.acordado:
            self.comida -= 1
            self.feliz = True
            print(f"{self.nome} comeu! sua comida restante é: {self.comida}")
        else:
            print(f"{self.nome} não pode fazer isso, ele está dormindo!")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} latiu: Auau!")
        else:
            print(f"{self.nome} não pode fazer isso, ele está dormindo!")

Cachorro1 = Cachorro("Yuki", "Akita", 11)

Cachorro1.comer()
Cachorro1.brincar()
Cachorro1.brincar()
Cachorro1.brincar()
Cachorro1.brincar()
Cachorro1.brincar()
Cachorro1.brincar()
Cachorro1.dormir()
Cachorro1.latir()
Cachorro1.acordar()
