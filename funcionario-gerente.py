class Funcionario:
    def _init_(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario
        
    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"Salário: {self.__salario}")
        
class Gerente(Funcionario):
    def _init_(self, nome, cpf, salario, bonus):
        super()._init_(nome, cpf, salario)
        self.__bonus = bonus

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Bonus: {self.__bonus}")
        print(f"Sua salário após receber seu bonus: {self.get_salario() + self.__bonus}")
        
class Operacional(Funcionario):
    def _init_(self, nome, cpf, salario, turno):
        super()._init_(nome, cpf, salario)
        self.__turno = turno
        
    def exibir_dados(self):
        super().exibir_dados()
        print(f"seu turno é: {self.__turno}")

funcionario1 = Gerente("fabian", 12345678910, 7500, 300)
funcionario1.exibir_dados()

funcionario2 = Operacional("laura", 09876543210, 7700, "vespertino")
funcionario2.exibir_dados()
