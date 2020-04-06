#Classe de pessoa física : Possui nome e cpf
class PessoaFisica:
    def __init__(self, nome, cpf, id=1):
        self.__nome = nome
        self.__cpf = cpf
        self.__id = id
    
    @property 
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def id(self):
        return self.__id
    
    @nome.setter
    def nome(self, atribuir_nome):
        self.__nome = atribuir_nome

    @cpf.setter
    def cpf(self, atribuir_cpf):
        self.__cpf = atribuir_cpf


#Classe de Pessoa jurídica: Possui Razao social e cnpj
class PessoaJuridica:
    def __init__(self, razao, cnpj, id=2):
        self.__razao = razao
        self.__cnpj = cnpj
        self.__id = id
    
    @property 
    def razao(self):
        return self.__razao

    @property
    def cnpj(self):
        return self.__cnpj
        
    @property
    def id(self):
        return self.__id
    
    @razao.setter
    def razao(self, atribuir_razao):
        self.__razao = atribuir_razao

    @cnpj.setter
    def cnpj(self, atribuir_cnpj):
        self.__cnpj = atribuir_cnpj