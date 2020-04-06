class Fabrica:
    __instance = None

    def __new__(cls, nome, endereco):
        if Fabrica.__instance is None:
            Fabrica.__instance = object.__new__(cls)
            Fabrica.__instance.__nome = nome
            Fabrica.__instance.__endereco = endereco

            return Fabrica.__instance
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco

    
def main():
    #Criando o primeiro objeto (esse vai funcionar)
    fabrica1 = Fabrica('Honda', 'Av. Paulista')
    print(fabrica1) #Objeto foi criado com  sucesso
    print(fabrica1.nome, fabrica1.endereco)

    #Tentando criar outro objeto da mesma classe
    fabrica2 = Fabrica('Honda2', 'Av. Rio')
    print(fabrica2) #Vai printar o None, pois não foi criado

if __name__ == '__main__':
    main()