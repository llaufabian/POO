class Conta:
    def _init_(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Saldo após depósito: {self.__saldo}")

    def sacar(self, valor):
        if self._saldo + self._limite >= valor:
            self.__saldo -= valor
        else: 
            print("saldo bancário insuficiente :( ")

    def get_saldo(self):
        return self.__saldo
    
    def set_limite(self, valor):
        if valor >=0:
            self.__limite = valor
        else:
            print("Valor de limite não pode ser negativo!!")
    

conta1 = Conta("laura", 1500.0, 0)
print(f"Titular da conta: {conta1.get_titular()}")
print("Depósito Bancário")
valor = float(input("Digite o valor do depósito: "))
conta1.depositar(valor)
print("Saque Bancário")
valor = float(input("Digite o valor para saque: "))
conta1.sacar(valor)
print(f"Saldo bancário: {conta1.get_saldo()}")
print("Novo Limite bancário")
valor = float(input("Infome um novo limite: "))
conta1.set_limite(valor)
print("Saque Bancário")
valor = float(input("Digite o valor para saque: "))
conta1.sacar(valor)
print(f"Saldo bancário: {conta1.get_saldo()}")
