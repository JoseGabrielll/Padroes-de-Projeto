from abc import abstractmethod

#Classe mais abstrata que possui métodos abstrados, onde cada fábrica adapta e usa como quer
class Veiculo:

    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        
    def criar_moto(self):
        print('Uma moto', self.nome, 'foi criada')

    def criar_carro(self):
        print('Um carro', self.nome, 'foi criado')

class Honda:

    def criar_moto(self, Veiculo):
        Veiculo.criar_moto()
        
    
    def criar_carro(self, Veiculo):
        Veiculo.criar_carro()
       
def main():
    fabrica1 = Honda()
    moto1 = Veiculo('Bross', 'Moto')
    carro1 = Veiculo('HB20', 'Carro')
    fabrica1.criar_moto(moto1)
    fabrica1.criar_carro(carro1)

if __name__ == '__main__':
    main()
    
    
    

    
