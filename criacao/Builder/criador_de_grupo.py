from grupo import PessoaFisica
from grupo import PessoaJuridica

class CriadorGrupos:
    def __init__(self, nome_grupo):
        self.__nome_grupo = nome_grupo
        self.lista = [] #lista com todos os usuários

    @property
    def nome_grupo(self):
        return self.__nome_grupo

    @nome_grupo.setter
    def nome_grupo(self, atribuir_nome):
        self.__nome_grupo = atribuir_nome
    
    def AdicionaPessoaFisica(self, PessoaFisica):
        self.lista.append(PessoaFisica)

    def AdicionaPessoaJuridica(self, PessoaJuridica):
        self.lista.append(PessoaJuridica)
    
    def ImprimePessoas(self, lista):
        for pessoa in lista:
            if (pessoa.id==1):
                print(pessoa.nome, pessoa.cpf)
            else:
                print(pessoa.razao, pessoa.cnpj)
                
