class Colaborador(object):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Contador(Colaborador):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Analista(Colaborador):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Empresa(object):
    def __init__(self):
        self.colaboradores = list()

    def adiciona_colaborador(self, Colaborador):
        self.colaboradores.append(Colaborador)
    
    #def remove_colaborador()
    def exibe_colaboradores(self):
        print('Lista de colaboradores da empresa:')
        for colaborador in self.colaboradores:
            print(colaborador.nome)

    def calcula_salarios(self):
        salario_total = 0
        
        for colaborador in self.colaboradores:
            salario_total += colaborador.salario
        
        return salario_total
    
def main():
    colaborador1 = Contador('Felipe', 2800)
    colaborador2 = Analista('Ana', 3400)

    empresa1 = Empresa()
    empresa1.adiciona_colaborador(colaborador1)
    empresa1.adiciona_colaborador(colaborador2)

    empresa1.exibe_colaboradores()

    salario1 = empresa1.calcula_salarios()
    print('O salario total da empresa é:', salario1)

if __name__ == '__main__':
    main()
        